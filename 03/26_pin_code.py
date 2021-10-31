correct_code = '0805'
unlocked = False

for i in range(3):
    code = input('Enter the PIN code: ')
    if code == correct_code:
        unlocked = True
        break
    elif i != 2:
        print("Incorrect...")

if not unlocked:
    print("Sorry, your payment card has been blocked.")
else:
    print("Cart unlocked")
