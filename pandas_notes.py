import pandas
#
# data = pandas.read_csv("../Python_Project_25/weather_data.csv")
#
# # print(type(data)) ===> DataFrame
# # print(data)
#
# # print(type(data["temp"])) ===> Series
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # transforms each column into a dictionary
# # print(type(data_dict))
# # print(data_dict)
#
# # can transform each series into a list
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# #
# # # average_temp = sum(temp_list)/len(temp_list)
# # # using panda's built in series methods
# # average_temp = data["temp"].mean()
# # print(average_temp)
# #
# # max_temp = data["temp"].max()
# # print(data.temp.max())
# # # can use dot notation as pandas automatically makes the columns named attributes
# # print(data.day)
#
# # getting data from a row and filtering it
# monday = data[data.day == "Monday"]
#
# # how to get the row with max temp.
# print(data[data.temp == data.temp.max()])
#
# # filter multiple criteria in rows
# weekend = data[data["day"].isin(["Saturday", "Sunday"])]
# # the above inherits the attributes of the column names
# print(weekend.condition)
#
# # convert monday's temps to Far (0°C × 9/5) + 32 = 32°F
# # note this version of pandas knows to make them ints
# mondayFarTemp = ((monday.temp * 9/5) + 32)
# print(mondayFarTemp)
#
# Creating own DataFrame from scratch
data_dict = {
    "students": ["beth", "liz", "elizabeth"],
    "scores": [30, 40, 50],
}

new_dataframe = pandas.DataFrame(data_dict)
print(new_dataframe)
# new_dataframe.to_csv("testing.csv")

