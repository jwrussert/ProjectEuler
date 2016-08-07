import numpy
import itertools

#import the csv into a numpy array
numbers = numpy.genfromtxt(r"C:\Users\jwrus_000\Google Drive\Documents\Python Scripts\Euler\067_Maximum_Path_Sum_2.csv", delimiter=",", dtype ="int")


#the array will consider all blank values as -1. So I want convert those to 0s
numbers[numpy.array(numbers)<0] = 0

TempSum = 0 #a variable to store the current path sums so they can be compared

for row in range(len(numbers)-1, 0, -1): #scroll through all rows, from the bottom up to the second row
    for col in range(len(numbers[row])-1):  #scroll through each pair of numbers in the row to figure out which number is higher
        if numbers[row-1][col] > 0:
            TempSum = numbers[row][col] #just set it to the left number first, then decide if the right number is higher
            if numbers[row][col+1] > TempSum:
                TempSum = numbers[row][col+1]

            numbers[row-1][col] = numbers[row-1][col] + TempSum #replace the number directly above with the sum of that number and he ideal path below it


print(numbers[0][0])
