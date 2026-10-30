class Solution:
    def threeWayPartition(self, array, a, b):
        low = 0
        mid = 0
        high = len(array) - 1
        
        while mid <= high:
            if array[mid] < a:
                array[low], array[mid] = array[mid], array[low]
                low += 1
                mid += 1
            elif array[mid] > b:
                array[mid], array[high] = array[high], array[mid]
                high -= 1
            else:
                mid += 1
        
        return array