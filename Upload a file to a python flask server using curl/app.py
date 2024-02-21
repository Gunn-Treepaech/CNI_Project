from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    # Create an "upload" folder if it doesn't exist
    upload_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'upload')
    os.makedirs(upload_dir, exist_ok=True)
    
    # Save the file to the "upload" folder and keep the original file name
    file.save(os.path.join(upload_dir, file.filename))
    
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
