""" Question

You are at the chemistry lab performing the Iodine Clock Experiment. 
You have been given a stop watch in which the time is in hh:mm:ss format;
the hour is represented in 24-hour format. 
The clock starts at 00:00:00 and ends at 23:59:59. 
However at times, the display of the stop watch is incorrect that one of the 
characters of the time at any point of time remains blank. 
That is, assume that the actual time that has elapsed be 10:25:48 
but on the stop watch this might be displayed 10: 5:48. Here, 
the number 2 in the minutes is not getting displayed properly. 
And, the possible values that can be placed in this position are 0, 1, 2, 3, 4 and 5. 
Placing these values in the input, we find the minimum possible time would be 10:05:48 
and the maximum possible time would be 10:55:48.

Your task is to find out the possible values that the blank may take, 
and also display the maximum and minimum values."""

#represented empty space as @

def clock(s):
    min=""
    max=""
    pos_val=[]
    if s[0]=='@':
        min='0'+s[1:]
        max='2'+s[1:]
        pos_val=[i for i in range(3)]
        return min,max,pos_val 
    elif s[1]=="@":
        if s[0]=='0' or s[0]=='1':
            min=s[0]+'0'+s[2:]
            max=s[0]+'9'+s[2:]
            pos_val=[i for i in range(10)]
        else:
            min=s[0]+'0'+s[2:]
            max=s[0]+'3'+s[2:]
            pos_val=[i for i in range(4)]
    elif s[3]=="@":
            min=s[:3]+'0'+s[4:]
            max=s[:3]+'5'+s[4:]
            pos_val=[i for i in range(6)]
    elif s[4]=="@":
            min=s[:4]+'0'+s[5:]
            max=s[:4]+'9'+s[5:]
            pos_val=[i for i in range(10)]
    elif s[6]=="@":
            min=s[:6]+'0'+s[7:]
            max=s[:6]+'5'+s[7:]
            pos_val=[i for i in range(6)]
    elif s[7]=="@":
            min=s[:7]+'0'
            max=s[:7]+'9'
            pos_val=[i for i in range(10)]
    return min,max,pos_val  

s=["@2:23:34","0@:23:34","1@:23:34","2@:23:34","14:@3:34","14:2@:34","18:23:@4","23:23:3@"]
for i in s:
    print(i)
    res=clock(i)
    print(f"Min:{res[0]}\nMax:{res[1]}\nPossible values:{res[2]}\n")


