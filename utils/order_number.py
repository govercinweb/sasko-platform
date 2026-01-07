import random
import string


def order_number_generator(alpha_cnt=2, num_cnt=5):
    alphas = random.sample(string.ascii_uppercase, alpha_cnt)
    digits = random.sample(string.digits, num_cnt)
    sample = alphas + digits
    return "".join(sample)
