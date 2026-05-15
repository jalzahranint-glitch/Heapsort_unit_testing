
#This function arranges the input array
# from smallest to largest using the Heapsort algorithm
def heapsort(arr):
    myarr= list(arr)  #create copy of th input array 
    def heapify(n, i):
        largest = i
        left = 2*i + 1
        right= 2*i + 2
        if left < n and myarr[left] > myarr[largest]:
            largest = left
        if right < n and myarr[right] > myarr[largest]:
            largest = right
        if largest != i:
            myarr[i], myarr[largest] = myarr[largest], myarr[i]
            heapify(n, largest)
    n = len(myarr)
    i = n // 2 - 1
    while i >= 0:
        heapify(n, i)
        i -= 1
    # Extract the large  elements one by one using while
    i = n - 1
    while i > 0:
        myarr[0], myarr[i] = myarr[i], myarr[0]
        heapify(i, 0)
        i -= 1
    return myarr  #return array after sorting 

    