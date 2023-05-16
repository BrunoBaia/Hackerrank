"""Collections.OrderedDict()

https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=false

Task

You have a list of n items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence."""


from collections import OrderedDict

number_items = int(input())
mercadoria = OrderedDict()
for _ in range(number_items):
    item = input().split()
    price = int(item.pop())
    item = " ".join(item)
    if mercadoria.setdefault(item):
        mercadoria[item] += price
    else:
        mercadoria[item] = price
for item in mercadoria.items():
    print(*item)
