import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def run_kubectl_command(pod_name, server_pod_ip, package_size):
    command = f"kubectl exec -it {pod_name} -- iperf3 -c {server_pod_ip} -p 12345 -f k -n {package_size} "
    run_command(command)

def run_ping_command(pod_name, server_pod_ip, package_size_ping):
    command = f"kubectl exec -it {pod_name} -- ping -c 1 {server_pod_ip} -s {package_size_ping}"
    run_command(command)

def run_tests(pod_name, server_pod_ip, package_sizes):
    for size in package_sizes:
        counter = 1
        print(f"----------------------------------------------------------------------")
        print(f"Starting test with package size {size} Bytes")
        print(f"----------------------------------------------------------------------")
        for _ in range(10):
            if "ping" in size:
                print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(f"Ping Test round {counter}")
                print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

                run_ping_command(pod_name, server_pod_ip, size.split('_')[0])

                print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(f"Ping Test round {counter} Completed")
                print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            else:
                print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(f"Test round {counter}")
                print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

                run_kubectl_command(pod_name, server_pod_ip, size)

                print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(f"Test round {counter} Completed")
                print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            counter += 1
        print(f"----------------------------------------------------------------------")
        print(f"Test completed with package size {size} Bytes")
        print(f"----------------------------------------------------------------------")

if __name__ == "__main__":
    # Get user input
    pod_name = input("Enter the pod name: ")
    server_pod_ip = input("Enter the server pod IP address: ")

    # ------ Define package sizes for both iperf3 and ping ------
    # ขนาดเล็ก (100 Byte): ขนาดแพ็กเก็ตขนาดเล็กเหมาะสำหรับการทดสอบความเร็วในการส่งข้อมูลแบบ bursty หรือการส่งข้อมูลจำนวนมากในเวลาสั้นๆ
    # ขนาดกลาง (1,000 Byte): ขนาดแพ็กเก็ตขนาดกลางเป็นขนาดแพ็กเก็ตมาตรฐานที่มักใช้ในการทดสอบเครือข่าย
    # ขนาดใหญ่ (10,000 Byte): ขนาดแพ็กเก็ตขนาดใหญ่เหมาะสำหรับการทดสอบ throughput ของเครือข่าย
    # ขนาดพิเศษ (100000 Byte): ขนาดแพ็กเก็ตพิเศษเหมาะสำหรับการทดสอบ throughput ของเครือข่ายที่มีแบนด์วิดท์สูง
    # ------ END ------

    #iperf3_package_sizes = ["100M"]
    #ping_package_sizes = []
    iperf3_package_sizes = ["100", "1000", "10000", "100000"]
    ping_package_sizes = ["100_ping", "1000_ping", "10000_ping"]

    # Run tests
    run_tests(pod_name, server_pod_ip, iperf3_package_sizes + ping_package_sizes)
