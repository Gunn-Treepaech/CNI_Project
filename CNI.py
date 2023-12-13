import subprocess

def run_kubectl_command(pod_name, server_pod_ip, package_size):
    command = f"kubectl exec -it {pod_name} -- iperf3 -c {server_pod_ip} -p 12345 -n {package_size}"
    
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running kubectl command: {e}")

def run_ping_command(pod_name, server_pod_ip_ping, package_size_ping):
    command = f"kubectl exec -it {pod_name} -- ping {server_pod_ip_ping} -l {package_size_ping}"
    
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running kubectl command: {e}")

# รับข้อมูล pod_name และ server_pod_ip จากผู้ใช้
pod_name = input("Enter the pod name: ")
server_pod_ip = input("Enter the server pod IP address: ")
server_pod_ip_ping = input("Enter the server pod IP Ping address: ")

#----------------------------------------------------------------------------
# Iperf3
#----------------------------------------------------------------------------

print("เริ่มทดสอบที่ขนาด 256 Bytes")
for _ in range(10):
    run_kubectl_command(pod_name, server_pod_ip, 256)
print("เสร็จสิ้นการทดสอบที่ขนาด 256 Bytes")

print("เริ่มทดสอบที่ขนาด 1024 Bytes")
for _ in range(10):
    run_kubectl_command(pod_name, server_pod_ip, 1024)
print("เสร็จสิ้นการทดสอบที่ขนาด 1024 Bytes")

print("เริ่มทดสอบที่ขนาด 4096 Bytes")
for _ in range(10):
    run_kubectl_command(pod_name, server_pod_ip, 4096)
print("เสร็จสิ้นการทดสอบที่ขนาด 4096 Bytes")

print("เริ่มทดสอบที่ขนาด 16384 Bytes")
for _ in range(10):
    run_kubectl_command(pod_name, server_pod_ip, 16384)
print("เสร็จสิ้นการทดสอบที่ขนาด 16384 Bytes")

#----------------------------------------------------------------------------
# Ping
#----------------------------------------------------------------------------

print("เริ่มทดสอบ Ping ที่ขนาด 256 Bytes")
for _ in range(10):
    run_ping_command(pod_name, server_pod_ip, 256)
print("เสร็จสิ้นการทดสอบ Ping ที่ขนาด 256 Bytes")

print("เริ่มทดสอบ Ping ที่ขนาด 1024 Bytes")
for _ in range(10):
    run_ping_command(pod_name, server_pod_ip, 1024)
print("เสร็จสิ้นการทดสอบ Ping ที่ขนาด 1024 Bytes")

print("เริ่มทดสอบ Ping ที่ขนาด 4096 Bytes")
for _ in range(10):
   run_ping_command(pod_name, server_pod_ip, 4096)
print("เสร็จสิ้นการทดสอบ Ping ที่ขนาด 4096 Bytes")

print("เริ่มทดสอบ Ping ที่ขนาด 16384 Bytes")
for _ in range(10):
    run_ping_command(pod_name, server_pod_ip, 16384)
print("เสร็จสิ้นการทดสอบ Ping ที่ขนาด 16384 Bytes")