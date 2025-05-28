# Azure Function: Storage Queue & SQL Output Binding (Python)

**Name:** Mohit Singh Panwar  
**Student ID:** 041167761  
**Email:** panw0011@algonquinlive.com  
**Video DEMO Part1:** https://youtu.be/woDNxiDn04A
**Video DEMO Part2:** https://youtu.be/WM0uYmA7LYY


This project demonstrates how to create and deploy Azure Functions in Python that:

- Send messages to an Azure Storage Queue
- Insert records into an Azure SQL Database

Both functions are developed using **Visual Studio Code** and tested locally before being deployed to Azure.

---

## ✅ Tasks Completed

### 1. Storage Queue Output Binding

- Followed the official Azure Storage Queue binding QuickStart.
- Used Python and VS Code for local development.
- Tested function locally using REST and curl.
- Deployed to Azure and verified messages appeared in `outqueue` via Azure Storage Explorer.

### 2. Azure SQL Output Binding

- Followed the official Azure SQL output binding QuickStart.
- Set up `mySampleDatabase` in Azure SQL with a `dbo.ToDo` table.
- Verified that HTTP-triggered inserts are written to the database using the Azure Query Editor.

---

## ⚙️ Setup Instructions

### Azure Resources Created

| Resource           | Name               |
|--------------------|--------------------|
| Azure Storage      | myhttptrigger2     |
| Azure Queue        | outqueue           |
| Azure SQL Database | mySampleDatabase   |
| SQL Server         | msp21.database.windows.net |
| Function App       | my-http-trigger-app (example) |

### Local Environment Prerequisites

- Python 3.8 or 3.9
- Azure Functions Core Tools
- VS Code with extensions:
  - Python
  - Azure Functions
  - Azure Storage
- Azure Storage Explorer
- Azurite (optional for local queue emulation)

---

### 1. Create or Open Azure Function Project
- Use VS Code to either create a new Azure Function project or open an existing one.

### 2. Download Remote App Settings
To sync Azure Storage locally:
- F1 → `Azure Functions: Download Remote Settings...`
- Select Function App
- Overwrite `local.settings.json`
- Copy `AzureWebJobsStorage` value

### 3. Register Binding Extensions
Ensure `host.json` includes:

#### For Queue Binding:
```json
{
  "version": "2.0",
  "extensionBundle": {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[3.*, 4.0.0)"
  }
}
```

#### For SQL Binding:
```json
{
  "version": "2.0",
  "extensionBundle": {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[4.*, 5.0.0)"
  }
}
```

---

## 📦 Queue Output Binding

### Function Code (function_app.py)

```python
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpExample")
@app.queue_output(arg_name="msg", queue_name="outqueue", connection="AzureWebJobsStorage")
def HttpExample(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> func.HttpResponse:
    logging.info('Processing HTTP request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
            name = req_body.get('name')
        except ValueError:
            pass

    if name:
        msg.set(name)
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body.",
            status_code=200
        )
```

### Run & Test
- Press **F5** to run locally
- Right-click `HttpExample` → Execute
- Test input: `{ "name": "Azure" }`

### Check Queue
- Open Azure Storage Explorer → Queues → `outqueue`
- Confirm message is present

### Deploy
- F1 → `Azure Functions: Deploy to Function App`

---

## 🗃️ SQL Output Binding

### Azure SQL Setup

#### 1. Create SQL Database
- Name: `mySampleDatabase`
- Server: globally unique
- Auth: SQL Server Authentication
- Allow Azure services access ✅

#### 2. Create Table
Query Editor → Run:

```sql
CREATE TABLE dbo.ToDo (
    [Id] UNIQUEIDENTIFIER PRIMARY KEY,
    [order] INT NULL,
    [title] NVARCHAR(200) NOT NULL,
    [url] NVARCHAR(200) NOT NULL,
    [completed] BIT NOT NULL
);
```

#### 3. Add App Setting
F1 → `Azure Functions: Add New Setting...`  
Name: `SqlConnectionString`  
Value: Your edited ADO.NET connection string

### Function Code (function_app.py)

```python
import azure.functions as func
import logging
from azure.functions.decorators.core import DataType
import uuid

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
@app.generic_output_binding(
    arg_name="toDoItems",
    type="sql",
    CommandText="dbo.ToDo",
    ConnectionStringSetting="SqlConnectionString",
    data_type=DataType.STRING
)
def test_function(req: func.HttpRequest, toDoItems: func.Out[func.SqlRow]) -> func.HttpResponse:
    logging.info('Processing HTTP request.')

    name = req.get_json().get('name')
    if name:
        toDoItems.set(func.SqlRow({
            "Id": str(uuid.uuid4()),
            "title": name,
            "completed": False,
            "url": ""
        }))
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
            "Please pass a name in the request body",
            status_code=400
        )
```

### Run & Test
- F5 → Run locally
- Right-click `HttpTrigger1` → Execute Function
- Test input: `{ "name": "Azure" }`

### Check SQL Output
Query:
```sql
SELECT TOP 1000 * FROM dbo.ToDo;
```

### Deploy
- F1 → `Azure Functions: Deploy to Function App`

---

## 💡 What I Learned

- How to set up Python Azure Functions using the v2 programming model
- How to bind output to both Azure Queue and Azure SQL
- The value of extension bundles and correct JSON schema mapping
- Debugging queue and database connectivity issues
- Using Azure Storage Explorer and Query Editor for validation

---

## 🎥 Demo Video

▶️ **Video DEMO Part1:** https://youtu.be/woDNxiDn04A
▶️ **Video DEMO Part2:** https://youtu.be/WM0uYmA7LYY 

- Shows both functions running
- Verifies queue message and SQL insert
- Explains project structure and code

---

## 🔗 GitHub Repository

**Public Repo:** https://github.com/mspanwar21/Azure-Function-App





