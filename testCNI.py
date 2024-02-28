import subprocess
from threading import Thread

def run_command(command, pod_name, size, counter):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command for {size} round {counter} in pod {pod_name}: {e}")

def run_kubectl_command(pod_name, server_pod_ip, package_size, counter):
    command = f"kubectl exec -it {pod_name} -- iperf3 -c {server_pod_ip} -p 12345 -f k -n {package_size} "
    return Thread(target=run_command, args=(command, pod_name, package_size, counter))

def run_ping_command(pod_name, server_pod_ip, package_size_ping, counter):
    command = f"kubectl exec -it {pod_name} -- ping -c 1 {server_pod_ip} -s {package_size_ping}"
    return Thread(target=run_command, args=(command, pod_name, package_size_ping, counter))

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
                thread = run_ping_command(pod_name, server_pod_ip, size.split('_')[0], counter)
            else:
                print(f"----------------------------------------------------------------------")
                print(f"{size} Test round {counter}")
                print(f"----------------------------------------------------------------------")
                # Code
                thread = run_kubectl_command(pod_name, server_pod_ip, size, counter)

            thread.start()
            thread.join()  # Wait for the completion of the current command before starting the next one
            counter += 1

        print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"Test completed with package size {size} Bytes")
        print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

if __name__ == "__main__":
    # Get user input
    pod_name = input("Enter the pod name to run commands: ")
    server_pod_ip = input("Enter the IP of the Iperf server: ")
    
    all_pod_name = pod_name.split()
    len_all_pod_name = len(all_pod_name)

    # ------ Define package sizes for both iperf3 and ping ------
    iperf3_package_sizes = ["100", "1000", "10000", "100000"]
    ping_package_sizes = ["100_ping", "1000_ping", "10000_ping"]

    # Run tests
    if len_all_pod_name >= 1:
        for i in all_pod_name:
            run_tests(i, server_pod_ip, iperf3_package_sizes + ping_package_sizes)
    else:
        run_tests(pod_name, server_pod_ip, iperf3_package_sizes + ping_package_sizes)
