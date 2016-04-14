import random


#Function takes an array and the size of the array and fills it
#with random numbers from -100 to 100

def fillArray( myArray, arraySize):
    for i in range(0 , arraySize):
        myArray.append(random.randrange(-100, 100))

#Creating ten arrays of size 100
        
array0, array1, array2, array3, array4, array5, array6, array7,\
        array8, array9 =([], [], [], [], [], [], [], [], [], [])

fillArray(array0, 100)
fillArray(array1, 100)
fillArray(array2, 100)
fillArray(array3, 100)
fillArray(array4, 100)
fillArray(array5, 100)
fillArray(array6, 100)
fillArray(array7, 100)
fillArray(array8, 100)
fillArray(array9, 100)


