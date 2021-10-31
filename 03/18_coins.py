init_amount = int(input('Enter the amount in PLN: '))
amount = init_amount

fives = amount // 5
amount //= 5

twoes = amount // 2
amount //= 2

ones = amount

print(
    f"The amount of PLN {init_amount} in coins: \n 5 zł - {fives} \n 2 zł - {twoes} \n 1 zł - {ones}")
