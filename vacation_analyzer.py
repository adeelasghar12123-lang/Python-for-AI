vacation_plan = [
    {
        "place" : "Paris",
        "return flight" : 200,
        "hotel per day" : 100,
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
        "hotel per day" : 10,
        "weekly car rental" : 70

    },
]

def duration(time = input("Input time in weeks :") ,vacation_plan = vacation_plan ):
    time = time.split()
    weeks = int(time[0])
    cost_per_week_min = vacation_plan[0]["return flight"] + (vacation_plan[0]["hotel per day"]*7) + vacation_plan[0]["weekly car rental"]
    final = vacation_plan[0]["place"]
    for dict in vacation_plan:
        cost_per_week = dict["return flight"] + (dict["hotel per day"]*7) + dict["weekly car rental"]
        if cost_per_week < cost_per_week_min:
            cost_per_week_min = cost_per_week
            final = dict["place"]
    print(final)
        

duration()



