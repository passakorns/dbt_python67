#การสร้างลิสต์
nums =[5, 7, 10, 4, 6, 12]

lst1 = list()

lst2 = ['a', 'e', 'i', 'o', 'u']

lst3 = [4, 5.5, 0, 'apple']

print('nums:', nums,'\nlst1:', lst1, '\nlst2', lst2, '\nlst3', lst3)

#การเข้าถึงสมาชิกในลิสต์
sum = nums[2] + nums[4]
print(sum)

#เข้าถึงสมาชิกของ lst2 ทุกตัว และแสดงผลเป็นตัวพิมพ์ใหญ่
for x in lst2:
    print(x.upper())

#การเพิ่มข้อมูลเก็บในลิสต์
lst1.append(5)
print(lst1)
lst1.append(10)
print(lst1)
lst1.insert(1, 9)
print(lst1)
lst1.insert(2,14)
print(lst1)
mylst = lst1+lst3
print(mylst)
mylst.pop(7) #ลบสมาชิกในลิสต์ตำแหน่งอินเด็กซที่ 7
print(mylst)
mylst.remove(5.5) #ลบสมาชิกในลิสต์ที่มีค่าข้อมูลที่ต้องการลบ
print(mylst)