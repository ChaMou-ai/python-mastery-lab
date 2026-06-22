import sys

sentence = " ".join(sys.argv[1:])

words = sentence.split()

print("words",len(words))