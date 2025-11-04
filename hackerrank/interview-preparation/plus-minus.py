def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    
    n = len(arr)
    
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    
    print("{:.6f}".format(pos/n)) # positive ratio
    print("{:.6f}".format(neg/n)) # positive ratio
    print("{:.6f}".format(zero/n)) # positive ratio

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
