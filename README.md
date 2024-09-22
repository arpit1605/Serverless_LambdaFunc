# Serverless_LambdaFunc

**1: Automated Instance Management Using AWS Lambda and Boto3
Objective: In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that will automatically manage EC2 instances based on their tags.**

**1.Create two EC2 instances:**
Created an EC2 instance and associated with the Tag with Key as ‘Action’ and Value ‘Arpit-Auto-Start’: 
![image](https://github.com/user-attachments/assets/6d2da873-e455-48a1-9a58-eb97088b7707)

Created an EC2 instance and associated with the Tag with Key as ‘Action’ and Value ‘Arpit-Auto-Stop’:
![image](https://github.com/user-attachments/assets/d62dc35c-ff91-42dc-90ee-0fb477838c3f)

**2.Create an IAM role for EC2 permissions:**
Creating an IAM role for Lambda function:
![image](https://github.com/user-attachments/assets/6cb7a508-04b3-4655-bf0f-2d0446847f3f)

Adding AmazonEC2FullAccess permission:
![image](https://github.com/user-attachments/assets/c4488f70-e719-4f6d-a39c-26e8549b3449)

Naming the role:
![image](https://github.com/user-attachments/assets/ae3e20ef-c1a3-41b5-9729-6bcbab3c307d)

New IAM role has been created successfully:
![image](https://github.com/user-attachments/assets/2a7bdb02-a0e2-4437-9977-18dea6f90e63)

**3.Set up an AWS Lambda function:**
Creating a Lambda Function for Auto Start and Auto Stop EC2 instances: 
Please remember to set a timeout of at least 10 seconds to prevent the function from failing in case of long execution time.
![image](https://github.com/user-attachments/assets/d38b014b-7fe5-4a4f-9c88-b51f39b8ac81)

Selecting the new IAM role that we just created for the Lambda function:
![image](https://github.com/user-attachments/assets/4662fd76-2b57-4b0f-bc96-d3fda41ccf9b)

**4.Testing:**
State of EC2 instances before executing the Lambda function: The instance with ‘Arpit-Auto-Start’ tag is in stopped state and ‘Arpit-Auto-Stop' tag is in running state.
![image](https://github.com/user-attachments/assets/ca0c761c-dcaa-4b63-bf7b-21b2a124800d)

Deployed the changes and manually executed the Lambda Function and it executed successfully as shown below:
![image](https://github.com/user-attachments/assets/16a97a94-f2c9-42b7-97b8-11098c3aac13)

State of EC2 instances post execution the Lambda function: The instance with ‘Arpit-Auto-Start’ tag has started running and ‘Arpit-Auto-Stop' tag has been stopped.
![image](https://github.com/user-attachments/assets/d8a27293-2726-43d3-be67-d65543907154)





