# Upload a file to a python flask server using curl
  ### อัปโหลดไฟล์ไปยังเซิร์ฟเวอร์ที่รอรับไฟล์
  ```sh
  curl -X POST -F "file=@va.txt" http://localhost:5000/upload
  ```