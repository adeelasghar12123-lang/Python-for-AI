vacation_plan = [
    {
        "place" : "Paris",
        "return flight" : 200,
        "hotel per day" : 20,
        "weekly car rental" : 200

    },

        {
        "place" : "London",
        "return flight" : 250,
        "hotel per day" : 30,
        "weekly car rental" : 120

    },

        {
        "place" : "Dubai",
        "return flight" : 370,
        "hotel per day" : 15,
        "weekly car rental" : 80

    },

        {
        "place" : "Mumbai",
        "return flight" : 450,
        "hotel per day" : 30,
        "weekly car rental" : 70

    },
]

def get_cheapest_vacation(vacation_plan = vacation_plan ):
    time = input("Input time duration for vacations(in days or in weeks or in months) : ") 
    parts = time.split()
    if len(parts) != 2:
        print("Enter duration in valid format e.g. = (4 days / 2 weeks / 1 month)")
        return
    if parts[1].lower().startswith("d"):
        days = int(parts[0])
        weeks = 0
        months = 0
    elif parts[1].lower().startswith("w"):
        weeks = int(parts[0])
        days = 0
        months = 0
    elif parts[1].lower().startswith("m"):
        months = int(parts[0])
        days = 0
        weeks = 0
    else:
        print("Invalid time unit. Use days, weeks, or months.")
        return

    days = days + 7*weeks + 30*months
    weeks = days // 7
    rent_weeks = weeks
    if days % 7 != 0:
        rent_weeks += 1

    min_cost = float('inf')
    final = ""
    for plan in vacation_plan:
        cost_per_week = plan["return flight"] + (plan["hotel per day"]*days) + (plan["weekly car rental"]*rent_weeks)
        if cost_per_week < min_cost:
            min_cost = cost_per_week
            final = plan["place"]
    print(f'Cheapest Destination : {final} ${min_cost}')
        

get_cheapest_vacation()



