import os

def rename_files(directory, file_type):
    # ตรวจสอบว่า directory มีอยู่จริงหรือไม่
    if not os.path.exists(directory):
        print(f"Directory '{directory}' ไม่มีอยู่")
        return

    # ตรวจสอบว่า directory เป็น directory หรือไม่
    if not os.path.isdir(directory):
        print(f"'{directory}' ไม่ใช่ directory")
        return

    # รวบรวมไฟล์ทั้งหมดใน directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # กรองไฟล์ที่มีชนิดตามที่กำหนด
    filtered_files = [f for f in files if f.endswith(file_type)]

    # เรียงลำดับไฟล์ตามชื่อ
    filtered_files.sort()

    # เปลี่ยนชื่อไฟล์เป็นตัวเลขเรียงลำดับ
    for i, filename in enumerate(filtered_files):
        new_filename = f"{i+1:03d}{file_type}"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        print(f"เปลี่ยนชื่อไฟล์ '{filename}' เป็น '{new_filename}'")

# เรียกใช้ฟังก์ชัน
rename_files("D:\\ami\\ami\\VDO", ".png")

