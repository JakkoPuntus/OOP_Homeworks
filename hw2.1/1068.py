N = int(input()) 

n = abs(N)+2 if N <=0 else N #количество членов прогрессии
#если N меньше или равно нулю, прогрессия имеет вид 1 0 -1 -2...N и число членов прогрессии равно модулю N и плюс два члена 1 и 0

S = int((N + 1)/2 * n)

print(S)