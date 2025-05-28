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

## ▶️ Run & Test Locally

### 1. Queue Function

**Run:**

```bash
func start
```

**Test:**

```bash
curl -X POST http://localhost:7071/api/HttpExample -H "Content-Type: application/json" -d '{"name": "Azure"}'
```

**Check:**

- Open Azure Storage Explorer
- Navigate to Queue: `outqueue`
- Confirm the message is present

---

### 2. SQL Function

**Run:**

```bash
func start
```

**Test:**

```bash
curl -X POST http://localhost:7071/api/hello -H "Content-Type: application/json" -d '{"name": "SQL Test"}'
```

**Check:**

- Azure Portal → SQL Database → Query Editor

```sql
SELECT * FROM dbo.ToDo WHERE title = 'SQL Test';
```

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





