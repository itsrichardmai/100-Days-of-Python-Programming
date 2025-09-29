# import csv
# Using pandas allows us to handle data much more smoothly. 
import pandas 


data = pandas.read_csv("NYSData.csv")
    
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels = len(data[data["Primary Fur Color"] == "Red"])
print(grey_squirrels)
print(black_squirrels)
print(red_squirrels)
    
data_dict = {
        "Fur Color": ["Grey", "Black", "Red"],
        "Count": [2473, 103, 0]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


    # Before Pandas 
    # with open('./weather_data.csv') as data_file:
    #     data = csv.reader(data_file)
    #     temperatures = []
    #     for row in data:
    #         if row[1] != "temp":
    #             temperatures.append(int(row[1]))
    #         print(temperatures)

    # After Pandas 
    # data = pandas.read_csv("weather_data.csv")
    # data_dict = data.to_dict()
    # print("\nData Dict:", data_dict)

    # temp_list = data["temp"].to_list()
    # print("\nTemp List:", temp_list)

    # Challenge: Try to find the average of the temperatures 
    # mean = 0 
    # for i in temp_list:
    #     mean += i
    # mean /= len(temp_list)
    # print("\nMean:", mean)
    # # Easier way to do it using the documentation of pandas
    # print("\nMean using .mean():" ,data["temp"].mean())
    # print("Print(data['temp']].max()): ", data["temp"].max())
    # print("Print(data['condition']:", data["condition"])
    # print("Print(data.condition)", data.condition)
    # # Get Data in Row 
    # print(data[data.day == "Monday"])
    # # Find the day where the temperature was the maximum
    # print(data[data.temp == data.temp.max()])
    # monday = data[data.day == "Monday"]
    # print("Monday's Temperature:", monday.temp)
    # monday_temp = monday.temp[0]
    # monday_temp_F = monday_temp * 9/5 + 32
    # print(monday_temp_F)

    # # Create a dataframe from scratch 
    # data_dict = {
    #     "students": ["Any", "James", "Angela"],
    #     "scores": [76, 56, 65]
    # }
    # data = pandas.DataFrame(data_dict)
    # data.to_csv("new_data.csv")
