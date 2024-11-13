f.close()
fo.close()


"""
My bearkfast
2 eggs
4oz ham
1pc whole wheat toast
4oz heinz baked beans
8oz. Orange Juice
4oz red cabbage sauerkraut
4oz pickled beets
"""

"""
Question: use food values file text file:
protiens(gr), calories
fat(gr), calories
total calories
"""
'''
# opens food data file
f = open("FoodValues.txt","r")


#create an output file 
fo = open ("Elements.txt","w")

#read into a large string
l = f.readline()
while(l != ''):
    tl = l.split('\t')
    tl1 = tl[0:11]
    so = ''
    for s in tl1:
        so += s+'\t'
    so = so + '\n'
    fo.write(so)
    l = f.readline()
'''
def getfooditems(amount):
    foodList = []

    for _ in range(amount):
        food = input("Please enter the name of the food: ")
        oz = float(input("Please enter how many ounces: "))  # Convert input to float for decimal values

        foodList.append({'Food': food, 'Ounces': oz})

    return foodList

# Example usage
num_items = int(input("How many food items are there? "))
items_list = getfooditems(num_items)
print(items_list)
        

f = open("Elements.txt","r")
foodList = []
while f hasline:
    newLine = curren Line
    foodList.add(newLine)


    data = newLine

    data_array = data.split('\t')

    print(data_array)
