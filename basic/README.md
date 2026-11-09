# Task 1: Simple Task Management App with Machine Learning

**Slash Mark Machine Learning Internship — Project 1**

---

## 📌 Project Overview
The **Simple Task List** is a Python-based command-line task management application that integrates **Machine Learning (Natural Language Processing & Naive Bayes)** to automatically predict and recommend task priorities based on their descriptions. It allows users to add, remove, view, and prioritize tasks while persisting everything into a `tasks.csv` file.

---

## 🚀 Key Features

1. **Add Task with ML Priority Prediction**:
   - Uses a trained **Multinomial Naive Bayes** text classification model.
   - When you enter a task description (e.g., *"Pay electricity bill"*), the ML model automatically analyzes the keywords and predicts its priority (**High**, **Medium**, or **Low**).
   - The user can either press **Enter** to accept the ML recommendation or enter a custom priority.

2. **Remove Task**:
   - Easily remove a task by specifying its description (case-insensitive).
   - Updates the dataset and immediately retrains the ML model.

3. **List Tasks**:
   - Neatly formats and displays all existing tasks, their index numbers, and priority levels.

4. **Recommend Urgent Task**:
   - Intelligent heuristic that scans tasks by urgency (**High ➔ Medium ➔ Low**) and recommends which task to tackle first.

5. **Persistent Storage (File I/O)**:
   - All tasks are saved automatically to `tasks.csv`, ensuring tasks persist across sessions.

---

## 🛠️ Prerequisites & Installation

### 1. Prerequisites
- Python 3.8+ (Python 3.12 verified)
- `pip` package manager

### 2. Install Required Dependencies
```powershell
pip install -r requirements.txt
```
*(Or manually: `pip install pandas scikit-learn`)*

---

## 💻 How to Run

```powershell
python main.py
```

