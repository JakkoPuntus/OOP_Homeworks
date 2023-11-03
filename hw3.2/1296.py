gp_tmp = 0 #промежуточный гравитационный потенциал 
gp = 0  #максимальный гравитационный потенциал

n = int(input())

for i in range(n):
    p = int(input()) 

    gp_tmp = max(p, gp_tmp+p)
    gp = max(gp, gp_tmp)


print(gp)