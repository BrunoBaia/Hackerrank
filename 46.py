"""Set .discard(), .remove() & .pop()

https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=false

Task
You have a non-empty set s, and you have to execute n commands given in n lines.
The commands will be pop, remove and discard."""


n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    command = input().split()
    if command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
    else:
        s.pop()
print(sum(s))
