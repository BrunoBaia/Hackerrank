"""Decorators 2 - Name Directory

https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=false

Input Format

The first line contains the integer n, the number of people.
n lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

Output Format

Output n names on separate lines in the format described above in ascending order of age."""


def person_lister(f):
    def inner(peop):
        people3 = sorted(peop, key=lambda x: int(x[2]))
        return list(map(f, people3))
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
