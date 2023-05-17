"""Words Score

https://www.hackerrank.com/challenges/words-score/problem?isFullScreen=false

Task

In this challenge, the task is to debug the existing code to successfully execute all provided test files.
Consider that vowels in the alphabet are a, e, i, o, u and y.
Function score_words takes a list of lowercase words as an argument and returns a score as follows:
The score of a single word is 2 if the word contains an even number of vowels. Otherwise, the score of this word is 1.
The score for the whole list of words is the sum of scores of all words in the list.
Debug the given function score_words such that it returns a correct score.
Your function will be tested on several cases by the locked template code."""


def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    score = sum([2 if sum([is_vowel(letter) for letter in word]) % 2 == 0 else 1 for word in words])
    return score


n = int(input())
wordss = input().split()
print(score_words(wordss))
