# Docker Image Build ให้ใช้ได้ทั้ง amd64 arm64
  ### ติดตั้ง Docker Buildx plugin ผ่าน package manager
  ```sh
  apt install docker-buildx-plugin
  ```
  ### ติดตั้ง Docker Buildx plugin ลงในระบบ Docker CLI เพื่อให้สามารถใช้งาน Docker Buildx ได้
  ```sh
  docker buildx install
  ```
  ### ติดตั้ง buildx CLI
  ```sh
  docker buildx create --use
  ```
  ### ตรวจสอบ builder instance ที่ถูกใช้
  ```sh
  docker buildx inspect
  ```
  ### สร้าง image ด้วยคำสั่ง
  ```sh
  docker buildx build --platform linux/amd64,linux/arm64 -t your-image-name:tag .
  ```
  ### push image ไปยัง Docker Hub หรือ registry อื่น ๆ ตามที่คุณต้องการ
  ```sh
  docker buildx build --platform linux/amd64,linux/arm64 -t your-docker-id/your-image-name:tag --push .
  ```
# Copy directories and files to and from Kubernetes Container [POD]
  ### command
  ```sh
  kubectl cp Videos/Video.mp4 <Pod-Name>:./videos/Video.mp4
  ```
