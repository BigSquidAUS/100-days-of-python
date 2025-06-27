# Create a .csv called squirrel_count.csv containing a small table that shows squirrel fur colour
# and count. (Primary Fur Color)

import pandas

squirrel_data = pandas.read_csv(filepath_or_buffer="2018-squirrel-data.csv")
squirrel_fur_colour = squirrel_data["Primary Fur Color"] # Gray, Cinnamon, Black

count_gray = 0
count_cinnamon = 0
count_black = 0

for fur in squirrel_fur_colour:
   if fur == "Gray":
       count_gray += 1
   elif fur == "Black":
       count_black += 1
   elif fur == "Cinnamon":
       count_cinnamon += 1

# print(f"Gray Squirrels: {count_gray}\nCinnamon Squirrels: {count_cinnamon}\nBlack Squirrels: {count_black}")

squirrel_fur_dict = {
    "colour" : ["Gray","Cinnamon","Black"],
    "count" : [count_gray, count_cinnamon,count_black]
}

data = pandas.DataFrame(squirrel_fur_dict)
data.to_csv("squirrel_count.csv")