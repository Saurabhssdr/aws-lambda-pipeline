provider "aws" {
  region = "ap-south-1" 
}

# S3 Bucket
resource "aws_s3_bucket" "data_bucket" {
  bucket = "godigitalbucket546"  
}

# RDS Database
resource "aws_db_instance" "database" {
  identifier        = "rds-database"
  instance_class    = "db.t3.micro"
  engine            = "mysql"
  allocated_storage = 20
  username          = "admin"
  password          = "your-password"  # Replace with your secure password
  skip_final_snapshot = true
}

# Glue Database
resource "aws_glue_catalog_database" "glue_db" {
  name = "glue_database"  # Glue database name
}

# AWS ECR Repository
resource "aws_ecr_repository" "lambda_repo" {
  name = "lambda-container-repo"  # ECR repository name
}

# IAM Role for Lambda
resource "aws_iam_role" "lambda_role" {
  name = "lambda-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

