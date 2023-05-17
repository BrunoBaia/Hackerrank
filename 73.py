"""ginortS

https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=false

Task

You are given a string s,s contains alphanumeric characters only.
Your task is to sort the string s in the following manner:
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits."""


string = input()
lower = []
upper = []
odd = []
even = []
for s in string:
    if s.islower():
        lower.append(s)
    elif s.isupper():
        upper.append(s)
    else:
        if int(s) % 2 == 1:
            odd.append(s)
        else:
            even.append(s)
lower.sort()
upper.sort()
odd.sort()
even.sort()
new_string = "".join(lower)+"".join(upper)+"".join(odd)+"".join(even)
print(new_string)
