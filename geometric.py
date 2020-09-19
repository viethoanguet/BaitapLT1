import math
def prob(n, p):
    ssumprob = 1 / (p**n)
    return ssumprob
def infoMeasure(n, p):
        temp = sumprob(n, p)
        suminfoMeasure = - (math.log10(temp) / math.log10(2))
        return suminfoMeasure
def sumProb(N, p):
    sum = 0
    for i in range(1, N+1):
        sum += prob(i, p)
    return sum
#vì geometric liên quan tới số lượt thử cho 1 lần thành công duy nhất
def approxEntropy(N, p):
    sum = 0
    for i in range(1, N+1):
        sum += i / (p**i)
    return sum
n = int(input())
p = int(input())
N = int(input())
print(prob(n, p))
#print(infoMeasure(n, p))
#print(sumProb(N, p))
#print(approxEntropy(N, p))
