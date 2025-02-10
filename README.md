# aws-lambda-pipeline
# AWS CI/CD Pipeline Project

## Overview
This project sets up an **AWS CI/CD pipeline using Jenkins** to:
1. Read data from **S3**, push it to **RDS**, and if RDS is unavailable, store it in **Glue Database**.
2. Create a **Docker image** of the Python script and deploy it to **AWS ECR**.
3. Use **Terraform** to create all required AWS resources.

## **Work Completed**
✅ 1. **AWS Resource Creation** via Terraform (Verified with Screenshots)  
✅ 2. **Jenkins Pipeline Execution** (Terraform code pushed, Pipeline Output captured)  
❌ 3. **Lambda Function Deployment using ECR** (Pending due to limited time)

## **Screenshots Included**
- Terraform resource creation
- Jenkins pipeline execution
- AWS resources (S3, RDS, ECR, Glue)
- Docker image push to ECR

## **Pending Work (Lambda Function Deployment)**
Due to the **limited submission time**, I could not complete **Lambda function deployment using the ECR image**. However, I have:
- Set up the ECR repository
- Created the required AWS resources  
I can complete this part if given additional time.


