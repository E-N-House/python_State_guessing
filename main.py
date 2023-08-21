import pandas
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Gray_fur_count = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
black_fur = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
cinn_fur = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]

print(len(Gray_fur_count))
print(len(black_fur))
print(len(cinn_fur))
fur_colors = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "counts": [len(Gray_fur_count), len(black_fur), len(cinn_fur)],
}

pandas.DataFrame(fur_colors).to_csv("Fur Counts.csv")