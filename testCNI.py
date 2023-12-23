import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def run_kubectl_command(pod_name, server_pod_ip, package_size):
    command = f"kubectl exec -it {pod_name} -- iperf3 -c {server_pod_ip} -p 12345 --bidir -f k -n {package_size} "
    run_command(command)

def run_ping_command(pod_name, server_pod_ip, package_size_ping):
    command = f"kubectl exec -it {pod_name} -- ping -c 1 {server_pod_ip} -s {package_size_ping}"
    run_command(command)

def run_tests(pod_name, pod_ip, server_pod_name, server_pod_ip, package_sizes):
    for size in package_sizes:
        print(f"----------------------------------------------------------------------")
        print(f"Starting test with package size {size} Bytes")
        print(f"----------------------------------------------------------------------")
        for _ in range(10):
            if "ping" in size:
                run_ping_command(pod_name, server_pod_ip, size.split('_')[0])
            elif "reverse" in size:
                run_ping_command(server_pod_name, pod_ip, size.split('_')[0])
            else:
                run_kubectl_command(pod_name, server_pod_ip, size)
        print(f"----------------------------------------------------------------------")
        print(f"Test completed with package size {size} Bytes")
        print(f"----------------------------------------------------------------------")

if __name__ == "__main__":
    # Get user input
    pod_name = input("Enter the pod name: ")
    pod_ip = input("Enter the pod IP address: ")
    server_pod_name = input("Enter the server pod name: ")
    server_pod_ip = input("Enter the server pod IP address: ")

    # ------ Define package sizes for both iperf3 and ping ------
    # ขนาดเล็ก (512 Byte): ขนาดแพ็กเก็ตขนาดเล็กเหมาะสำหรับการทดสอบความเร็วในการส่งข้อมูลแบบ bursty หรือการส่งข้อมูลจำนวนมากในเวลาสั้นๆ
    # ขนาดกลาง (6,000 Byte): ขนาดแพ็กเก็ตขนาดกลางเป็นขนาดแพ็กเก็ตมาตรฐานที่มักใช้ในการทดสอบเครือข่าย
    # ขนาดใหญ่ (40,000 Byte): ขนาดแพ็กเก็ตขนาดใหญ่เหมาะสำหรับการทดสอบ throughput ของเครือข่าย
    # ขนาดพิเศษ (100 MByte): ขนาดแพ็กเก็ตพิเศษเหมาะสำหรับการทดสอบ throughput ของเครือข่ายที่มีแบนด์วิดท์สูง
    # ------ END ------

    #iperf3_package_sizes = ["100M"]
    #ping_package_sizes = []
    iperf3_package_sizes = ["512", "6000", "40000", "100M"]
    ping_package_sizes = ["512_ping", "6000_ping", "40000_ping", "512_reverse", "6000_reverse", "40000_reverse"]

    # Run tests
    run_tests(pod_name, pod_ip, server_pod_name, server_pod_ip, iperf3_package_sizes + ping_package_sizes)
