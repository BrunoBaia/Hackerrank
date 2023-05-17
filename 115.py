"""collections.Counter()

https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=false

Task

R is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay x amount of money only if they get the shoe of their desired size
Your task is to compute how much money R earned."""


from collections import Counter

x = input()
shoe_size = Counter(input().split())
money = 0
for _ in range(int(input())):
    size, price = input().split()
    if shoe_size.get(size):
        shoe_size[size] -= 1
        money += int(price)
print(money)
