def EEA(r1, r2, u1, u2, v1, v2) :
    if r2 == 0:
        print(f'gcd: {r1}\nx: {u1}\ny: {v1}')
        return
    q = r1//r2
    r = r1%r2
    u = u1 - q*u2
    v = v1 - q*v2

    return EEA(r2, r, u2, u, v2, v)


def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod  # 모듈로 mod의 base를 먼저 계산합니다.
    while exp > 0:
        if exp % 2 == 1:  # 현재 지수의 최하위 비트가 1이면 결과에 base를 곱합니다.
            result = (result * base) % mod
        exp = exp >> 1  # 지수를 오른쪽으로 한 비트 시프트합니다.
        base = (base * base) % mod  # base를 제곱합니다.
    return result



def euler_phi(n):
    result = 1  # 1은 모든 n과 서로소
    for i in range(2, n):
        if gcd(n, i) == 1:
            result += 1
    return result

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modular_exponentiation(a, k, n):
    phi_n = euler_phi(n)
    # 오일러의 정리에 따라, a^(k % phi(n))을 계산
    exponent = k % phi_n
    result = 1
    base = a % n

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % n
        base = (base * base) % n
        exponent //= 2

    return result