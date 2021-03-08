def solution(n, m):
    if n > m:
        n, m = m, n
    gcd = n
    for i in range(m, 0, -1):
        if not n % i and not m % i:
            gcd = i
            break
    lcm = (m * n) // gcd

    return [gcd, lcm]

print(solution(3, 12))
print(solution(2, 5))

