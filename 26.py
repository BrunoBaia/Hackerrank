"""The Minion Game

https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=false

Game Rules

Both players are given the same string, s.
Both players have to make substrings using the letters of the string s.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings."""


def minion_game(string):
    stuart = 0
    kevin = 0
    for ind, let in enumerate(string):
        if let not in "AEIOU":
            stuart += len(s[ind::])
        else:
            kevin += len(s[ind::])
    if stuart > kevin:
        print(f'Stuart {stuart}')
    elif stuart < kevin:
        print(f'Kevin {kevin}')
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
