#reverse a string#
def reverse_string(text):
    return text[::-1]
text="hello world"
reverse_text=reverse_string(text)
print(reverse_text)

#reverse a string without function#
string="hello"
reversed_string=''.join(reversed(string))
print(reversed_string)

#maximum element of number#
a = 12
b = 34
c = 13

if a >= b and a >= c:
    max = a
elif b >= a and b >= c:
    max = b
else:
    max = c
print(max)


def OperationsBinaryString(str):
    ans= ord(str[0]-ord('0'))
    for i in range(1,len(str),2):
        j=i+1;
        if(str[i]=='A'):
            ans = ans & (ord(str[j])-ord('0'))
        elif(str[i]=='B'):
            ans = ans | (ord(str[j])-ord('0'))
        elif(str[i]=='C'):
            ans = ans ^ (ord(str[j]) - ord('0'))
        return ans



