A = 17
B = 11
C = 256
t0 = 172
MaxVal = 255


def ksumm(string: str):
    summa = 0
    for item in string:
        summa += ord(item)
    if summa <= MaxVal:
        return summa
    else:
        return summa % (MaxVal+1)


def str_to_bin(item: str):
    item = bin(ord(item))[2::]
    item = "0" * (8 - len(item)) + item

    return item

def logic_xor(x, t):
    y = ""
    for i in range(8):
        y += str(int(x[i] != t[i]))
    return y

def gamma(string: str):
    x_list = [str_to_bin(item) for item in string]

    p = len(string)
    t_list = [t0]
    for i in range(1, p):
        t_list.append((A * t_list[i-1] + B) % C)

    for i in range(0, p):
        t = bin(t_list[i])[2::]
        t_list[i] = "0" * (8 - len(t)) + t

    y_list = [int(logic_xor(x_list[i], t_list[i]), base=2) for i in range(0, p)]
    summa = sum(y_list)
    if summa <= MaxVal:
        return summa
    else:
        return summa % (MaxVal+1)


examples = ["0123456789", "9876543210", "1000005", "1500000"]

for example in examples:
    print(f"P = {example}, Ksumm = {ksumm(example)}, SummKodBukvOtkr = {gamma(example)}")



