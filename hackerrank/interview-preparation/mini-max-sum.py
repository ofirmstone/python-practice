def miniMaxSum(arr):
    minNum = min(arr)
    maxNum = max(arr)
    total = sum(arr)
    
    minVal = total - maxNum
    maxVal = total - minNum
    
    print(f"{minVal} {maxVal}")
    
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
