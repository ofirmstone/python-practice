import os

def timeConversion(s):
    hour = int(s[:2])
    clock = s[8:]
    
    if (clock == "PM" and hour != 12):
        hour += 12
        return(f"{hour}{s[2:8]}")
    elif (clock == "AM" and hour == 12):
        hour -= 12
        
    if (clock == "PM"): # for 12pm 
        return(f"{hour}{s[2:8]}") 
    
    return(f"0{hour}{s[2:8]}")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
