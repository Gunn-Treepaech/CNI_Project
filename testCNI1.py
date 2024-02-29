import os
import subprocess
import asyncio
def run_command(command, output_file):
    try:
        with open(output_file, "a") as file:
            subprocess.run(command, shell=True, check=True, stdout=file, stderr=file)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}", file=file)

async def run_kubectl_command(pod_name, server_pod_ip, package_size, output_file):
    command = f"kubectl exec -it {pod_name} -- iperf3 -c {server_pod_ip} -p 12345 -f k -n {package_size} -l {package_size}"
    await run_command(command, output_file)

async def run_ping_command(pod_name, server_pod_ip, package_size_ping, output_file):
    command = f"kubectl exec -it {pod_name} -- ping -c 1 {server_pod_ip} -s {package_size_ping}"
    await run_command(command, output_file)

#def run_tests(pod_name, server_pod_ip, package_sizes, output_file, localhost):
async def run_tests(pod_name, server_pod_ip, package_sizes, output_file,):
    for size in package_sizes:
        counter = 1
        for _ in range(10):
            if "ping" in size:
                asyncio.create_task(run_ping_command(pod_name, server_pod_ip, size.split('_')[0], output_file))
            else:
                asyncio.create_task(run_kubectl_command(pod_name, server_pod_ip, size, output_file))
            counter += 1
        print(f"Test completed with package size {size} Bytes")
    #curl_command = f"curl -X POST -F 'file=@{output_file}' http://{localhost}:5000/upload"
    curl_command = f"curl -X POST -F 'file=@{output_file}' http://192.168.50.25:5000/upload"
    os.system(curl_command)
    print(f"Upload completed")

if __name__ == "__main__":
    pod_name = input("ใส่ชื่อ pod ที่จะเข้าไปใช้คำสั่ง: ")
    server_pod_ip = input("ใส่ IP ของ Server Iperf: ")
    output_file = input("ใส่ชื่อ file: ")
    
    iperf3_package_sizes = ["100", "200", "400", "800", "1600", "3200", "6400", "12800", "25600", "51200", "102400"]
    ping_package_sizes = ["100_ping", "200_ping", "400_ping", "800_ping", "1600_ping", "3200_ping", "6400_ping", "12800_ping", "25600_ping", "51200_ping"]
    
    alls_name_pod = pod_name.split()
    lens = len(alls_name_pod)
    
    if lens > 1:
        for i in alls_name_pod:
            asyncio.create_task(run_tests(i, server_pod_ip, iperf3_package_sizes + ping_package_sizes, output_file))
    else:
        asyncio.create_task(run_tests(pod_name, server_pod_ip, iperf3_package_sizes + ping_package_sizes, output_file))
    
    #localhost = input("ใส่ localhost: ")
    #run_tests(pod_name, server_pod_ip, iperf3_package_sizes + ping_package_sizes, output_file, localhost)