height = float(input('Enter your height in cm: ')) / 100
weight = float(input('Enter your weight in kg: '))

bmi = weight / (height ** 2)

print(f'BMI index: {bmi}')
