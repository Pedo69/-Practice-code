numbers = []

n = int(input('จำนวนตัวเลขที่ต้องการป้อน: '))
for i in range(n):
    num = int(input(f'ตัวเลขที่ {i + 1}: '))
    numbers.append(num)

print('ค่าน้อยที่สุดคือ:', min(numbers))
print('ค่ามากที่สุดคือ:', max(numbers))
