import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def run_kubectl_command(pod_name, server_pod_ip, package_size):
    command = f"kubectl exec -it {pod_name} -- iperf3 -c {server_pod_ip} -p 12345 -f k -n {package_size} -l {package_size}"
    run_command(command)

def run_ping_command(pod_name, server_pod_ip, package_size_ping):
    command = f"kubectl exec -it {pod_name} -- ping -c 1 {server_pod_ip} -s {package_size_ping}"
    run_command(command)

def run_tests(pod_name, server_pod_ip, package_sizes):
    for size in package_sizes:
        counter = 1
        print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"Starting test with package size {size} Bytes")
        print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for _ in range(10):
            if "ping" in size:
                print(f"----------------------------------------------------------------------")
                print(f"{size} Ping Test round {counter}")
                print(f"----------------------------------------------------------------------")
                # Code
                run_ping_command(pod_name, server_pod_ip, size.split('_')[0])
            else:
                print(f"----------------------------------------------------------------------")
                print(f"{size} Test round {counter}")
                print(f"----------------------------------------------------------------------")
                # Code
                run_kubectl_command(pod_name, server_pod_ip, size)
            counter += 1
        print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"Test completed with package size {size} Bytes")
        print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

if __name__ == "__main__":
    # Get user input
    pod_name = input("ใส่ชื่อ pod ที่จะเข้าไปใช้คำสั่ง: ")
    server_pod_ip = input("ใส่ IP ของ Server Iperf: ")
    package_sizes = input("ใส่ขนาดแพ็กเก็ตที่ต้องการทดสอบ (คั่นด้วย ,): ").split(",")

    # Run tests
    run_tests(pod_name, server_pod_ip, package_sizes)