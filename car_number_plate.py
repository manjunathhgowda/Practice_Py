"""
You are required to write a function that validates and formats a license plate string 
according to specific rules. The license plate may contain only alphanumeric characters 
(A–Z and 0–9); any other character makes the plate invalid. After processing, the total 
length of the license plate must be between 2 and 10 characters inclusive; if it contains 
fewer than 2 or more than 10 characters, it should be considered invalid. All alphabetic 
characters must be converted to uppercase. Additionally, the license plate must contain 
at least one digit; if no digit is present, the input is invalid. If the plate satisfies 
all validation conditions, it must then be formatted into groups of 2 or 3 characters 
separated by hyphens (-). If the length of the cleaned license plate is divisible by 3, 
it should be split into groups of 3 characters each. If the length is not divisible by 3, 
create as many groups of 3 characters as possible, and the final group must contain exactly 
2 characters. For example, a plate with 9 characters such as ABC123XYZ should be formatted 
as ABC-123-XYZ; a plate with 8 characters such as ABC123XY should be formatted as ABC-123-XY; 
and a plate with 7 characters such as ABC1234 should be formatted as ABC-123-4. If the license 
plate fails any of the validation conditions, the function must return the string "INVALID".
"""
def validate(s):
    s = s.upper()

    for ch in s:
        if not ch.isalnum():
            return "Invalid"

    if len(s) <= 2 or len(s) >= 10:
        return "Invalid"

    if not any(ch.isdigit() for ch in s):
        return "Invalid"

    n = len(s)
    res = []
    
    
    rem=n%3
    
    if rem == 0:
        for i in range(0, n, 3):
            res.append(s[i:i+3])
    elif rem==1:
        stop = n - 4
        for i in range(0, stop, 3):
            res.append(s[i:i+3])
        res.append(s[stop:stop+2])
        res.append(s[stop+2:])

    else: 
        stop = n - 2
        for i in range(0, stop, 3):
            res.append(s[i:i+3])
        res.append(s[stop:])

    return "-".join(res)
p=["ABC123xyz","abc1234XY","ABC123XY",'AB',"A@123","X4T","1234xa78","ABCDE12","abcd1234xy",'abc23']
for i in p:
    res=validate(i)
    print("\n",res)