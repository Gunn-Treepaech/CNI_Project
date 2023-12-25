## Vagrant
* SSH Only --> username: vagrant password: vagrant
* Login --> username: root password pass

## ipref3 with Kubernetes
* https://www.suse.com/support/kb/doc/?id=000020954
  ## Project Commad:
     ### แก้โฮสต์ของคอมพิวเตอร์ Linux:
          sudo nano /etc/hostname	
     ### ติ้ดตั้ง microk8s:
          sudo snap install microk8s --classic --channel=1.28
     ### ถอนติ้ดตั้ง microk8s:
          sudo snap remove microk8s
     ### แสดงสถานะของ MicroK8s:
          microk8s status
     ### สร้างนามแฝง (alias) ให้กับคำสั่ง microk8s.kubectl ให้เป็น kubectl แทน:
          sudo snap alias microk8s.kubectl kubectl
     ### ดูสถานะ node ทั้งหมดใน cluster:
          kubectl get nodes
     ### ใช้เพิ่มโหนด (node) ใหม่ให้กับ MicroK8s:
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
          kubectl get pods -o wide -A
     ### Delete all pods in Terminating status
          for p in $(kubectl get pods | grep Terminating | awk '{print $1}'); do kubectl delete pod $p --grace-period=0 --force;done
     ### Get a Shell to a Running Container
          kubectl exec --stdin --tty {podname} --/bin/sh
     ## หรือ
          kubectl exec -it {podName} -- /bin/sh
     ### หา IP ของ Pod จากชื่อ Pod โดยใช้ kubectl
          kubectl get pod nginx-pod -o go-template --template '{{.status.podIP}}'
     ### Path Calico yaml Microk8s
          cd /var/snap/microk8s/current/args/cni-network/
     ### Apply CNI Calico yaml
          microk8s kubectl apply -f /var/snap/microk8s/current/args/cni-network/cni.yaml
     ### Apply CNI Cilium yaml
          microk8s kubectl apply -f /var/snap/microk8s/6239/actions/cilium.yaml
     ### เรียกข้อมูลการกำหนดค่า Cilium YAML
          microk8s kubectl get configmap cilium-config -n kube-system -o yaml
     ### บันทึกการกำหนดค่า
          microk8s kubectl get configmap cilium-config -n kube-system -o yaml > cilium-config.yaml
  
## Docker images linux/arm64
* https://hub.docker.com/r/taoyou/iperf3-alpine
## Understanding Kubernetes Cluster Networking
  ##### https://www.google.com/search?q=kubernetes+networking+models+overlay+underlay&sca_esv=593274838&sxsrf=AM9HkKlWnKcUA9WUmyfr58Jf0PtKWlzs9Q%3A1703344113052&ei=8feGZbvsAo6WjuMPz-692AU&oq=kubernetes+networking+models+overlay+undery&gs_lp=Egxnd3Mtd2l6LXNlcnAiK2t1YmVybmV0ZXMgbmV0d29ya2luZyBtb2RlbHMgb3ZlcmxheSB1bmRlcnkqAggAMgcQIRigARgKMgcQIRigARgKMgcQIRigARgKSKyvAVDPAljsgwFwAXgBkAEAmAGRAaABpA2qAQQ1LjExuAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICBRAhGKABwgIIECEYFhgeGB3CAggQABiABBiiBMICBhAAGB4YDcICBBAAGB7CAgYQABgWGB7iAwQYACBBiAYBkAYI&sclient=gws-wiz-serp
* https://romanglushach.medium.com/understanding-the-different-types-of-kubernetes-network-models-e1c93db146c
* https://collabnix.github.io/kubelabs/ClusterNetworking101/
* https://medium.com/@extio/understanding-kubernetes-node-to-node-communication-a-deep-dive-e1d6a5ff87f3
* https://www.zentao.pm/blog/kubernetes-network-model-1379.html
