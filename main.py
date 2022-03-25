# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#This is a very easy test example of code

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# open the file named numbers.txt and print it
myfile = open("/Users/marigrini/numbers.txt", "r")
print(myfile.read())

#Open the file, read the lines in the file into a list and sort the list
with open("/Users/marigrini/numbers.txt", "r") as filestream:
    for line in filestream:
        currentline = line.split(",")
        print "This is the list with numbers from the file", currentline
        currentline.sort()
        print "This is the sorted list", currentline




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
