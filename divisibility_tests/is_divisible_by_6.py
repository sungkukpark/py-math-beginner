# 6의 배수 판별 프로그램
# 주어진 숫자가 짝수이고 각 자리 숫자의 합이 3의 배수인지 확인하여 6의 배수인지 판별하는 프로그램입니다
def is_divisible_by_6(n):
    sum_of_digits = sum(int(ch) for ch in str(n))
    return sum_of_digits % 3 == 0 and n % 2 == 0


# 0은 모든 정수의 배수이므로 6의 배수로 판별합니다.
assert is_divisible_by_6(0) == True
assert is_divisible_by_6(6) == True
assert is_divisible_by_6(12) == True
assert is_divisible_by_6(30) == True
assert is_divisible_by_6(132) == True
assert is_divisible_by_6(134) == False


if __name__ == "__main__":
    print("Test complete")
