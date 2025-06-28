# 2의 배수 판별 프로그램
# 일의 자리 숫자가 짝수인지 확인하여 2의 배수인지 판별하는 프로그램입니다.
def is_divisible_by_2(n) -> bool:
    one_digit = n % 10
    return is_even(one_digit)


# 짝수 판별 프로그램
# 숫자가 짝수인지 확인하는 함수입니다.
def is_even(n) -> bool:
    return n % 2 == 0


assert is_divisible_by_2(0) == True
assert is_divisible_by_2(1) == False
assert is_divisible_by_2(2) == True

if __name__ == "__main__":
    print("Test complete")
