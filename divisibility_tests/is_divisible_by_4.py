# 4의 배수 판별 프로그램
# 끝의 두 자리 수가 00이거나 4로 나누어 떨어지는지 확인하는 함수입니다.
def is_divisible_by_4(n):
    last_two_digits = n % 100
    return last_two_digits == 0 or last_two_digits % 4 == 0


assert is_divisible_by_4(0) == True
assert is_divisible_by_4(4) == True
assert is_divisible_by_4(100) == True
assert is_divisible_by_4(102) == False
assert is_divisible_by_4(1004) == True
assert is_divisible_by_4(1002) == False


if __name__ == "__main__":
    print("Test complete")
