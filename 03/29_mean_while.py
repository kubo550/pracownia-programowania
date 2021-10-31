numbers = []
can_add = True

while can_add:
    num = float(input("Enter number: "))
    if num == 0:
        can_add = False
    else:
        numbers.append(num)

_sum = sum(numbers)
_len = len(numbers)
_mean = sum(numbers) / len(numbers)
print(f"RESULT: Quantity={_len}, Sum={_sum}, Mean={_mean}")
