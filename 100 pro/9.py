# ข้อ 1: ดึงตัวอักษร 'gram' จาก "programming"
def slice_text1(text: str) -> str:
    return text[3:7]

# ข้อ 2: ดึง [15, 20, 25] จาก list
def slice_list1(numbers: list) -> list:
    return numbers[2:5]

# ข้อ 3: ดึงตัวอักษร 3 ตัวสุดท้าย
def last_three_chars(text: str) -> str:
    return text[-3:]

# ข้อ 4: ดึงเลขคู่ index คี่ [4, 8, 12, 16]
def even_index_odd_positions(numbers: list) -> list:
    return numbers[1::2]

# ข้อ 5: กลับด้านข้อความ
def reverse_text(text: str) -> str:
    return text[::-1]

# ตัวอย่างเรียกใช้ (คุณสามารถแก้ slicing เอง)
print(slice_text1("programming"))
print(slice_list1([5, 10, 15, 20, 25, 30]))
print(last_three_chars("development"))
print(even_index_odd_positions([2,4,6,8,10,12,14,16]))
print(reverse_text("slicing"))
