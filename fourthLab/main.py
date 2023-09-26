A = 17
B = 11 
C = 256
t0 = 172
MaxVal = 255

def KSumm(summa: str):
    int_summa = 0
    for item in summa:
        int_summa += int(item)
    if int_summa <= MaxVal:
        return int_summa
    else:
        return int_summa % (MaxVal+1)

def make(summa: str):
    int_summa = 0
    t_list = [0] * len(summa)
    x_list = []
    t_list[0] = t0
    for item in summa:
        x_list.append(int(item))

    for i in range(1, len(t_list)):
        t_list[i] = (A * t_list[i-1] + B) % C
     
    Y_list = []
    for index, item in enumerate(t_list):
        Y = x_list[index] | t_list[index]
    return  KSumm("".join(Y_list))

print(KSumm("0123456789"), make("0123456789"))
print(KSumm("9876543210"), make("9876543210"))
print(KSumm("1000005"), make("1000005"))
print(KSumm("1500000"), make("1500000"))
print(make("23"))