capitals = {
    "France": "Paris",
    "Germany": "Berlin",

}

# nested list in dictionary 

travel_log = {
    "France": ["Paris", "Lillie", "Dijon"],
    "Germancy": ["Stuttgart", "Berlin"]
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1]) #prints D 

# nested list in dict in dict travel log.

complex_travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lillie", "Dijon"],
        "total_visits": 12
    },
    "Germany":{
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

print(complex_travel_log["Germany"]["cities_visited"][2])