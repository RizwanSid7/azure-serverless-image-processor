### ✅ `README.md` – Azure Serverless Image Processing Pipeline

```markdown
# Azure Serverless Image Processing Pipeline

This project is a serverless solution built on Microsoft Azure that automatically processes and resizes images uploaded to Azure Blob Storage. The architecture uses **Azure Functions**, **Blob Storage**, **Event Grid**, and **Terraform** to provision infrastructure as code.

---

## 🧱 Project Architecture

- **Azure Blob Storage** – Stores uploaded images.
- **Azure Event Grid** – Detects blob upload events and forwards them.
- **Azure Function App** – Triggered by Event Grid to process/resize images.
- **Terraform** – Provisions all Azure resources as Infrastructure-as-Code (IaC).
- **Azure CLI / PowerShell** – For deploying and managing services.

---

## 🖥️ Prerequisites

- Azure subscription
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Terraform](https://developer.hashicorp.com/terraform/downloads)
- Git and GitHub account
- PowerShell (or any terminal)
- (Optional) Visual Studio Code

---

## 📁 Project Structure

```

azure-serverless-image-processor/
│
├── function-app/
│   ├── **init**.py              # Azure Function logic (Python script, pre-written)
│   ├── function.json            # Function binding configuration
│   └── requirements.txt         # Python dependencies (auto-installed by Azure)
│
├── terraform/
│   ├── main.tf                  # All Azure infrastructure (Function, Storage, Event Grid)
│   └── .terraform.lock.hcl
│
├── .gitignore
├── LICENSE
└── README.md

````

---

## ⚙️ Terraform Deployment Steps

> ✅ Run these commands in **Windows PowerShell** from the project root directory.

### 1. Login to Azure
```bash
az login
````

### 2. Initialize Terraform

```bash
cd terraform
terraform init
```

### 3. Plan Infrastructure

```bash
terraform plan
```

### 4. Apply Infrastructure

```bash
terraform apply
```

---

## 🚀 Deploy Azure Function

After infrastructure is deployed:

1. Go to the Azure Portal.
2. Open your **Function App**.
3. Use the **Code + Test** blade to upload or paste the `__init__.py` script.
4. Or use [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local) (optional).

---

## ✅ Features

* Event-driven image processing using Azure serverless services.
* Infrastructure provisioned through Terraform for consistency and reusability.
* Easily deployable using Azure CLI and PowerShell.
* Uses `.gitignore` to prevent large files or sensitive content from being pushed.

---

## 🔒 Security & Best Practices

* Sensitive files (e.g., `.terraform`, credentials) are excluded via `.gitignore`.
* Uses least privilege for Function App and Storage access.
* Followed Azure naming conventions and resource tagging.

---

## 📦 Git & Version Control Commands

```bash
git init
git remote add origin https://github.com/RizwanSid7/azure-serverless-image-processor.git
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

---

## 📌 Author

**Rizwan Siddiqui**
[GitHub Profile](https://github.com/RizwanSid7)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

```
