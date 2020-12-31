#Bubble Sort
def bubbleSort(array):
    for i in range (1, len(array)):
        sorted = True
        for j in range(len(array)-i):
         if (array[j]) < (array[j+1]):
          array[j], array[j+1] = array[j+1], array[j]
          sorted = False
        if sorted:
         break
    return(array)

#Selection Sort
def selectionSort(array):
    length = len(array)
    for i in range (length-1):
        lowVal = i
        for j in range (i+1, length):
            if array[j] < array[lowVal]:
                lowVal = j
        array[lowVal], array[i] = array[i], array[lowVal]
    return(array)

#Insertion Sort
def insertionSort(list):
    length = len(list)
    for i in range(length-1):
        lowVal = i
        for j in range(i+1,length):
            if list[lowVal] > list[j]:
                lowVal = j
        list.insert(i,list[lowVal])
        list.pop(lowVal+1)
    return (list)

#Indirect Array
def indirectSort(array):
    sortArray = [i for i in range (len(array))]
    for i in range (1, len(array)):
        sorted = True
        for j in range(len(array)-i):
         if (array[sortArray[j]]) > (array[sortArray[j+1]]):
          sortArray[j], sortArray[j+1] = sortArray[j+1], sortArray[j]
          sorted = False
        if sorted:
         break
    return(array, sortArray)

#Binary Search
def binarySearch(array, number):
    bottom = 0
    top = len(array) - 1
    middle = (top + bottom)//2
    while ((bottom != top) and (array[middle] != number)):
        if array[middle] < number:
            bottom = middle + 1
        if array[middle] > number:
            top = middle - 1
        middle = (top + bottom)//2
    if array[middle] == number:
        return ( middle)
    else:
        return (-1)

#Merge sort
def mergeSort(array):
    if len(array) >1:
        middle = len(array)//2
        leftSide = array[:middle]
        rightSide = array[middle:]
        mergeSort(leftSide)
        mergeSort(rightSide)
        i = j = k = 0
        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] < rightSide[j]:
                array[k] = leftSide[i]
                i+=1
            else:
                array[k] = rightSide[j]
                j+=1
            k+=1
        while i < len(leftSide):
            array[k] = leftSide[i]
            i+=1
            k+=1
        while j < len(rightSide):
            array[k] = rightSide[j]
            j+=1
            k+=1

array = [3,5,4,8,9,1,0]
mergeSort(array)
print(array)

#Quick sort
def setPivot(array,low,high):
    i = ( low-1 )
    pivot = array[high]
    for j in range(low , high):
        if array[j] < pivot:
            i = i+1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = array[high],array[i+1]
    return ( i+1 )

def quickSort(array,low,high):
    if low < high:
        pivot = setPivot(array,low,high)
        quickSort(array, low, pivot-1)
        quickSort(array, pivot+1, high)

array = [3,5,4,8,9,1,0]
length = len(array)
quickSort(array,0,length-1)
print (array)
