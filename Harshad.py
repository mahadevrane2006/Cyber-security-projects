# Harshad (Niven) Number Check
def is_harshad(num):
    digit_sum = sum(int(d) for d in str(num))
    return num % digit_sum == 0

# Example usage
number = int(input("Enter a number: "))
if is_harshad(number):
    print(f"{number} is a Harshad Number.")
else:
    print(f"{number} is NOT a Harshad Number.")
