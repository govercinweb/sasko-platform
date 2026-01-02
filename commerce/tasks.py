from celery import shared_task

from commerce.models import ExchangeRate


@shared_task
def refresh_exchange_rates_from_tcmb():
    ExchangeRate.refresh_from_tcmb()
