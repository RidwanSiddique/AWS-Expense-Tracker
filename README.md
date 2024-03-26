# AWS-Expense-Tracker

The AWS Expense Tracker is a serverless application designed to record and manage expenses. It provides an easy way to add, retrieve, and manage expense records through a simple API. Built on AWS using serverless architecture, it leverages various AWS services for scalability, reliability, and performance.

## Features

- **Add Expenses:** Users can submit expense details, including date, category, amount, and description.
- **Retrieve Expenses:** Users can retrieve their list of expenses by their user ID.

## Architecture

This application is built using the following AWS services:

- **AWS Lambda:** Manages the logic for adding and retrieving expenses, ensuring a serverless execution model that scales automatically with usage.
- **Amazon DynamoDB:** Stores expense records in a scalable, NoSQL database table. Each record is associated with a user ID, making it easy to retrieve all expenses for any given user.
- **Amazon API Gateway:** Provides RESTful endpoints for the application, allowing users to interact with the service via HTTP requests to add or retrieve expenses.
- **AWS IAM:** Manages access permissions, ensuring that the Lambda function has the necessary permissions to access DynamoDB and that API Gateway can invoke the Lambda function.

## Getting Started

This section outlines how to interact with the Expense Tracker application, including adding and retrieving expenses.

### Adding an Expense

Send a `POST` request to the `/expenses` endpoint with a JSON payload containing the expense details:

```json
{
  "Date": "2024-01-09",
  "Category": "Food",
  "SubCategory": "Coffee",
  "Description": "Morning coffee",
  "Cost": 2.25,
  "PaymentMethod": "Credit Card",
  "Location": "University Cafe"
}

```
## Retrieving Expenses

Send a `GET` request to the `/expenses/{userID}` endpoint, replacing `{userID}` with the user ID whose expenses you want to retrieve.

## Deployment

This application is deployed using AWS SAM (Serverless Application Model), which allows for easy deployment and management of the serverless components. The `template.yml` file defines the AWS resources and their configurations.

## Security

- All interactions with the API are secured through Amazon API Gateway, which can be configured to require API keys or authentication.
- Access permissions to AWS resources are tightly controlled through AWS IAM roles and policies, ensuring that each component of the application has only the permissions it needs.

## Future Enhancements

- Implement authentication and authorization to secure access to user-specific expenses.
- Add functionality for updating and deleting expenses.
- Integrate with AWS Cognito for user management.
- Provide detailed analytics and summaries of expenses by category, time period, etc.

## Contributing

Contributions to the AWS Expense Tracker are welcome! Please feel free to submit issues or pull requests with improvements or new features.
