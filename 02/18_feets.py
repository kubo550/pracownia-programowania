import math

height_cm = 170
one_cm_in_inches = 0.3937008
inches = height_cm * one_cm_in_inches

print(f'{math.ceil(inches // 12)} feet and {math.ceil(inches % 12)} inches')
