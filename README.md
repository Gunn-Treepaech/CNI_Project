# ตั้งค่าสภาพแวดล้อม
  ### แก้โฮสต์ของคอมพิวเตอร์ Linux:
  ```sh
  sudo nano /etc/hostname
  ```
  ### ติ้ดตั้ง microk8s:
  ```sh
  sudo snap install microk8s --classic --channel=1.28
  ```
  ### ถอนติ้ดตั้ง microk8s:
  ```sh
  sudo snap remove microk8s
  ```
  ### แสดงสถานะของ MicroK8s:
  ```sh
  microk8s status
  ```
  ### สร้างนามแฝง (alias) ให้กับคำสั่ง microk8s.kubectl ให้เป็น kubectl แทน:
  ```sh
  sudo snap alias microk8s.kubectl kubectl
  ```
  ### ดูสถานะ node ทั้งหมดใน cluster:
  ```sh
  kubectl get nodes
  ```
  ### ใช้เพิ่มโหนด (node) ใหม่ให้กับ MicroK8s:
  ```sh
  sudo microk8s.add-node
  ```
  ### ลบ node ออกจาก cluster ใน master:
  ```sh
  sudo microk8s remove-node worker1
  sudo microk8s remove-node worker2
  sudo microk8s remove-node worker3
  sudo microk8s remove-node workervm1
  sudo microk8s remove-node workervm2
  sudo microk8s remove-node workervm3
  sudo microk8s remove-node workervm4
  ```
  ### ออกจาก cluster ใน worker:
  ```sh
  sudo microk8s.leave
  ```
# ปรับใช้จากไฟล์ yaml
  ### deploy from file yaml:
  ```sh
  kubectl apply -f iperf3-deployment.yaml
  ```
  ### delete deploy from file yaml:
  ```sh
  kubectl delete -f iperf3-deployment.yaml
  ```
  ### เลือก pod เพื่อเป็น server mode:
  ```sh
  kubectl exec -it {PodName} -- iperf3 -s -p 12345
  ```
  ### เลือก pod เพื่อเป็น client mode:
  ```sh
  kubectl exec -it {PodName} -- iperf3 -c {server pod IP address} -p 12345
  ```
  ### Get Pods:
  ```sh
  kubectl get pods -o wide -A
  ```
  ### Get a Shell to a Running Container:
  ```sh
  kubectl exec -it {podName} -- /bin/sh
  ```
  ### Delete all pods in Terminating status:
  ```sh
  for p in $(kubectl get pods | grep Terminating | awk '{print $1}'); do kubectl delete pod $p --grace-period=0 --force;done
  ```
# เปลี่ยน topology ของ CNI
  ### Path Calico yaml Microk8s:
  ```sh
  cd /var/snap/microk8s/current/args/cni-network/
  ```
  ### Apply CNI Calico yaml:
  ```sh
  microk8s kubectl apply -f /var/snap/microk8s/current/args/cni-network/cni.yaml
  ```
# เปลี่ยน CNI เป็น Cilium
  ```sh
  microk8s enable community
  microk8s enable cilium
  ```
# เปลี่ยน CNI เป็น Flannel
  ```sh
  microk8s disable ha-cluster --force
  ```
