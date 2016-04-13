import os
import csv
import sys

#ENUMERATION ALGORITHM
# O(n^3)
def enumeration(array):
    
    Sum = 0
    maxStart = 0
    maxStop = 0
    
    for i in range(0, len(array)):
        currentStart = i
        
        for j in range(i, len(array)):
            current = 0
            currentStop = j
            
            for k in range(i, j + 1):
                current += array[k]
                
                if current > Sum:
                    Sum = current
                    maxStart = currentStart
                    maxStop = currentStop
    
    return Sum

#BETTER ENUMERATION ALGORITHM
# O(n^2)
def betterEnumeration(array):
    
    maxSum = 0
    maxStart = 0
    maxStop = 1
    k = 0
    
    for i in range(0, len(array)):
        sumNum = 0
        currentStart = i
        
        for j in range(i, len(array)):
            sumNum = sumNum + array[j]
            currentStop = j
            
            if sumNum > maxSum:
                maxSum = sumNum
                maxStart = currentStart
                maxStop = currentStop
    
    return maxSum

#DIVIDE AND CONQUER
#referenced https://copingwithcomputers.com/2014/05/17/maximum-subarray-problem/
# O(nlogn)
def divideCrossover(array, start, middle, end):
    
    currentLeftSum = 0
    leftSum = -sys.maxint - 1
    currentRightSum = 0
    rightSum = -sys.maxint - 1
    leftIndex = middle
    rightIndex = middle+1
    
    #for the crossover range we have to find the values for everything including the middle value
    for i in range(middle, start-1, -1):
        currentLeftSum += array[i]
        
        if currentLeftSum > leftSum:
            leftSum = currentLeftSum
            leftIndex = i
    
    for j in range(middle+1, end+1):
        currentRightSum += array[j]
        
        if currentRightSum > rightSum:
            rightSum = currentRightSum
            rightIndex = j
    
    return (leftIndex, rightIndex, leftSum + rightSum)

#Used with divideCrossover() for D&C, returns sum
def divideAndConquer(array, start = 0, end=None):
    
    if end is None:
        end = len(array)-1
        
    #base case. if n = 1
    if end == start:
        return start, end, array[start]
    else:
        middle = (start+end)/2
        
        #values for crossover
        leftLow, leftHigh, leftSum = divideAndConquer(array, start, middle)
        rightLow, rightHigh, rightSum = divideAndConquer(array, middle+1, end)
        Low, High, Sum = divideCrossover(array, start, middle, end)
        
        #return array indices and sum of solution
        if leftSum >= rightSum and leftSum >= Sum:
            resultArray = [leftLow, leftHigh, leftSum]
            return resultArray
        
        elif rightSum >= leftSum and rightSum >= Sum:
            resultArray = [rightLow, rightHigh, rightSum]
            return resultArray
        
        else:
            resultArray = [Low, High, Sum]
            return resultArray
        
#LINEAR ALGORITHM
# O(n) complexity
def linear(array):
    
    currentStart = 0
    currentStop = 0
    currentSum = 0
    maxStart = 0
    maxStop = 0
    Sum = 0
    
    for x in range(0, len(array)):
        if (array[x] > currentSum + array[x]):
            currentSum = array[x]
            currentStart = x
            currentStop = x
        else:
            currentSum = currentSum + array[x]
            currentStop = x
            
        if(currentSum > Sum):
            Sum = currentSum
            maxStart = currentStart
            maxStop = currentStop
            
    return Sum

#MAIN FUNCTION
def main():
    
    #will increment in loop to number arrays for readability
    count = 1
    
    # file variables
    problemsFile = "MSS_Problems.txt"
    # results file to be created
    resultsFile = "MSS_Results.txt"
    
    # check if MSS_Problems.txt exits, if not - program will exit
    fileCheck = os.path.isfile(problemsFile)
    if (fileCheck == False):
        print ("ERROR: No such file named " + problemsFile + " found.")
        return 1
    
    # output to verify file is found (can be deleted)
    print("File successfully found!")
    
    # to create the results file
    with open(resultsFile, 'wt') as resultTemp:
        
        # then to open the problems file
        with open(problemsFile, 'rt') as temp:
            fStream = csv.reader(temp)
            # to read in row by row
            for row in fStream:
                    
                if (len(row) > 0):
                    
                    # make row into list to hold integers
                    row[0] = row[0].replace('[', '')
                    row[len(row) - 1] = row[len(row) - 1].replace(']', '')
                    row = list(map(int, row))
                    
                    # separation for readability 
                    print("Array #" + str(count))
                    count += 1
                    
                    # prints out contents of array (this can be deleted) just made it easier to visualize
                    print(row)
                    
                    #ENUMERATION RESULT
                    result = enumeration(row)
                    print("Enumeration Result: " + str(result))
                    
                    #write original array to file
                    resultTemp.write("Array: " + str(row))
                    
                    # write enumeration result to file
                    resultTemp.write("\nEnumeration Sum: " + str(result))
                
                    #BETTER ENUMERATION RESULTS
                    result = betterEnumeration(row)
                    print("Better Enumeration Result: " + str(result))
                    
                    # write better enumeration result to file
                    resultTemp.write("\nBetter Enumeration Sum: " + str(result))
                    
                    #DIVIDE AND CONQUER RESULT
                    result = divideAndConquer(row, 0, len(row)-1)
                    print("Divide and Conquer Result: " + str(result[2]))
                    
                    #write divide and conquer result to file
                    resultTemp.write("\nDivide and Conquer Sum: " + str(result[2]))
                    
                    #LINEAR RESULT
                    result = linear(row)
                    print("Linear Result: " + str(result)+ "\n")
                    
                    # write linear result to file
                    resultTemp.write("\nLinear Sum: " + str(result) + "\n\n")

# call to main function                    
main()

    