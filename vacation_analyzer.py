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

def get_cheapest_vacation(vacation_plan):
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
        



















def get_max_days_for_budget(vacation_plan):
    try:
        budget = float(input("Enter your maximum budget: $"))
        if budget <= 0:
            print("Please enter a valid budget greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    best_place = ""
    max_days = 0
    best_cost = 0

    for plan in vacation_plan:
        days = 1
        
        # Keep increasing the days by 1 until the cost exceeds the budget
        while True:
            # Reusing your original car rental logic!
            rent_weeks = days // 7
            if days % 7 != 0:
                rent_weeks += 1
                
            cost = plan["return flight"] + (plan["hotel per day"] * days) + (plan["weekly car rental"] * rent_weeks)
            
            # Check if this duration is affordable
            if cost <= budget:
                if days > max_days:
                    max_days = days
                    best_place = plan["place"]
                    best_cost = cost
                # Tie-breaker: If it gives the SAME max days, but is cheaper, pick this one instead
                elif days == max_days and cost < best_cost:
                    best_place = plan["place"]
                    best_cost = cost
                    
                days += 1 # Move to check the next day
            else:
                break # Cost exceeded budget, break the loop and check the next destination
                
    if max_days == 0:
        print(f"\nSorry, a budget of ${budget} is too low to stay at any destination for even 1 day.")
    else:
        print(f"\n--- Best Recommendation for ${budget} ---")
        print(f"Destination: {best_place}")
        print(f"Max Duration: {max_days} days")
        print(f"Total Cost: ${best_cost}")

# --- Main Menu ---
print("Welcome to the Vacation Planner!")
print("1. Find the cheapest destination for a specific duration")
print("2. Find the longest possible vacation for a specific budget")
choice = input("Enter 1 or 2: ")

if choice == "1":
    get_cheapest_vacation(vacation_plan)
elif choice == "2":
    get_max_days_for_budget(vacation_plan)
else:
    print("Invalid choice. Please run the script again.")

