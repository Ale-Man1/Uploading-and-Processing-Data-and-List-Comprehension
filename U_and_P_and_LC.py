import pandas as pd


def main():
    # Part 1: Uploading data from github to Python using read_CSV
    df = pd.read_csv(
        'https://raw.githubusercontent.com/Ale-Man1/Uploading-and-Processing-Data-and-List-Comprehension/main/cars'
        '-sample35.csv')
    df.index += 1
    df.columns = ["Price", "Maintenance Cost", "Number of Doors", "Number of Passengers", "Luggage Capacity",
                  "Safety Rating", "Classification of Vehicle"]
    pd.set_option('display.width', None)
    print(df, "\n \n")

    # Part 2: Extracting each column into seven distinct Python list objects
    # Creating seven separate lists
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    # Nested for loop to get each element from the rows and columns into their respective list
    for col in df:
        for val in df[col].values:
            if col == "Price":
                # print(val)
                one.append(val)
            elif col == "Maintenance Cost":
                # print(val)
                two.append(val)
            elif col == "Number of Doors":
                # print(val)
                three.append(val)
            elif col == "Number of Passengers":
                # print(val)
                four.append(val)
            elif col == "Luggage Capacity":
                # print(val)
                five.append(val)
            elif col == "Safety Rating":
                # print(val)
                six.append(val)
            elif col == "Classification of Vehicle":
                # print(val)
                seven.append(val)
    # doesn't say to print so i wont

    # Part 3:
    list_p3 = []
    for i in range(len(one)):  # create for loop to traverse price and grab indices of prices that are med
        if one[i] == "med":
            list_p3.append(df.index[i])
    print("Index Values with med as the price: ", list_p3)

    # Part 4:
    list_p4 = []
    for i in list_p3:  # For loop created to traverse the numbers found in list_p3 and grab the values of passenger numbers for those specific indices
        list_p4.append(four[i - 1])
    print("Number of Passengers for the values with the price of med: ", list_p4)

    # Part 5:
    list_p5 = []
    for i in range(len(one)):  # For loop with if statement inside to grab indices with high price and non-low maintenance costs
        if one[i] == "high" and two[i] != "low":
            list_p5.append(df.index[i])
    print("Index Values with high price and not low maintenance cost: ", list_p5)

    # Part 6: Same as Part 3 but with list comprehensions
    list_p6 = [x for x in df.index[df['Price'] == 'med']]
    print(list_p6)

    # Part 7: Same as Part 4 but with list comprehensions
    list_p7 = [x for x in df["Number of Passengers"] if any(df.index == any(list_p6))]
    print(list_p7)

    # Part 8: Same as Part 5 but with list comprehensions
    list_p8 = [x for x in df.index[df['Price'] == 'high'] if df["Number of Passengers"].item != "low"]
    print(list_p8)

    # Part 1 of the question at the bottom (the only part):
    nlist = [[1, 2, 3], ["A", "B", "C"], [4, 5], ["D", "E"]]
    new_list = [a for b in nlist for a in b]
    print(new_list)


if __name__ == '__main__':
    main()
