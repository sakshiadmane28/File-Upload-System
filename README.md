# File Upload System Using Amazon EC2 and Amazon S3

## Project Overview
This project is a cloud-based file upload application developed using Python, Flask, and Boto3. The application is hosted on an Amazon EC2 instance and allows users to upload files through a web interface. Uploaded files are securely stored in an Amazon S3 bucket.

## Features
- Upload files through a web interface
- Store files securely in Amazon S3
- Flask-based backend
- Hosted on Amazon EC2
- Uses Boto3 to interact with AWS services
- Simple HTML and CSS user interface

## Technologies Used
- Amazon EC2
- Amazon S3
- AWS IAM
- Python
- Flask
- Boto3
- HTML
- CSS

## Project Structure
```
project/
│── app.py
│── index.html
│── README.md


## How It Works
1. The user selects a file from the web page.
2. Flask receives the uploaded file.
3. Boto3 connects to Amazon S3.
4. The file is uploaded to the S3 bucket.
5. A success message is displayed.

## EC2 Deployment Commands
sudo dnf update -y
sudo dnf install -y python3-pip git
python3 --version
pip3 --version
mkdir -p /home/ec2-user/s3-upload-app/templates
cd /home/ec2-user/s3-upload-app
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install Flask boto3
pip freeze > requirements.txt

## Future Improvements
- Multiple file upload
- User authentication
- File preview
- Upload progress bar
- File download functionality

## Author
 Sakshi Admane
