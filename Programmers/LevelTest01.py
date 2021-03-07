def solution(n, m):
    if n > m:
        n, m = m, n
    gcd = n
    for i in range(m, -1, -1):
        if not m % i and not n % i:
            gcd = i
            break
    lcm = (n*m) // gcd
    return [gcd, lcm]

print(solution(3, 12))
print(solution(2, 5))

