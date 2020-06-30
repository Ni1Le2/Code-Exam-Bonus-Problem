from boyer_moore_alg import find_boyer_moore
from brute_force_alg import find_brute
from knuth_morris_pratt_alg import find_kmp

import time

import os

spath1 = "C:\\Nico\Studium\Vorlesungen 2. Semester\Algorithmen und Datenstrukturen\Exam Bonus Problem\Code\Sample texts\Bible.txt"
spath2 = "C:\\Nico\Studium\Vorlesungen 2. Semester\Algorithmen und Datenstrukturen\Exam Bonus Problem\Code\Sample texts\\aaa.txt"

if os.path.exists(spath1):
    with open(spath1) as textfile:
        text1 = (textfile.read())

if os.path.exists(spath2):
    with open(spath2) as textfile:
        text2 = (textfile.read())*40    #letter 'a' 100.000 *40 times = 4.000.000

# T = text, P = pattern
pattern1 = "Omega"
pattern2 = "   "
pattern3 = "He which testifieth these things saith, Surely I come quickly. Amen. Even so, come, Lord Jesus."
pattern4 = "abcdefghijklmnopqrstuvwxyz"

pattern5 = "aaaaaaaaaaaaaab"
pattern6 = "baaaaaaaaaaaaa"
pattern7 = "He which testifieth these things saith, Surely I come quickly. Amen. Even so, come, Lord Jesus.a"


timeTotal = 0
countVar = 20
start_time = time.time()
for i in range(countVar):
    find_brute(text1, pattern1)
    #find_boyer_moore(text1, pattern1)
    #find_kmp(text1, pattern1)

time = (time.time() - start_time)
averageTime = time/countVar
print("total time: %s seconds" % time)
print("average out of 20: %s seconds" % averageTime)

