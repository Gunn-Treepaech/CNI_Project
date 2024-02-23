# Translate a Docker Compose File to Kubernetes Resources
- https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/
  ### ติดตั้ง Kompose บน Linux
  ```sh
  curl -L https://github.com/kubernetes/kompose/releases/download/v1.26.0/kompose-linux-amd64 -o kompose
  chmod +x kompose
  sudo mv ./kompose /usr/local/bin/kompose
  ```
  ### แปลง docker-compose.yml โดยใช้คำสั่ง
  ```sh
  kompose convert
  ```
