data = {'age':[15, 22, 30,24,20],\
        'weight':[30,45,57,60,40]}

for key, value in data.items():
    for v in value:
        print(f'{v}, ',end='')
    print()
print(f'อายุต่ำสุด คือ {min(data['age'])}')
print(f'น้ำหนักต่ำสุด คือ {min(data['weight'])}')

ageAvg = sum(data['age'])/len(data['age'])
weightAvg = sum(data['weight'])/len(data['weight'])

for value in data['age']:
    if value > ageAvg:
        print(f'อายุ {value} มากกว่า {ageAvg}')

for value in data['weight']:
    if value > weightAvg:
        print(f'น้ำหนัก {value} มากกว่า {weightAvg}')