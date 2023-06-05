from decimal import Decimal
def round_to_10_cents(x):
    remainder=x.remainder_near(Decimal('0.10'))
    if abs(remainder)==Decimal('0.05'):
       return x
    else:
        return x-remainder
