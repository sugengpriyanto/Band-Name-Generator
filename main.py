print("Welcome to Band Name Generator")
city = input("What city did your band formed?\n")
pet = input("What is your pet name?\n")
leader = input("What is the name of the band leader?\n")
noun = input("Type a singular noun in your mind right now\n")
tm = input("What is your favourite Day, Month, or Season?\n")
col = input("What is your favourite color?\n")
body = input("Type a part of human body\n")

name1 = city + " " + pet
name2 = noun + " " + leader
name3 = col + " " + tm
name4 = col + " " + body
name5 = city + " " + tm
name6 = col + " " + leader
name7 = noun + " " + pet
name8 = col + " " + pet

name = [name1, name2, name3, name4, name5, name6, name7, name8]

for i in name:
  print(i)