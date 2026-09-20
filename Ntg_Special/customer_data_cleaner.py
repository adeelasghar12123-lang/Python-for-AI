customers = [
    {"name": "Ali", "email": "ALI@gmail.com", "city": "Lahore"},
    {"name": "Sara", "email": "sara@gmail.com", "city": "Karachi"},
    {"name": "ali", "email": "ali@gmail.com", "city": "Lahore"},
    {"name": "Hamza", "email": "HAMZA@GMAIL.COM", "city": "Islamabad"},
    {"name": "Sara Khan", "email": "SARA@gmail.com", "city": "Karachi"},
    {"name": "Ayesha", "email": "ayesha@yahoo.com", "city": "Lahore"},
    {"name": "Hamza", "email": "hamza@gmail.com", "city": "Islamabad"},
]
seen_emails = set()
unique_customers = []
duplicate_emails = []

def cleaning(customers):
    if not customers:
        return
    for customer in customers:
        customer["name"] = customer["name"].title()
        customer["email"] = customer["email"].lower()
        customer["city"] = customer["city"].title()
cleaning(customers)

def deduplication(customers,duplicate_emails):
    if not customers:
        return
    for customer in customers:
        if customer["email"] not in seen_emails:
            seen_emails.add(customer["email"])
            unique_customers.append(customer)
        else:
            duplicate_emails.append(customer["email"])
    
deduplication(customers,duplicate_emails)


def customers_by_city(unique_customers):
    city = {}
    if not unique_customers:
        return
    for customer in unique_customers:
        city_name = customer["city"]
        if city_name in city:
            city[city_name] += 1
        else:
            city[city_name] = 1
    return city

city = customers_by_city(unique_customers)



def city_with_most_customers(city):
    if not city:
        return
    max_count = max(city.values())
    most_customers = []
    for key,value in city.items():
        if value == max_count:
            most_customers.append(key)
    return most_customers



def unique_email_finder(unique_customers):
    if not unique_customers:
        return
    unique_email = {}
    for customer in unique_customers:
        email = customer["email"]
        parts = email.split("@")
        domain = parts[1]
        if domain in unique_email:
            unique_email[domain] += 1
        else:
            unique_email[domain] = 1
    return unique_email




def final_report():
    print("======= CUSTOMER REPORT =======")
    print(f'ORIGINAL CUSTOMERS : {len(customers)}')
    print(f'UNIQUE CUSTOMERS : {len(unique_customers)}')
    print(f'DUPLICATE EMAILS : {len(customers)-len(unique_customers)}')
    print()
    print("Duplicate Email Addresses")
    for mail in duplicate_emails:
        print(mail)
    print()
    print("Customers by city")
    for key,value in city.items():
        print(f'{key} : {value}')
    print()
    print("City with most customers")
    most_customers  = city_with_most_customers(city)
    for city_name in most_customers:
        print(city_name)
    print()
    print("EMAIL providers")
    dict_email_providers = unique_email_finder(unique_customers)
    for key,value in dict_email_providers.items():
        print(key,value)
    


final_report()