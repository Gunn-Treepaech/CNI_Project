## Vagrant
* SSH Only --> username: vagrant password: vagrant
* Login --> username: root password pass

## ipref3 with Kubernetes
* https://www.suse.com/support/kb/doc/?id=000020954
  ## Project Commad:
     ### แก้ hostname บน Linux:
          sudo nano /etc/hostname	
     ### ติ้ดตั้ง microk8s:
          sudo snap install microk8s --classic 
     ### ดูสถานะของ microk8s:
          microk8s status
     ### ดูสถานะ node ทั้งหมดใน cluster:
          kubectl get nodes
     ### Get ข้อมูลสำหรับเพิ่มเข้า cluster ใน node ที่เป็น master:
          sudo microk8s.add-node
     ### ลบ node ออกจาก cluster ใน master:
          sudo microk8s remove-node <node name> 
     ### ออกจาก cluster ใน worker:
          sudo microk8s.leave
     ### deploy from file yaml:
          kubectl apply -f iperf3-deployment.yaml
     ### delete deploy from file yaml:
          kubectl delete -f iperf3-deployment.yaml
     ### เลือก pod เพื่อเป็น server mode:
          kubectl exec -it {PodName} -- iperf3 -s -p 12345
     ### เลือก pod เพื่อเป็น client mode:
          kubectl exec -it {PodName} -- iperf3 -c {server pod IP address} -p 12345
     ### Get Pods:
          kubectl get pods -o wide

## Docker images linux/arm64
* https://hub.docker.com/r/taoyou/iperf3-alpine
