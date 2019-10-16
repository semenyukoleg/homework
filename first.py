from random import randrange
import time
from datetime import datetime

# Python program for implementation of MergeSort 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]   
        R = arr[mid:] 
  
        mergeSort(L) 
        mergeSort(R) 
  
        i = j = k = 0
          

        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

def partition(arr,low,high): 
    i = ( low-1 )        
    pivot = arr[high]     
  
    for j in range(low , high): 
  
        if   arr[j] < pivot: 
           
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 


# Python program for implementation of Quicksort Sort 

def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

# Python program for implementation of heap Sort 
  
def heapify(arr, n, i): 
    largest = i 
    l = 2 * i + 1     
    r = 2 * i + 2     
  
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
   
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  
   
        heapify(arr, n, largest) 
   
def heapSort(arr): 
    n = len(arr) 
  
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0) 

f = open(r"C:\Users\igor\source\repos\PythonApplication2\PythonApplication2\ai182.txt", "r")
f.seek(248)
s = f.read(15)
task_array = [int (s[i]) for i in range (0, 15)]

from datetime import datetime
#Merge sort
#Average duration: 0:00:00.001095
arr = task_array
start_time = datetime.now()
merge_sort(arr)
end_time = datetime.now()
print("Merge sort: " + str(arr) + "\n" + 'Duration: {}'.format(end_time - start_time) + "\n")

#Quick sort
#Average duration: 0:00:00.001095
arr = task_array
start_time = datetime.now()
quick_sort(arr, 0, len(arr) - 1)
end_time = datetime.now()
print("Quick sort: " + str(arr) + "\n" + 'Duration: {}'.format(end_time - start_time) + "\n")

#Heap sort
#Average duration: 0:00:00.000750
arr = task_array
start_time = datetime.now()
heap_sort(arr)
end_time = datetime.now()
print("Heap sort: " + str(arr) + "\n" + 'Duration: {}'.format(end_time - start_time) + "\n") 

# Conclusion: all three sorts are pretty fast, compering them to n^2 sorts algorithms, heap gave the best result

