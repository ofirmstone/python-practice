# contraints:
#   1 <= n <= 1000001
#   n is odd
#   -10000 <= arr[i] <= 10000

def findMedian(arr):
 sortedArr = sorted(arr)
 return(sortedArr[len(arr) // 2])
