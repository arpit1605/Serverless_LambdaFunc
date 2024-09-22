# Serverless_LambdaFunc

# 1: Automated Instance Management Using AWS Lambda and Boto3

### Objective: In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that will automatically manage EC2 instances based on their tags.


#### 1. Create two EC2 instances:
Created an EC2 instance and associated with the Tag with Key as ‘Action’ and Value ‘Arpit-Auto-Start’: 
![image](https://github.com/user-attachments/assets/6d2da873-e455-48a1-9a58-eb97088b7707)

Created an EC2 instance and associated with the Tag with Key as ‘Action’ and Value ‘Arpit-Auto-Stop’:
![image](https://github.com/user-attachments/assets/d62dc35c-ff91-42dc-90ee-0fb477838c3f)

#### 2. Create an IAM role for EC2 permissions:
Creating an IAM role for Lambda function:

![image](https://github.com/user-attachments/assets/6cb7a508-04b3-4655-bf0f-2d0446847f3f)

Adding AmazonEC2FullAccess permissions:

![image](https://github.com/user-attachments/assets/c4488f70-e719-4f6d-a39c-26e8549b3449)

Naming the role:

![image](https://github.com/user-attachments/assets/ae3e20ef-c1a3-41b5-9729-6bcbab3c307d)

New IAM role has been created successfully:

![image](https://github.com/user-attachments/assets/2a7bdb02-a0e2-4437-9977-18dea6f90e63)

#### 3. Set up an AWS Lambda function:

Creating a Lambda Function for Auto Start and Auto Stop EC2 instances: 
Please remember to set a timeout of at least 10 seconds to prevent the function from failing in case of long execution time.

![image](https://github.com/user-attachments/assets/d38b014b-7fe5-4a4f-9c88-b51f39b8ac81)

Selecting the new IAM role that we just created for the Lambda function:

![image](https://github.com/user-attachments/assets/4662fd76-2b57-4b0f-bc96-d3fda41ccf9b)

#### 4. Testing:
State of EC2 instances before executing the Lambda function: The instance with ‘Arpit-Auto-Start’ tag is in stopped state and ‘Arpit-Auto-Stop' tag is in running state.

![image](https://github.com/user-attachments/assets/ca0c761c-dcaa-4b63-bf7b-21b2a124800d)

Deployed the changes and manually executed the Lambda Function and it executed successfully as shown below:

![image](https://github.com/user-attachments/assets/16a97a94-f2c9-42b7-97b8-11098c3aac13)

State of EC2 instances post execution the Lambda function: The instance with ‘Arpit-Auto-Start’ tag has started running and ‘Arpit-Auto-Stop' tag has been stopped.

![image](https://github.com/user-attachments/assets/d8a27293-2726-43d3-be67-d65543907154)





# 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

### Objective: To gain experience with AWS Lambda and Boto3 by creating a Lambda function that will automatically clean up old files in an S3 bucket.


#### 1. S3 Setup: 
Create an S3 bucket as below: 

![image](https://github.com/user-attachments/assets/430f1688-3751-4022-9087-3e8f03c2c77d)

![image](https://github.com/user-attachments/assets/ee5eda9c-0a7a-42ef-b3af-40550336f269)

![image](https://github.com/user-attachments/assets/00512ae2-28bf-4adb-a99d-9aac36217dd5)

![image](https://github.com/user-attachments/assets/ff894dfc-93ef-44c1-a469-5cce5e72f88e)

Uploaded some files as below:

![image](https://github.com/user-attachments/assets/8f2c7952-4220-4ccc-9011-9d82b9efed22)


#### 2. Lambda IAM Role: 

Create a new IAM role for Lambda function:

![image](https://github.com/user-attachments/assets/2cbdd756-ff59-4329-a245-7cf8a44e0484)

Add permission for AmazonS3FullAccess:

![image](https://github.com/user-attachments/assets/daa53124-b207-4b40-855c-5c59bc478c5c)

Name the Lambda function:

![image](https://github.com/user-attachments/assets/3bcc1ce5-c948-482d-8f35-490d621ad5c0)

Lambda function has been created successfully:

![image](https://github.com/user-attachments/assets/caff2097-0f4e-4284-a1d2-e4a3cd7c110c)

#### 3. Set up an AWS Lambda function:

Creating a Lambda Function for Automated S3 bucket cleanup: 
Please remember to set a timeout of at least 1 minute to prevent the function from failing in case of long execution time.

![image](https://github.com/user-attachments/assets/70e36511-6edd-4ab8-8a52-ed497f05b0d8)

![image](https://github.com/user-attachments/assets/e20cbeab-e6ff-464a-892c-dd0a1d472a55)

#### 4. Testing: 

Manually executed the lambda function to delete the files older than 30 days:

![image](https://github.com/user-attachments/assets/e5b3ec24-c639-4519-b0a7-a1e0e2a9a6a1)

All the files were 8 days older so all of them have been deleted successfully.

![image](https://github.com/user-attachments/assets/e5b5c826-12ba-460a-a1c7-b16b93b95aeb)



# 4. Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3

### Objective: To automate the backup process for your EBS volumes and ensure that backups older than a specified retention period are cleaned up to save costs.

#### 1. EBS Setup: 

Navigated to the EC2 dashboard and identified an EBS volume we wish to back up. 

![image](https://github.com/user-attachments/assets/60fb87a8-9eba-4c3b-a0f5-91d4f8a86e50)

#### 2. Create an IAM role for EC2 permissions:

Creating an IAM role for Lambda function:

![image](https://github.com/user-attachments/assets/9763fc76-8c09-4791-ab9d-2e60cd0af757)

Adding AmazonEC2FullAccess permission:

![image](https://github.com/user-attachments/assets/715a58ba-1316-40de-96cd-6f1273fe71ef)

Naming the role:

![image](https://github.com/user-attachments/assets/0aafa6b3-77ba-4c9d-9c8b-c9588b52f8e8)

New IAM role has been created successfully:

![image](https://github.com/user-attachments/assets/565af2ab-4a68-4a79-aa7c-466d9ab6957c)

#### 3. Set up an AWS Lambda function:

Creating a Lambda Function for Automatic EBS Snapshot and Cleanup: 
Please remember to set a timeout of at least 1 minute to prevent the function from failing in case of long execution time.

![image](https://github.com/user-attachments/assets/8ae99e6f-6163-4c87-be71-c9a18276e2b0)

Selecting the new IAM role that we just created for the Lambda function:

![image](https://github.com/user-attachments/assets/cc1156ac-b56f-4923-9b1e-ef6483e4710e)


#### 4. Testing:

Manually invoked the Lambda function. 
New snapshot snap-0499688ae728d6123 has been created as shown below in the execution result:

![image](https://github.com/user-attachments/assets/95cd6aff-c46c-4972-a814-562e9c45f5a7)

snap-0499688ae728d6123 is present in the Snapshots list as below:

![image](https://github.com/user-attachments/assets/7f09a390-8f17-437b-ab1b-de8e7de624a4)



# 8. Analyze Sentiment of User Reviews Using AWS Lambda, Boto3, and Amazon Comprehend

### Objective: Automatically analyze and categorize the sentiment of user reviews using Amazon Comprehend.

#### 1. Create an IAM role for EC2 permissions:
Creating an IAM role for Lambda function:

![image](https://github.com/user-attachments/assets/6203b745-b7e2-4913-953d-0cb5d7b33d57)

Adding ComprehendFullAccess permission:

![image](https://github.com/user-attachments/assets/971d6348-f624-4002-8d56-ff02bd296326)

Naming the role:

![image](https://github.com/user-attachments/assets/aff0d441-3bee-44c1-aa52-2d3c7ccb0122)

New IAM role has been created successfully:

![image](https://github.com/user-attachments/assets/b2d49ac7-d77e-47b5-ac0d-e6547e153731)

#### 2. Set up an AWS Lambda function:
Creating a Lambda Function for Analyze Sentiment of User Reviews: 
Please remember to set a timeout of at least 1 minute to prevent the function from failing in case of long execution time.

![image](https://github.com/user-attachments/assets/00e44d0a-dfdf-4e20-9efc-53d56b0b167e)


Selecting the new IAM role that we just created for the Lambda function:

![image](https://github.com/user-attachments/assets/6e14a030-7fc4-4114-bc98-032196c8f3eb)

#### 3. Testing: 

Click Test to trigger the function.  

![image](https://github.com/user-attachments/assets/ff6f098f-c6f9-4016-9196-b3f31b5eb23c)

Cloudwatch Logs:

![image](https://github.com/user-attachments/assets/5deb99d2-ae2c-48cb-a3b1-f1c44dbfefb9)

