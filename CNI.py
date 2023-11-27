import subprocess

def run_kubectl_command(pod_name, server_pod_ip):
    command = f"kubectl exec -it {pod_name} -- iperf3 -c {server_pod_ip} -p 12345"
    
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running kubectl command: {e}")

# รับข้อมูล pod_name และ server_pod_ip จากผู้ใช้
pod_name = input("Enter the pod name: ")
server_pod_ip = input("Enter the server pod IP address: ")

# วนลูปเรียกใช้คำสั่ง 10 ครั้ง
for _ in range(10):
    run_kubectl_command(pod_name, server_pod_ip)
