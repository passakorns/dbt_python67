score_dict = {102:89, 113:90, \
              115:90, 120:80, \
                125:85}

user_id = int(input('เลขที่สอบคุณคือ: '))

if user_id in score_dict.keys():
    print(f'คุณ "สอบผ่าน" {score_dict[user_id]} คะแนน')
else:
    print('พบกันใหม่รอบหน้า')
