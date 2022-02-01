import sys
import re

def containsAll(word,letters):
    for letter in letters:
        if letter not in word:
            return False;
    return True;

def containsNone(word,letters):
    for letter in letters:
        if letter in word:
            return False;
    return True;  

def matchesPattern(word,patt):
    re_patt = "^"+patt.replace('-','.')+"$"
    res = re.search(re_patt,word)
    if res:
        return True
    return False


words = sys.argv[1];
pattern = sys.argv[2];
# exact letters pattern in the format
# a-v-a
others = sys.argv[3].split(',');
# misplaced letters
# b,c,d
excl = sys.argv[4].split(",");
# wrong letters
# h,j,k

with open(words) as file:
    lines = file.readlines()

print("Word pattern: ",pattern)
print("Misplaced letters: ", others)
print("Wrong letters: ",excl)

goods = [word for word in lines if containsAll(word,others) and containsNone(word,excl) and matchesPattern(word,pattern)]

print(goods)