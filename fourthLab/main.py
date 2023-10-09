# A = 17
# B = 11
# C = 256
# t0 = 172
# MaxVal = 255


A = 9
B = 11
C = 256
t0 = 201
MaxVal = 255

def ksumm(summa: str):
    int_summa = 0
    for item in summa:
        int_summa += ord(item)
    if int_summa <= MaxVal:
        return int_summa
    else:
        return int_summa % (MaxVal+1)


def SummKodBukvOtkr(summa: str):
    t_list = [0] * len(summa)
    x_list = []
    t_list[0] = t0
    for item in summa:
        x_list.append(int(item))

    for i in range(1, len(t_list)):
        t_list[i] = (A * t_list[i-1] + B) % C

    y_list = ""
    for i in range(0, len(t_list)):
        y_list += str(x_list[i] | t_list[i])

    return ksumm(y_list)

# examples = ["0123456789", "9876543210", "1000005", "1500000"]

examples = ["021345"]
for example in examples:
    
    print(f"P = {example}, Ksumm = {ksumm(example)}, SummKodBukvOtkr = {SummKodBukvOtkr(example)}")


