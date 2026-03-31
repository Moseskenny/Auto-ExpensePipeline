# 🚀 Automated Expense Processing Pipeline

### *(Python + Jenkins + Google Drive API)*



## 📌 Overview

This project is a **fully automated expense processing pipeline** designed to simulate a real-world data engineering workflow.

It continuously monitors incoming data, transforms raw financial records into a structured format, and uploads the results to the cloud — all without manual intervention.

The goal of this project was to:

* Build a **practical automation system**
* Handle **messy real-world data**
* Implement a **CI/CD-style pipeline using Jenkins**
* Integrate securely with external APIs (Google Drive)

---

## 💡 Why This Project?

In real-world scenarios, organizations deal with:

* Unstructured or inconsistent data (CSV files)
* Repetitive manual processing (Excel formatting, categorization)
* Risk of human error in financial tracking

This project solves those problems by:

✔ Automating the entire workflow
✔ Cleaning and standardizing input data
✔ Ensuring consistency in output format
✔ Reducing manual effort to near zero

It mimics how **data pipelines in production systems** operate — making it highly relevant for roles in:

* Data Engineering
* Backend Development
* DevOps / Automation

---

## Demo:

![Animation](https://github.com/user-attachments/assets/0fbe49ef-33a5-46ff-9654-68e41d22eff4)

---


## ⚙️ How It Works (Pipeline Flow)

```
📥 Inbox Folder (CSV Input)
        ↓
🧠 Python Processing Engine
        ↓
📊 Structured Excel Output
        ↓
☁️ Google Drive Upload
        ↓
📦 Archive (Processed Files)
```

---

## 🔄 Step-by-Step Workflow

### 1. 📂 File Detection

* Jenkins runs the pipeline on a scheduled trigger (cron-based)
* The system scans the `inbox/` directory
* Identifies the **latest folder containing CSV data**

---

### 2. 🧹 Data Processing

* Reads raw CSV using **Pandas**
* Handles inconsistent data formats:

  * Fixes corrupted or invalid date formats
  * Standardizes categories using a mapping config
* Extracts:

  * Date
  * Transaction Type (Income / Expense)
  * Category
  * Amount
  * Notes

---

### 3. 📅 Smart Date Handling

* Preserves:

  * Day
  * Year
* Replaces:

  * Month → with **current system month**
* Ensures valid and consistent date formatting across all records

---

### 4. 📊 Excel Generation

* Uses a pre-defined **Excel template**
* Writes processed data starting from row 9
* Automatically fills:

  * **Cell F5 → Current Month (e.g., March)**

---

### 5. ☁️ Cloud Upload

* Uploads generated Excel file to **Google Drive**
* Uses **OAuth 2.0 authentication**
* Securely manages access via `token.pickle`

---

### 6. 🧼 Cleanup & Archival

* Moves processed CSV file to `processed/`
* Deletes local Excel file after successful upload
* Ensures no duplicate or redundant data

---

## 🧰 Tech Stack

### 🐍 Backend & Processing

* Python
* Pandas (data transformation)
* OpenPyXL (Excel handling)

### ⚙️ Automation

* Jenkins (CI/CD pipeline scheduling)

### ☁️ Cloud Integration

* Google Drive API
* OAuth 2.0 Authentication

### 🗂️ File Handling

* OS / Shutil (file operations & archiving)

---

## 📁 Project Structure

```
Expense-pipeline/
│
├── scripts/
│   ├── main.py
│   ├── processor.py
│   ├── uploader.py
│
├── inbox/          # Incoming CSV folders
├── outbox/         # Generated Excel files
├── processed/      # Archived CSV files
│
├── templates/
│   └── master_template.xlsx
│
├── configs/
│   └── mapping.json
│
├── .gitignore
└── README.md
```

---

## 🔐 Security Considerations

To protect sensitive data:

❌ The following are NOT included in this repository:

* Real financial data
* `credentials.json`
* `token.pickle`

✔ Instead:

* Dummy/sample data is used
* A placeholder credentials file is provided

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone <your-repo-link>
cd Expense-pipeline
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Add your Google Drive credentials

* Place your `credentials.json` in the project root
* Run authentication once to generate `token.pickle`

---

### 4. Run manually

```
python scripts/main.py
```

---

### 5. Run with Jenkins

* Configure a pipeline job
* Add cron trigger:

```
H/1 * * * *
```

---

## ✨ Key Features

* 🔄 Fully automated pipeline (no manual intervention)
* 🧠 Handles messy and inconsistent data gracefully
* 📊 Template-based Excel generation
* ☁️ Seamless Google Drive integration
* 📦 Clean file lifecycle management
* 🔐 Secure handling of credentials

---

## 🚀 Future Improvements

* Real-time file detection (using watchdog instead of cron)
* Multi-file batch processing
* Logging system with status tracking
* Cloud deployment (AWS / GCP)
* Dashboard for monitoring pipeline activity

---

## 📣 Final Thoughts

This project goes beyond a simple script — it demonstrates:

* End-to-end pipeline design
* Automation mindset
* Real-world data handling
* Secure API integration

It reflects how modern systems process, transform, and move data at scale.

---

## 🔗 Connect

If you found this interesting or have suggestions, feel free to connect!

LinkedIn: https://www.linkedin.com/in/moses-kenny/

---

## 📜 License

This project is licensed under the MIT License.

You are free to:

Use
Modify
Distribute

With proper attribution.

---

⭐ If you like this project

Give it a star ⭐ on GitHub — it helps a lot!

