number = int(input("숫자를 입력하세요: "))
n = int(input("변환할 진수를 입력하세요: "))

answer = ""

while number // n >= 1:
    remain = number % n
    number = number // n
    answer = str(remain) + answer
    if number < n:
        answer = str(number) + answer

print("변환 값: %s(%s)" % (answer, n))

