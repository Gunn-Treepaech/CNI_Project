Vagrant.configure(2) do |config|

  # Use shell provision for setting thing up
  USERNAME = "root"
  PASSWORD = "pass"
  config.vm.provision "shell", path: "install.sh", :args => [USERNAME, PASSWORD]

  # Define the number of VMs to create
  NodeCount = 1

  # Define the list of IP addresses to use
  ips = ["192.168.56.20"]

  (1..NodeCount).each do |i|

    config.vm.define "workerVM#{i}" do |node|

      # Create a VM
      node.vm.box               = "ubuntu/focal64"
      node.vm.box_check_update  = false
      node.vm.hostname          = "workerVM#{i}.example.com"

      # Configure a static IP address for the VM
      node.vm.network "private_network", ip: ips[i-1]

      # Set the number of CPUs, RAM, and cores
      node.vm.provider :virtualbox do |v|
        v.name    = "workerVM#{i}"
        v.memory  = 1024
        v.cpus    = 1
      end

      node.vm.provider :libvirt do |v|
        v.nested  = true
        v.memory  = 1024
        v.cpus    = 1
      end

    end

  end

end
