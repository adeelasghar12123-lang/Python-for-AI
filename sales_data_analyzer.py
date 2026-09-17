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

def rev_by_cat(sales):
    rev_bc = {}
    for item in sales:
        revenue = item["quantity"]*item["price"]
        category_name = item["category"]
        if category_name in rev_bc:
            rev_bc[category_name] += revenue
        else:
            rev_bc[category_name] = revenue
    return rev_bc

def expensive_sale(sales):
    highest_amount = 0
    for item in sales:
        total_sale = item["quantity"]*item["price"]
        if total_sale > highest_amount:
            highest_amount = total_sale
            product_name = item["product"]
            product_sale =  total_sale
    return {product_name : product_sale}

def final_report():
    print("====== SUMMARY ======")
    print(f'TOTAL REVENUE : {total_revenue}')
    print()
    print("=== Revenue by product ===")
    print()
    rev_per_product_dic = rev_per_prdct(sales)
    for key,value in rev_per_product_dic.items():
        print(key,value)
    print()
    b_p = best_product(sales)
    for key,value in b_p:
        print(f'Best selling product is : {key}')
    print()
    print("=== REVENUE BY CATEGORY ===")
    rev_by_cat_dic = rev_by_cat(sales)
    for key,value in rev_by_cat_dic.items():
        print(key,value)
