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

## 🧠 Machine Learning Explanation

### Pipeline Architecture:
```
Task Description (Text)
          │
          ▼
CountVectorizer (Tokenization & Word Frequency Matrix)
          │
          ▼
Multinomial Naive Bayes Classifier (MultinomialNB)
          │
          ▼
Predicted Priority ('High' | 'Medium' | 'Low')
```

- **`CountVectorizer`**: Converts words from task descriptions into numerical frequency vectors (Bag of Words representation).
- **`MultinomialNB`**: Calculates probabilities for each priority class based on word occurrences (e.g., words like *"bill"*, *"pay"*, *"urgent"* strongly correlate with *"High"* priority; words like *"meeting"*, *"call"* correlate with *"Medium"* or *"Low"*).
- **Continuous Learning**: Every time a user adds or removes a task, `train_model()` updates the ML pipeline with the latest data.

---

## 🛠️ Prerequisites & Installation

### 1. Prerequisites
- Python 3.8+ (Python 3.12 verified)
- `pip` package manager

### 2. Install Required Dependencies
Open PowerShell or Command Prompt in this project directory and run:

```powershell
pip install -r requirements.txt
```
*(Or manually: `pip install pandas scikit-learn`)*

---

## 💻 How to Run

1. Open PowerShell / Terminal in the project folder:
   ```powershell
   cd C:\Users\shilpav\Desktop\MtechIntership\basic
   ```

2. Run the application:
   ```powershell
   python main.py
   ```

---

## 📖 Step-by-Step Usage Guide

### Menu Options:
```text
==============================
     Task Management App
==============================
1. Add Task
2. Remove Task
3. List Tasks
4. Recommend Task
5. Exit
```

### Example Test Scenarios:

#### 1. Adding a Task (Testing ML Prediction):
```text
Select an option (1-5): 1
Enter task description: Pay internet bill
-> ML Predicted Priority: High
Enter task priority (Low/Medium/High) [Press Enter for 'High']: [Press Enter]
Task added successfully with High priority.
```

#### 2. Listing Tasks:
```text
Select an option (1-5): 3

--- Current Task List ---
                            description priority
1                         Buy groceries     High
2               Complete project report   Medium
3      Schedule a meeting with the team      Low
4  Prepare presentation for the meeting   Medium
5                         Pay the bills     High
6                              Exercise      Low
7                     Pay internet bill     High
```

#### 3. Getting a Recommendation:
```text
Select an option (1-5): 4

Recommended task: Pay the bills - Priority: High
```

#### 4. Removing a Task:
```text
Select an option (1-5): 2
Enter task description to remove: Exercise
Task removed successfully.
```

#### 5. Exiting:
```text
Select an option (1-5): 5
Goodbye! Your tasks are saved.
```

---

## 📂 Project Structure

```text
basic/
├── main.py              # Main Python application with menu & ML pipeline
├── tasks.csv            # Persistent dataset of tasks and priorities
├── requirements.txt     # Python package requirements (pandas, scikit-learn)
├── instructions.txt     # Original instructions provided by Slash Mark
└── README.md            # Comprehensive project documentation
```

---

## 📤 Slash Mark Submission Steps

1. **Verify Execution**: Ensure `python main.py` runs without errors in your terminal.
2. **Push to GitHub**:
   - Create a GitHub repository (e.g. `SlashMark-ML-Task1-SimpleTaskList`).
   - Run:
     ```powershell
     git init
     git add .
     git commit -m "Complete Task 1: Simple Task List with ML Priority Classifier"
     git branch -M main
     git remote add origin https://github.com/<your-username>/<repo-name>.git
     git push -u origin main
     ```
3. **Capture Proof**:
   - Take screenshots of your terminal showing the app running, adding a task, showing ML prediction, listing tasks, and recommending a task.
4. **Submit on Portal**:
   - Click the **Submit Project** button on your Slash Mark portal and paste your GitHub repository link and screenshots.

