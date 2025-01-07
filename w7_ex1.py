#ฝึกปฏิบัติ
#ข้อ 1
nums = list([23,16,27,32,19])
print(*nums)
for i,n in enumerate(nums):
    print(f'nums[{i}] = {n}')

#ข้อ 2
import random

lstNum = list()
for _ in range(20):
    lstNum.append(random.randint(51,99))
print(lstNum)
#ข้อ 3
lstEven = list()    #เลขคู่
lstOdd = list()     #เลขคี่

for num in lstNum:
    if num%2 == 0:
        lstEven.append(num)
    else:
        lstOdd.append(num)
print(lstEven, lstOdd, sep='\n')

#ข้อ 4

for index, num in enumerate(lstNum):
    if num%7 == 0:
        lstNum.pop(index)
        print(num,end=' ')
print(lstNum)

#ข้อ 5
print(f'สมาชิกของ lstNum มีค่ามากที่สุด คือ {max(lstNum)}')
print(f'สมาชิกของ lstNum มีค่าน้อยที่สุด คือ {min(lstNum)}')
print(f'สมาชิกของ lstNum มีผลรวม คือ {sum(lstNum):.2f}')
print(f'สมาชิกของ lstNum มีผลรวมเฉลี่ย คือ {sum(lstNum)/len(lstNum):.2f}')

#ข้อ 6
lstNew = list()
for _ in range(5):
    lstNew.append(random.randint(71,89))

print(lstNew)
lstNum.extend(lstNew)
print(lstNum)

#ข้อ 7

if 80 in lstNum:
    print(f'80 อยู่ตำแหน่ง {lstNum.index(80)}')
else:
    print('ไม่พบ 80 ใน lstNum')
if 84 in lstNum:
    print(f'84 อยู่ตำแหน่ง {lstNum.index(84)}')
else:
    print('ไม่พบ 84 ใน lstNum')