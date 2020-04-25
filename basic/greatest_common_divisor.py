# 최대공약수
def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

# 유클리드를 이용한 최대공약수
def gcd_euclid(a, b):
    if b == 0:
        return a
    return gcd_euclid(b, a % b)
