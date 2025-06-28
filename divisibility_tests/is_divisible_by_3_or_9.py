# 3의 배수 판별 프로그램
# 각 자리 숫자의 합이 3의 배수인지 확인하는 함수입니다.
def is_divisible_by_3(n):
    return sum(int(ch) for ch in str(n)) % 3 == 0


# 9의 배수 판별 프로그램
# 각 자리 숫자의 합이 9의 배수인지 확인하는 함수입니다.
def is_divisible_by_9(n):
    return sum(int(ch) for ch in str(n)) % 9 == 0


assert is_divisible_by_3(123) == True
assert is_divisible_by_3(257) == False
assert is_divisible_by_3(321) == True

assert is_divisible_by_9(405) == True
assert is_divisible_by_9(256) == False
assert is_divisible_by_9(297) == True


if __name__ == "__main__":
    print("Test complete")
