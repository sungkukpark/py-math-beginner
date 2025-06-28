# 5의 배수 판별 프로그램
# 일의 자리 숫자가 0이거나 5인 수를 5의 배수로 판별하는 프로그램입니다.
def is_divisible_by_5(n):
    last_digit = n % 10
    return last_digit == 0 or last_digit == 5


assert is_divisible_by_5(0) == True
assert is_divisible_by_5(5) == True
assert is_divisible_by_5(100) == True
assert is_divisible_by_5(102) == False
assert is_divisible_by_5(1004) == False
assert is_divisible_by_5(1002) == False


if __name__ == "__main__":
    print("Test complete")
