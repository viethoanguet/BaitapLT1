import math
def fatorial(n):
    if n==0 : return 1
    return n * fatorial(n-1)
def prob(n p,r):
    ssumprob = fatorial(n) / (fatorial(n - r + 1) * fatorial(r - 1) * math.pow(2, n))
    return ssumprob
def infoMeasure(n, p, r):
    tong = prob(n,p,r)
    suminfo = - (math.log10(tong) / math.log10(2))
    return suminfo
def sumProb(N, p, r):
    sum = 0
    for i in range(1,N+1):
        sum += prob(i, p, r)
    return sum
def approxEntropy(N, p, r):
    sum = 0
    for i in range(1, N+1):
        sum += prob(i, p, r) * (math.log10(prob(i, p, r))/ math.log10(2))
    return -sum
n = float(input())
p =float(input())
N =float(input())
r =float(input())
print(prob(n, p, r))
#print(infoMeasure(n, p, r))
#print(sumProb(N, p, r))
#print(approxEntropy(N, p, r))
