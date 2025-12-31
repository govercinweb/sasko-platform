import datetime
from decimal import Decimal
from functools import lru_cache

import requests
from django.db import models
from lxml import etree


class Currency(models.Model):
    DEFAULT_CURRENCY_CODE = 'EUR'
    DEFAULT_CURRENCY_SYMBOL = '€'

    # WARNING: this may be removed in the future
    SYMBOLS = {
        'USD': '$',
        'TRY': '₺',
        'EUR': '€',
    }

    # WARNING: this may be removed in the future
    ORDERS = {
        'USD': 2,
        'TRY': 3,
        'EUR': 1,
    }

    code = models.CharField(max_length=5, unique=True)
    symbol = models.CharField(max_length=5, unique=True, null=True, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.code

    @classmethod
    @lru_cache
    def default_currency(cls):
        return cls.objects.get(code=cls.DEFAULT_CURRENCY_CODE)

    @classmethod
    def get_symbol(cls, currency_code):
        sym = cls.SYMBOLS.get(currency_code)
        if sym:
            return sym
        return currency_code

    @classmethod
    def get_order(cls, currency_code):
        order = cls.ORDERS.get(currency_code)
        if order:
            return order
        return 1999

    def convert(self, amount, to_code, date=None):
        if self.code == to_code:
            return amount
        if amount == Decimal('0'):
            return amount
        exchange_qs = ExchangeRate.objects.select_related(
            'from_currency',
            'to_currency',
        ).filter(
            models.Q(from_currency__code=self.code, to_currency__code=to_code)
            | models.Q(from_currency__code=to_code, to_currency__code=self.code),
        )
        exchange_rate = None
        if date is not None and exchange_qs.filter(date=date).exists():
            date_filtered_exchange_qs = exchange_qs.filter(date=date)
            exchange_rate = date_filtered_exchange_qs.last()
        if not exchange_rate:
            exchange_rate = exchange_qs.last()
        return exchange_rate.convert(amount=amount, from_code=self.code, to_code=to_code)


class ExchangeRate(models.Model):
    RATES = [
        'USD/TRY',
        'EUR/TRY',
        'EUR/USD',
    ]

    from_currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name='from_exchange_rates')
    to_currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name='to_exchange_rates')

    date = models.DateField()
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        unique_together = ['from_currency', 'to_currency', 'date']
        ordering = ['date']

    def __str__(self):
        return f'{self.date} - {self.rate}'

    @classmethod
    def refresh_from_tcmb(cls):
        response = requests.get('https://www.tcmb.gov.tr/kurlar/today.xml')
        root = etree.XML(response.content)
        # for elem in root.iter():
        #     print(elem)
        date_elem = root.xpath('//Tarih_Date')[0]
        date = datetime.datetime.strptime(date_elem.get('Tarih'), '%d.%m.%Y').date()

        usd_currency = None
        eur_currency = None
        for currency_elem in root.xpath('//Currency'):
            if currency_elem.get('CurrencyCode') == 'USD':
                usd_currency = currency_elem
            if currency_elem.get('CurrencyCode') == 'EUR':
                eur_currency = currency_elem

        data = {}
        for curr_elem in [usd_currency, eur_currency]:
            code = curr_elem.get('CurrencyCode')
            rate = None
            for elem in curr_elem.iter():
                if elem.tag == 'BanknoteBuying':
                    rate = Decimal(elem.text)
            data[(code, 'TRY')] = rate
        cross_rate = None
        for elem in eur_currency.iter():
            if elem.tag == 'CrossRateOther':
                cross_rate = Decimal(elem.text)
        data[('EUR', 'USD')] = cross_rate

        currency_map = {}
        for currency_codes in data.keys():
            for currency_code in currency_codes:
                if currency_code not in currency_map:
                    curr, is_created = Currency.objects.update_or_create(
                        code=currency_code,
                        defaults=dict(
                            symbol=Currency.get_symbol(currency_code),
                            order=Currency.get_order(currency_code),
                        )
                    )
                    currency_map[currency_code] = curr

        dates = [date]
        if date < datetime.datetime.now().date():
            dates.append(date + datetime.timedelta(days=1))
        for date in dates:
            for (from_curr_code, to_curr_code), rate in data.items():
                exchange_rate, is_created = cls.objects.update_or_create(
                    date=date,
                    from_currency=currency_map[from_curr_code],
                    to_currency=currency_map[to_curr_code],
                    defaults=dict(
                        rate=rate,
                    )
                )
                # TODO: why does the next line here?
                exchange_rate.refresh_from_db()
        return True

    def convert(self, amount, from_code, to_code):
        if self.from_currency.code == from_code and self.to_currency.code == to_code:
            return round(amount * self.rate, 2)
        elif self.from_currency.code == to_code and self.to_currency.code == from_code:
            return round(amount / self.rate, 2)
        else:
            raise Exception(f'There is no currency conversion from {from_code} to {to_code}')


class Sellable(models.Model):
    name = models.CharField(max_length=180, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
