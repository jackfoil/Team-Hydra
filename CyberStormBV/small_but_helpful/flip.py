# Coded by Brandon for team Hydra
# DO NOT LEAK

from sys import stdin, stdout

text = stdin.read()

text = list(text)

for i in range(len(text)):
    stdout.write(text[len(text)-1 - i])