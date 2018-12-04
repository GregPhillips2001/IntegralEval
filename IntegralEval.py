from math import*

f = input('Enter the function: ')
a = float(input('Enter the left endpoint: '))
b = float(input('Enter the right endpoint: '))
n = int(input('Enter the number of subintervals: '))

LRAM = 0.0
RRAM = 0.0
MRAM = 0.0

x = a
h = (b - a)/n
for i in range (n):
    x1 = x
    f1 = eval(f)
    LRAM = LRAM + f1*h
    x = x + h
    x2 = x
    f2 = eval(f)
    RRAM = RRAM + f2*h
    x = (x1 + x2)/2
    fm = eval(f)
    MRAM = MRAM + fm*h
    x = x2

print('LRAM = ' ,LRAM)
print('MRAM = ' ,MRAM)
print('RRAM = ' ,RRAM)

T = (LRAM+RRAM)/2
print("Trapezoidal Rule = ", T)
print("Simposon's Rule =", (T+2*MRAM)/3)

