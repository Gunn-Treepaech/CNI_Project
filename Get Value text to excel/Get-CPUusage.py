import pandas as pd
import os

# ระบุ path ปัจจุบัน
path = os.getcwd()

# วนลูปผ่านไฟล์ text ทั้งหมดใน path
for filename in os.listdir(path):
  if filename.endswith(".txt"):
    # อ่านข้อมูลจากไฟล์ text
    data = pd.read_csv(filename, delim_whitespace=True)

    # เก็บเฉพาะคอลัมน์ %idle
    idle_data = data["%idle"]

    # บันทึกข้อมูลลงเป็นไฟล์ Excel โดยใช้ชื่อไฟล์เดียวกันกับไฟล์ text
    idle_data.to_excel(filename.replace(".txt", ".xlsx"), index=False)
