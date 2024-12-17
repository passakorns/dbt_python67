import random
print(*range(10))

for x in range(10):
    print(f'X=> {x}')

for x in range(150, 15, -6):
    print(f'X==> {x}')

# ใช้ for-in สร้างการวนซ้ำ 9 รอบ
# สุ่มตัวเลข 1-6 และแสดงผล
# คำนวณผลรวมตัวเลขที่ได้จากการสุ่ม และแสดงผล
# คำนวณผลรวมเลขคู่และเลขคี่ และแสดงผล
# หากพบเลข 3 ไม่เอาไปรวมผลรวม

sum = 0
sum_even = 0
sum_odd = 0
for _ in range(9):
    num_rnd = random.randint(1,6)
    print(f'Num random -> {num_rnd}')
    if num_rnd == 3:
        continue
    sum = sum + num_rnd   #sum+=rnd
    if num_rnd%2 == 0:
        sum_even+=num_rnd
    else:
        sum_odd+=num_rnd

print(f'Sum: {sum}')
print(f'Sum Even: {sum_even}')
print(f'Sum Odd: {sum_odd}')