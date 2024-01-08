import re
import pandas as pd

# อ่านข้อมูลจากไฟล์ txt
with open('r1-r3-1.txt', 'r') as file:
    data = file.read()

# ใช้ regular expression หาค่า avg ของ round-trip
pattern = re.compile(r'round-trip min/avg/max = (\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+) ms')
matches = pattern.findall(data)

# สร้าง DataFrame จากข้อมูลที่ได้
df = pd.DataFrame(matches, columns=['min', 'avg', 'max'])

# บันทึกลง Excel
df.to_excel('output.xlsx', index=False)
