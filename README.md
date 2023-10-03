vagrant
- SSH Only --> username: vagrant password: vagrant
- Login --> username: root password pass
-
  ipref3 with Kubernetes
- https://www.suse.com/support/kb/doc/?id=000020954
- choose a pod to run in server mode:
- kubectl exec -it <pod-name> -- iperf3 -s -p 12345
- choose a pod to run in client mode:
- kubectl exec -it <pod-name> -- iperf3 -c <server pod IP address> -p 12345
- kubectl get pods -o wide  
