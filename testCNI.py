import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def run_kubectl_command(pod_name, server_pod_ip, package_size):
    command = f"kubectl exec -it {pod_name} -- iperf3 -c {server_pod_ip} -p 12345 -n {package_size}"
    run_command(command)

def run_ping_command(pod_name, server_pod_ip, package_size_ping):
    command = f"kubectl exec -it {pod_name} -- ping -c 1 {server_pod_ip} -l {package_size_ping}"
    run_command(command)

def run_tests(pod_name, server_pod_ip, package_sizes):
    for size in package_sizes:
        print(f"----------------------------------------------------------------------")
        print(f"Starting test with package size {size} Bytes")
        print(f"----------------------------------------------------------------------")
        for _ in range(10):
            if "ping" in size:
                run_ping_command(pod_name, server_pod_ip, size.split('_')[0])
            else:
                run_kubectl_command(pod_name, server_pod_ip, size)
        print(f"----------------------------------------------------------------------")
        print(f"Test completed with package size {size} Bytes")
        print(f"----------------------------------------------------------------------")

if __name__ == "__main__":
    # Get user input
    pod_name = input("Enter the pod name: ")
    server_pod_ip = input("Enter the server pod IP address: ")

    # Define package sizes for both iperf3 and ping
    iperf3_package_sizes = ["256", "1024", "4096", "16384"]
    ping_package_sizes = ["256_ping", "1024_ping", "4096_ping", "16384_ping"]

    # Run tests
    run_tests(pod_name, server_pod_ip, iperf3_package_sizes + ping_package_sizes)
