import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase

symbols = ("!", "”", "#", "$", "%", "&", "’", "(", ")", "*")

identificator = input("Введите идентификатор: ")
N = len(identificator)

password = [0] * 6
password[0] = random.choice(upper)
password[1] = random.choice(upper)
password[2] = (N * N) % 10
password[3] = random.randint(0,9)
password[4] = random.choice(symbols)
password[5] = random.choice(lower)

password = "".join(list(map(str, password)))

print(password)