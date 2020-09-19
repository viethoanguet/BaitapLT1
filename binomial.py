import math
def factoril(n):
    if n==0: return 1
    return n*factoril(n-1)
def prob(n,p,N):
    ssumprob=(factoril(N) / (factoril(n)*factoril(N-n) ))*math.pow(p,n)*math.pow(1-p,N-n)
    return ssumprob
def infoMeasure(n,p,N):
    tong=prob(n,p,N)
    suminfo=-(math.log10(tong)/math.log10(2))
    return suminfo
def sumprob(N,p):
    tong2=0
    for i in range(1,N+1):
        tong2+=prob(i,p,N)
    return tong2
n=float(input())
p=float(input())
N=float(input())
print(prob(n,p,N))
#print(infoMeasure(n,p,N))
#print(sumprob(N,p))
#print(appoxEntropy(N,p))
