# Azure Serverless Image Processor

A serverless image resizing application built using Azure Blob Storage, Azure Functions, and Event Grid.

## Architecture

- User uploads an image to the **input** Blob container.
- Azure Function triggers on new uploads and resizes the image.
- Resized image is saved in the **output** Blob container.
- Application Insights monitors the function performance and logs.
- (Optional) Frontend for uploading and viewing images.

## Features

- Serverless architecture using Azure Functions (Python)
- Infrastructure as Code with Terraform
- Event-driven processing with Blob Storage triggers
- Real-time monitoring with Application Insights

## Getting Started

### Prerequisites

- Azure CLI installed
- Terraform installed
- Python 3.8+
- Azure Functions Core Tools (for local testing)

### Deployment

1. Clone this repo
2. Provision Azure resources with Terraform (`terraform/` folder)
3. Deploy Azure Function (`function-app/` folder)
4. (Optional) Deploy frontend in `static-frontend/`

## License

MIT License
