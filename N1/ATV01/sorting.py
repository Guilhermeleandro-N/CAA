import random
import time
array20000 = [random.randint(1, 10000) for _ in range(20000)]
array10000 = [random.randint(1, 10000) for _ in range(10000)]
array1000 = [random.randint(1, 10000) for _ in range(1000)]


def tempo(sorting, array):
    start = time.time()
    sorting(array)
    colapsed_time= time.time() - start
    return f"{int(colapsed_time*1000)} ms."

def selection_sort(array):
    n = len(array)
    
    for i in range(0, n):
        min_index = i

        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        
        (array[i], array[min_index]) = (array[min_index], array[i])
    
    return array

def improved_selection_sort(array):
    n = len(array)
    i = 0
    j = n - 1
    while(i < j): 
        min = array[i] 
        max = array[i] 
        min_i = i 
        max_i = i 
        for k in range(i, j + 1, 1): 
            if (array[k] > max): 
                max = array[k] 
                max_i = k 
            elif (array[k] < min): 
                min = array[k] 
                min_i = k 
          
        temp = array[i] 
        array[i] = array[min_i] 
        array[min_i] = temp 
  
    
        if (array[min_i] == max): 
            temp = array[j] 
            array[j] = array[min_i] 
            array[min_i] = temp 
        else: 
            temp = array[j] 
            array[j] = array[max_i] 
            array[max_i] = temp 
  
        i += 1
        j -= 1
    
    return array

def bubble_sort(array):
    n = len(array)
    for i in range(0, n-1):
        for j in range(n - 1 -i):
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
    return array

def improved_bubble_sort(array):
    n = len(array)
    for i in range(0, n-1):
        swapped = False
        for j in range(n - 1 -i):
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
                swapped = True
        if not swapped:
            break
    return array

def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        chave = array[i]
        j = i - 1

        while j>=0 and array[j]> chave:
            array[j+1] = array[j]
            j = j-1
        
        array[j + 1] = chave
    return array

def binary_search(arr, val, start, end):
	
	if start == end:
		if arr[start] > val:
			return start
		else:
			return start+1


	if start > end:
		return start

	mid = (start+end)//2
	if arr[mid] < val:
		return binary_search(arr, val, mid+1, end)
	elif arr[mid] > val:
		return binary_search(arr, val, start, mid-1)
	else:
		return mid

def improved_insertion_sort(arr):
	for i in range(1, len(arr)):
		val = arr[i]
		j = binary_search(arr, val, 0, i-1)
		arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
	return arr



"TESTES DE TEMPO"

#Bublle Sort
print(f"Tempo teste Bublle Sort  (Não otimizado)\n20000 elementos: {tempo(bubble_sort, array20000.copy())} \n10000 elementos: {tempo(bubble_sort, array10000.copy())}\n1000 elementos: {tempo(bubble_sort, array1000.copy())}\n")

#Improved Bubble Sort
print(f"Tempo teste Bublle Sort  (Otimizado)\n20000 elementos: {tempo(improved_bubble_sort, array20000.copy())} \n10000 elementos: {tempo(improved_bubble_sort, array10000.copy())}\n1000 elementos: {tempo(improved_bubble_sort, array1000.copy())}\n")

#SELECTION SORT
print(f"Tempo teste Selection Sort (Não otimizado)\n20000 elementos: {tempo(selection_sort, array20000.copy())} \n10000 elementos: {tempo(selection_sort, array10000.copy())}\n1000 elementos: {tempo(selection_sort, array1000.copy())}\n")

#IMPROVED SELECTION SORT
print(f"Tempo teste Selection Sort (Otimizado)\n20000 elementos: {tempo(improved_selection_sort, array20000.copy())} \n10000 elementos: {tempo(improved_selection_sort, array10000.copy())}\n1000 elementos: {tempo(improved_selection_sort, array1000.copy())}\n")

#INSERTION SORT

print(f"Tempo teste Insertion Sort (Não otimizado)\n20000 elementos: {tempo(insertion_sort, array20000.copy())} \n10000 elementos: {tempo(insertion_sort, array10000.copy())}\n1000 elementos: {tempo(insertion_sort, array1000.copy())}\n")

#IMPROVED INSERTION SORT

print(f"Tempo teste Insertion Sort (Otimizado)\n20000 elementos: {tempo(improved_insertion_sort, array20000.copy())} \n10000 elementos: {tempo(improved_insertion_sort, array10000.copy())}\n1000 elementos: {tempo(improved_insertion_sort, array1000.copy())}\n")


