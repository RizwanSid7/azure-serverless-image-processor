provider "azurerm" {
  features {}
}

resource "random_string" "suffix" {
  length  = 6
  upper   = false
  number  = true
  special = false
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-serverless-image-${random_string.suffix.result}"
  location = "East US"
}

resource "azurerm_storage_account" "storage" {
  name                     = "srvimgproc${random_string.suffix.result}"
  resource_group_name      = azurerm_resource_group.rg.name
  location                = azurerm_resource_group.rg.location
  account_tier            = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "input" {
  name                  = "input"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "private"
}

resource "azurerm_storage_container" "output" {
  name                  = "output"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "private"
}

# You can add resources for Function App and Application Insights later.
