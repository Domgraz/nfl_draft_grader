import csv
import matplotlib.pyplot as plt
import pandas as pd

file = "top250_concensus_board.csv"
num = []
p_name = []
top_250 = {}
input_dict = {}

# def get opens the file initialized above, reads the name and ranking number 
# associated with the player and combines them into one dictionary to return

def get(file):
    with open(file, 'r') as csv_file:
     csv_reader = csv.reader(csv_file)
     for line in csv_reader:
         num.append(line[0])
         p_name.append(line[1])   
    num.remove("consensus_number")
    p_name.remove("player_name")
    
    for i in range(0,len(num)):
        num[i]= int(num[i])
        
    for i in range(len(num)):
        top_250[p_name[i]]= num[i]
   
    return top_250

# def inputs will take the given name and pick number in a loop until end is entered
# the name will be put into all uppercase to avoid problems in the compare fucntion
# these are then put into the input_dict and returned

def inputs():
    name = 0
    keys = []
    values = []
    while name != "END":
        name = input("Enter player full name or end:")
        name = name.upper()
        if name == "END":
            break
        keys.append(name)
        pick_num = int(input("Enter pick player was selected with:"))
        values.append(pick_num)
    
    for i in range(len(keys)):
        input_dict[keys[i]]= values[i]
    
    return input_dict

# def compare will take two dictionaries, compare the numbers given, print out 
# the difference and also display a graph showing the difference for each player

def compare(dict_1,dict_2):
    diff_dict = {}
    difference = []
    names = []

# this loop will take the name from the first list and see if it is in the second list
# if there is a identical name it will append to the diff_dict and then the difference 
# will be computed and returned as the value pairing, if no match it passes

    for i in dict_1:
       if i in dict_2:
            name = i
            diff = dict_2[i]-dict_1[i]
            names.append(name)
            difference.append(diff)
            for i in range(len(names)):
                diff_dict[names[i]] = difference[i]
       else:
            pass
            
# this segment uses matplotlob.pylot to generate a scatter plot for each of the players 
# input by the user

    name = list(diff_dict.keys())
    value = list(diff_dict.values())
    plt.scatter(name,value)
    plt.show()

# this part takes the numerical difference and assigns a A-E grade depending on the 
# percieved value, then it will print out the player names and grades
# finally the same text being printed will be exported to a csv file named pick_ratings.csv

    for i in range(len(names)):
        if difference[i] > 5:
            diff_dict[names[i]] = "A"
        elif difference[i] >= 0 and difference[i] < 5:
            diff_dict[names[i]] = "B"
        elif difference[i] < 0 and difference[i] > -5:
                diff_dict[names[i]] = "C"
        elif difference[i] >= -5 and difference[i] > -10 :
            diff_dict[names[i]] = "D"
        elif difference[i] <= -10:
            diff_dict[names[i]] = "E"

    for key,value in diff_dict.items():
        print(key +": "+ value )
    
    (pd.DataFrame.from_dict(data = diff_dict,orient = 'index')).to_csv("pick_ratings.csv",header = False)

compare(get(file),inputs())

        
    




