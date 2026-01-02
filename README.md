# Python CI Pipeline with GitHub Actions
[![Python CI](https://github.com/ashirwads/CICD/actions/workflows/ci.yml/badge.svg)](https://github.com/ashirwads/CICD/actions/workflows/ci.yml)

This project demonstrates a simple and practical **Continuous Integration (CI) pipeline** using **GitHub Actions** for a Python application.

The pipeline automatically runs tests whenever code is pushed to the repository or a pull request is created.

---

## 🚀 What This Project Does

- Automatically runs tests using **PyTest**
- Triggers CI on every **push** and **pull request**
- Uses **GitHub Actions** with a Linux (Ubuntu) runner
- Installs dependencies and validates code automatically
- Fails the pipeline if tests do not pass

---

## 🧰 Tech Stack

- Python  
- PyTest  
- Git & GitHub  
- GitHub Actions  
- YAML  

---

## 📂 Project Structure

├── .github/
│   └── workflows/
│       └── ci.yml
├── calculator.py
├── test_calculator.py
├── requirements.txt
└── README.md
---

## ⚙️ How the CI Pipeline Works

1. Code is pushed to the GitHub repository  
2. GitHub Actions triggers the workflow  
3. A fresh Ubuntu virtual machine is provisioned  
4. Python is set up and dependencies are installed  
5. PyTest is executed automatically  
6. The workflow passes or fails based on test results  

---

## 🧪 Run Tests Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest




✅ CI Status

The CI pipeline runs automatically on every push to validate the code.


---

## ✅ What to do now (important)

1️⃣ Save the file  
2️⃣ Commit & push:

```bash
git add README.md
git commit -m "Update README with project details"
git push