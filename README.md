# Amazon EKS from Code to Deploy (Level 100-200)
## Reference
    https://aws.amazon.com/blogs/containers/introducing-security-groups-for-pods

    https://github.com/awsdocs/amazon-eks-user-guide/blob/master/doc_source/security-groups-for-pods.md

    https://github.com/awsdocs/amazon-eks-user-guide/blob/master/doc_source/cni-upgrades.md

    https://eksworkshop.com


## Pre-requisites
- AWS Accounts
---
## Step to follow How to Amazon CLI on S3
 
 ## 1.) Create EKS cluster with following lab url:
    https://www.eksworkshop.com/020_prerequisites/workspace/#region-3

Follow step by step, till you have finished "Test the Cluster"

---
## 2.) Getting VPC ID

     VPCID=$(aws eks describe-cluster --name eksworkshop-eksctl \
    --query "cluster.resourcesVpcConfig.vpcId" \
    --output text)

    echo $VPCID

---
## 3.) Create Security Group and Postgres Database using Amazon RDS

     RDSSG=$(aws ec2 create-security-group --group-name RDSDbAccessSG --description "Security group to apply to apps that need access to RDS" --vpc-id $VPCID --query "GroupId" --output text)

    echo $RDSSG  

Refering the step below to create Amazon RDS Postgres
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html#CHAP_GettingStarted.Creating.PostgreSQL

Challenge:
- How can you enable inbound traffic from EKS to be able to connect to Amazon RDS Postgres?


---
## 4.) Build docker and push to Amazon ECR

    docker build -t postgres-test .
    aws ecr create-repository --repository-name postgres-test-demo
    
    aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin <AWS ACCOUNT ID>.dkr.ecr.ap-southeast-1.amazonaws.com

    docker tag postgres-test <AWS ACCOUNT ID>.dkr.ecr.ap-southeast-1.amazonaws.com/postgres-test-demo:latest

    docker push <AWS ACCOUNT ID>.dkr.ecr.ap-southeast-1.amazonaws.com/postgres-test-demo:latest

---
## 5.) Deploy Sample Application 

Let’s deploy our application and test that only the desired pods can access our RDS database. 
Save the following as postgres-test.yaml. Replace the HOST, DATABASE, and USER environment variables with the values 
from the step above where you created the RDS database.

    kubectl apply -f postgres-test.yaml
    kubectl describe pod postgres-test
    kubectl describe pod postgres-test

Challenge:
- How can you secure database credentials!! I do not want to store in kube manifest file..

---
## 6.) Checking if your pod can connect to Amazon RDS Postgres 

    kubectl logs postgres-test
   
 # Congrats, You are ready to develop your code, and deploy to Amazon EKS !!!


 ## Optional Useful Lab (Level 200-300)

 ## 1.) DEPLOY THE EXAMPLE MICROSERVICES
    https://www.eksworkshop.com/beginner/050_deploy/

 ## 2.) CI/CD WITH CODEPIPELINE
    https://github.com/aws-samples/amazon-eks-cicd-codebuild

    https://www.eksworkshop.com/intermediate/220_codepipeline/      

 ## 3.) DEPLOYING MICROSERVICES TO EKS FARGATE
    https://www.eksworkshop.com/beginner/180_fargate/  

 ## 4.) DEPLOYING STATEFUL MICROSERVICES WITH AWS EFS
    https://www.eksworkshop.com/beginner/190_efs/     

 ## 5.) USING SPOT INSTANCES WITH EKS
    https://www.eksworkshop.com/beginner/150_spotworkers/       


# Congrats, You are ready to develop your code, and deploy to Amazon EKS !!!

