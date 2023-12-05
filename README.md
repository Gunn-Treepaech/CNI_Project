## Vagrant
* SSH Only --> username: vagrant password: vagrant
* Login --> username: root password pass

## ipref3 with Kubernetes
* https://www.suse.com/support/kb/doc/?id=000020954
  ## Project Commad:
  ### Choose a pod to run in server mode:
     ### Choose a pod to run in server mode:
          kubectl exec -it {PodName} -- iperf3 -s -p 12345
     ### Choose a pod to run in client mode:
          kubectl exec -it {PodName} -- iperf3 -c {server pod IP address} -p 12345
     ### Get Pods:
          kubectl get pods -o wide

## Docker images linux/arm64
* https://hub.docker.com/r/taoyou/iperf3-alpine
