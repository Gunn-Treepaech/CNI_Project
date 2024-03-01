import os
import subprocess
import asyncio

# สร้างฟังก์ชันสำหรับรันคำสั่งและบันทึกผลลัพธ์ลงในไฟล์
async def run_command(command, output_file):
    try:
        with open(output_file, "a") as file:
            subprocess.run(command, shell=True, check=True, stdout=file, stderr=file)
    except subprocess.CalledProcessError as e:
        print(f"เกิดข้อผิดพลาดในการรันคำสั่ง: {e}", file=file)

# สร้างฟังก์ชันสำหรับรันคำสั่ง iperf3
async def run_kubectl_command(pod_name, server_pod_ip, package_size, output_file):
    command = f"kubectl exec -it {pod_name} -- iperf3 -c {server_pod_ip} -p 12345 -f k -n {package_size} -l {package_size}"
    await run_command(command, output_file)

# สร้างฟังก์ชันสำหรับรันคำสั่ง ping
async def run_ping_command(pod_name, server_pod_ip, package_size_ping, output_file):
    command = f"kubectl exec -it {pod_name} -- ping -c 1 {server_pod_ip} -s {package_size_ping}"
    await run_command(command, output_file)

# ฟังก์ชันหลักสำหรับรันทุกการทดสอบ
async def run_tests(pod_name, server_pod_ip, package_sizes, output_file):
    for size in package_sizes:
        counter = 1
        for _ in range(10):
            if "ping" in size:
                await run_ping_command(pod_name, server_pod_ip, size.split('_')[0], output_file)
            else:
                await run_kubectl_command(pod_name, server_pod_ip, size, output_file)
            counter += 1
        print(f"ทดสอบเสร็จสิ้นด้วยขนาดแพ็คเกจ {size} Bytes")
    #curl_command = f"curl -X POST -F 'file=@{output_file}' http://{localhost}:5000/upload"
    curl_command = f"curl -X POST -F 'file=@{output_file}' http://192.168.50.25:5000/upload"
    os.system(curl_command)
    print(f"การอัปโหลดเสร็จสิ้น")

if __name__ == "__main__":
    pod_name = input("ป้อนชื่อ Pod เพื่อทำการรันคำสั่ง: ")
    server_pod_ip = input("ป้อน IP ของ Iperf Server: ")
    output_file = input("ป้อนชื่อไฟล์: ")

    # กำหนดขนาดแพ็คเกจสำหรับ iperf3 และ ping
    iperf3_package_sizes = ["100", "200", "400", "800", "1600", "3200", "6400", "12800", "25600", "51200", "102400"]
    ping_package_sizes = ["100_ping", "200_ping", "400_ping", "800_ping", "1600_ping", "3200_ping", "6400_ping", "12800_ping", "25600_ping", "51200_ping"]

    # ตรวจสอบว่ามีหลาย Pods หรือไม่
    alls_name_pod = pod_name.split()
    lens_pod = len(alls_name_pod)

    # ตรวจสอบว่ามีหลายไฟล์ผลลัพธ์หรือไม่
    all_output_file = output_file.split()
    lens_output = len(all_output_file)

    # ทดสอบและรันโค้ด asynchronous ตามจำนวน Pods หรือใช้ Default
    if lens_pod > 1 and lens_output > 1 and lens_output == lens_pod:
        for i in range(lens_pod):
            asyncio.run(run_tests(alls_name_pod[i], server_pod_ip, iperf3_package_sizes + ping_package_sizes, all_output_file[i]))
    else:
        asyncio.run(run_tests(pod_name, server_pod_ip, iperf3_package_sizes + ping_package_sizes, output_file))
