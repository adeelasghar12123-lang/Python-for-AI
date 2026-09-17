sales = [
    {"product": "Laptop", "category": "Electronics", "quantity": 2, "price": 800},
    {"product": "Mouse", "category": "Electronics", "quantity": 5, "price": 20},
    {"product": "Chair", "category": "Furniture", "quantity": 3, "price": 100},
    {"product": "Laptop", "category": "Electronics", "quantity": 1, "price": 800},
    {"product": "Desk", "category": "Furniture", "quantity": 2, "price": 250},
    {"product": "Mouse", "category": "Electronics", "quantity": 3, "price": 20},
]


def total_revenue(sales):
    total_revenue = 0
    for product in sales:
        total_revenue += product["quantity"]*product["price"]
    return total_revenue 

def rev_per_prdct(sales):
    rev_pp = {}
    for item in sales:
        revenue = item["quantity"]*item["price"]
        product_name = item["product"]
        if product_name in rev_pp:
            rev_pp[product_name] += revenue
        else:
            rev_pp[product_name] = revenue
    return rev_pp

def best_product(sales):
    best_quantity = 0
    best_product = ""
    for item in sales:
        if item["quantity"] > best_quantity:
            best_quantity = item["quantity"]
            best_product = item["product"]
    return {best_product : best_quantity}

mew = best_product(sales)

for key,value in mew.items():
    print(key,value)
