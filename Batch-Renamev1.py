import os

def rename_files(directory, extension):
    # ตรวจสอบว่า Directory นี้มีอยู่จริงหรือไม่
    if not os.path.exists(directory):
        print(f"Directory '{directory}' ไม่มีอยู่")
        return

    # ดึงรายการไฟล์ทั้งหมดใน Directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # กรองไฟล์ที่ตรงกับ extension ที่กำหนด
    filtered_files = [f for f in files if f.endswith(extension)]

    # เรียงลำดับไฟล์ตามชื่อ
    filtered_files.sort()

    # เริ่มต้นตัวเลขที่จะใช้ในการเปลี่ยนชื่อไฟล์
    counter = 1

    # เปลี่ยนชื่อไฟล์ตามรูปแบบที่ต้องการ
    for old_name in filtered_files:
        # สร้างชื่อไฟล์ใหม่
        new_name = f"{counter:03d}{extension}"

        # สร้าง path ทั้งหมด
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)

        # เปลี่ยนชื่อไฟล์
        os.rename(old_path, new_path)

        # เพิ่มค่า counter สำหรับการสร้างชื่อไฟล์ถัดไป
        counter += 1

    print(f"Rename เสร็จสิ้น: {counter-1} ไฟล์")

# เรียกใช้ฟังก์ชัน
rename_files("D:\ami\ami\VDO", ".jpg")
