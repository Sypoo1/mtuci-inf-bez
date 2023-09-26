import math
import string
import random


P = 10 ** -4 
V = 15 # password/min
T = 2 * 7 * 24 * 60 # min

S_bottom = math.ceil(V * T / P)

alphabet = string.ascii_uppercase[:20:] # 20 первых заглавных букв английского алфавита
A = len(alphabet)
L = math.ceil(math.log(S_bottom, A))

password = [0] * A
for i in range(A):
    password[i] = random.choice(alphabet)
password = "".join(password)

print(password)

