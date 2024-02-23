# tshark deployment
- https://hub.docker.com/r/nicolaka/netshoot
- https://gist.github.com/githubfoam/6c9e07f95c2eb03ec4ae9709252c713f
  ### สร้าง Deployment และ Service
  ```sh
  kubectl apply -f tshark-deployment.yaml
  ```
  ### ลบ Deployment และ Service
  ```sh
  kubectl delete -f tshark-deployment.yaml
  ```
  ### เข้าถึง netshoot container
  ```sh
  kubectl exec -it <pod_name> -- /bin/bash
  ```
  ### รายการ interfaces ที่มีอยู่
  ```sh
  tshark -D
  ```
  ### เริ่มบันทึก traffic บน interface
  ```sh
  tshark -i <หมายเลขลำดับของ interface>
  ```
  ### บันทึก traffic ลงในไฟล์
  ```sh
  tshark -i 2 -w <ชื่อไฟล์.pcap>
  ```
  ### เรียกใช้ไฟล์ pcap หน้าต่าง interface ด้วย termshark
  ```sh
  termshark -r <ชื่อไฟล์.pcap>
  ```
