promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    discount = 0
    return discount

@promotion
def bulk_item(order):
    discount = 0
    return discount

@promotion
def large_order(order):
    discount = 0
    return discount

def best_promo(order):
    return max(promo(order) for promo in promos)
