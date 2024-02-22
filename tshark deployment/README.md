# tshark deployment
- https://hub.docker.com/r/nicolaka/netshoot
  ### สร้าง Deployment และ Service
  ```sh
  kubectl apply -f netshoot-deployment.yaml
  ```
  ### เข้าถึง netshoot container
  ```sh
  kubectl exec -it <pod_name> -- /bin/bash
  ```