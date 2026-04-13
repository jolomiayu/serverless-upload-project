# 🚀 Serverless File Upload System

This project is a fully serverless application that enables secure file upload and download using AWS services.

## 🧱 Architecture

API Gateway → Lambda → S3

- API Gateway handles HTTP requests
- Lambda generates pre-signed URLs
- S3 stores files securely

## ⚙️ Features

- Generate secure upload URLs
- Upload files directly to S3
- Generate download URLs
- Time-limited access using pre-signed URLs
- No backend file handling (scalable & efficient)

## 🛠️ Tech Stack

- AWS Lambda
- Amazon S3
- API Gateway
- GitHub
- AWS CodeBuild (CI)

## 🔄 Workflow

1. Request upload URL
2. Upload file directly to S3
3. Request download URL
4. Access file securely

## 💡 What I Learned

- Handling AWS pre-signed URLs
- Debugging real-world cloud errors (403, 500)
- Managing service regions correctly
- Lambda packaging and deployment
- Building CI pipelines with CodeBuild

## 🔗 GitHub Repository

https://github.com/jolomiayu/serverless-upload-project
