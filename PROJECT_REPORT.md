# Project Report: Task 1 — Simple Task List with Machine Learning

**Internship:** Slash Mark Machine Learning Internship  
**Project Track:** Machine Learning  
**Project Number:** 1 of 6  
**Difficulty:** Beginner  

---

## 1. Project Objective
The objective of this project is to build an interactive, command-line Task Management System in Python that integrates basic Machine Learning and Natural Language Processing (NLP) heuristics. The application enables users to manage daily tasks while utilizing a trained classification model to automatically predict task priorities based on textual task descriptions.

---

## 2. Key Modules & Implementation Details

### A. Data Persistence (`tasks.csv`)
- **Structure:** Two columns: `description` (task name/details) and `priority` (`High`, `Medium`, `Low`).
- **File I/O:** Uses Pandas `read_csv` and `to_csv` for seamless persistent storage across app sessions.

### B. Machine Learning Architecture
- **Feature Extraction (`CountVectorizer`):** Converts raw task description strings into a tokenized Bag-of-Words (BoW) frequency matrix.
- **Classification (`MultinomialNB`):** Applies Bayes' theorem with multinomial distribution assumptions to estimate the conditional probability of each priority class given the keywords in the description:
  $$P(\text{Priority} \mid \text{Keywords}) \propto P(\text{Priority}) \prod_{i} P(\text{word}_i \mid \text{Priority})$$
- **Dynamic Training Pipeline:** A Scikit-learn `Pipeline` chains the vectorizer and classifier. The model automatically retrains whenever tasks are added or deleted, enabling online learning from user habits.

### C. Heuristic Task Recommender
- Scans existing tasks and recommends high-urgency tasks first (`High` $\rightarrow$ `Medium` $\rightarrow$ `Low`), ensuring critical responsibilities are highlighted before routine items.

---

## 3. Bug Fixes & Code Improvements

During development, the following foundational issues in the starter template were resolved:
1. **Index KeyError in Task Recommendation:**
   - *Problem:* Calling `random.choice()` on a filtered Pandas Series accessed indices by label instead of positional offset, causing `KeyError: 1`.
   - *Resolution:* Converted the Pandas Series to a native Python list using `.tolist()`.
2. **Variable Scope Error in Task Removal:**
   - *Problem:* Assigning `tasks` inside `remove_task()` without declaring `global tasks` raised an `UnboundLocalError`.
   - *Resolution:* Declared `global tasks` and added case-insensitive matching.
3. **Syntax Anomaly:**
   - *Problem:* A rogue numeric literal `4` existed on line 63.
   - *Resolution:* Removed the stray character and sanitized the main loop structure.
4. **Integration of ML Pipeline:**
   - *Problem:* The starter template imported and instantiated `MultinomialNB`, but never connected it to the user workflow.
   - *Resolution:* Integrated `predict_priority()` to auto-suggest priorities when adding new tasks, allowing users to accept the recommendation with a single keystroke.

---

## 4. Test Results & Verification

| Test Case | Input | Expected Output | Status |
| :--- | :--- | :--- | :--- |
| **List Tasks** | Choice `3` | Displays all tasks in tabular form with 1-based index | **PASSED** |
| **ML Prediction (High)** | "Pay electricity bill" | Predicts `High` priority based on keyword *"bill"* | **PASSED** |
| **ML Prediction (Medium)** | "Prepare presentation for team" | Predicts `Medium` priority based on *"presentation"* | **PASSED** |
| **ML Prediction (Low)** | "Schedule meeting with team" | Predicts `Low` priority based on *"schedule"* | **PASSED** |
| **Remove Task** | "Exercise" | Deletes row from dataframe and updates `tasks.csv` | **PASSED** |
| **Recommend Task** | Choice `4` | Returns a random High-priority task | **PASSED** |
| **Exit** | Choice `5` | Gracefully terminates and saves changes | **PASSED** |

---

## 5. Conclusion
Project 1 demonstrates end-to-end Python software development, covering file persistence, robust error handling, command-line interface design, and real-time Machine Learning text classification.

