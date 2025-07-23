# Capstone 1 – AWS Cloud Institute

This project was part of my AWS Cloud Institute training, where I built a real-world serverless application using multiple AWS services. The goal was to simulate a workflow for processing and validating customer documents in a cloud-native way.

## What the Project Does

The app handles a customer’s application package, which includes a selfie, a photo ID, and a details file. Here's what it does behind the scenes:

- Pulls the documents from an S3 bucket
- Unzips and organizes them
- Parses the customer details from a CSV file
- Compares the face on the ID and the selfie using Amazon Rekognition
- Saves the results into DynamoDB
- Sends out an SNS notification about the match status

It’s all event-driven and fully serverless.

## AWS Services Used

- **Lambda** – backend logic (split across multiple functions)
- **API Gateway** – for triggering Lambda if needed
- **Amazon S3** – to store zipped and unzipped files
- **Amazon Rekognition** – to compare facial images
- **Amazon DynamoDB** – for storing application and match results
- **SNS** – to send out notification messages
- **AWS Step Functions** – to orchestrate the process
- **AWS SAM** – used to build and deploy everything as infrastructure-as-code

## Folder Breakdown

- `CompareDetailsLambdaFunction/` – Parses and stores CSV details
- `CompareFacesLambdaFunction/` – Handles face comparison with Rekognition
- `SubmitLicenseLambdaFunction/` – Moves license image to the right place
- `UnzipLambdaFunction/` – Extracts files from zipped input
- `ValidateLicenseLambdaFunction/` – Validates document structure
- `WriteToDynamoLambdaFunction/` – Writes final results to DynamoDB
- `template.yaml` – SAM template defining the infrastructure
- `README.md` – You're reading it

## What I Learned

Before this, I had a good understanding of AWS basics. This project pushed me deeper into how all the services work together — especially Step Functions and SAM. I also got more comfortable troubleshooting issues during deployment and thinking about security, scalability, and permissions the way real cloud developers do.

## About Me

I'm Diego Labra, an AWS Cloud Institute student and aspiring cloud developer. I come from a healthcare background but have shifted into cloud computing because I love solving problems and building things that run at scale. If you're hiring or just want to connect, I’d love to chat!

[LinkedIn](https://www.linkedin.com/in/diegolabra8310) 
