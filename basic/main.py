import os
import random
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# File to store tasks
CSV_FILE = 'tasks.csv'

# Initialize tasks DataFrame
tasks = pd.DataFrame(columns=['description', 'priority'])

# Load pre-existing tasks from CSV file (if any)
def load_tasks():
    global tasks
    if os.path.exists(CSV_FILE):
        try:
            tasks = pd.read_csv(CSV_FILE)
            if 'description' not in tasks.columns or 'priority' not in tasks.columns:
                tasks = pd.DataFrame(columns=['description', 'priority'])
        except Exception:
            tasks = pd.DataFrame(columns=['description', 'priority'])
    else:
        tasks = pd.DataFrame(columns=['description', 'priority'])

# Save tasks to CSV file
def save_tasks():
    tasks.to_csv(CSV_FILE, index=False)

# Global ML model pipeline
model = None

# Train or retrain the task priority classifier
def train_model():
    global model
    # MultinomialNB requires at least 2 distinct classes and at least 2 samples
    if not tasks.empty and tasks['priority'].nunique() >= 2 and len(tasks) >= 2:
        try:
            vectorizer = CountVectorizer()
            clf = MultinomialNB()
            model = make_pipeline(vectorizer, clf)
            model.fit(tasks['description'], tasks['priority'])
        except Exception:
            model = None
    else:
        model = None

# Predict priority for a given task description using ML
def predict_priority(description):
    if model is not None:
        try:
            return model.predict([description])[0]
        except Exception:
            pass
    # Basic heuristic fallback if ML model doesn't have enough classes yet
    desc_lower = description.lower()
    if any(k in desc_lower for k in ['urgent', 'important', 'immediately', 'bill', 'pay', 'exam', 'deadline', 'emergency']):
        return 'High'
    elif any(k in desc_lower for k in ['meet', 'meeting', 'report', 'presentation', 'call', 'discuss', 'project']):
        return 'Medium'
    return 'Low'

# Function to add a task to the list
def add_task(description, priority):
    global tasks
    new_task = pd.DataFrame({'description': [description], 'priority': [priority]})
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    save_tasks()
    train_model()

# Function to remove a task by description
def remove_task(description):
    global tasks
    # Case-insensitive match check
    matching = tasks[tasks['description'].str.strip().str.lower() == description.strip().lower()]
    if matching.empty:
        print(f"Task '{description}' not found in the list.")
        return False
    tasks = tasks[tasks['description'].str.strip().str.lower() != description.strip().lower()].reset_index(drop=True)
    save_tasks()
    train_model()
    print("Task removed successfully.")
    return True

# Function to list all tasks
def list_tasks():
    if tasks.empty:
        print("\nNo tasks available.")
    else:
        print("\n--- Current Task List ---")
        display_df = tasks.copy()
        display_df.index = display_df.index + 1
        print(display_df[['description', 'priority']].to_string())

# Function to recommend a task based on priority
def recommend_task():
    if tasks.empty:
        print("\nNo tasks available for recommendations.")
        return

    # Check for High, Medium, Low in order of urgency
    for level in ['High', 'Medium', 'Low']:
        matching = tasks[tasks['priority'] == level]
        if not matching.empty:
            random_task = random.choice(matching['description'].tolist())
            print(f"\nRecommended task: {random_task} - Priority: {level}")
            return

    # If non-standard priority labels exist
    random_task = random.choice(tasks['description'].tolist())
    print(f"\nRecommended task: {random_task}")

def main():
    load_tasks()
    train_model()

    while True:
        print("\n" + "="*30)
        print("     Task Management App")
        print("="*30)
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Recommend Task")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            description = input("Enter task description: ").strip()
            if not description:
                print("Task description cannot be empty!")
                continue

            # Use ML model to recommend/predict priority
            suggested_priority = predict_priority(description)
            print(f"-> ML Predicted Priority: {suggested_priority}")

            priority_input = input(f"Enter task priority (Low/Medium/High) [Press Enter for '{suggested_priority}']: ").capitalize().strip()
            if not priority_input:
                priority = suggested_priority
            elif priority_input in ['Low', 'Medium', 'High']:
                priority = priority_input
            else:
                print(f"Invalid priority entered. Defaulting to predicted priority: {suggested_priority}")
                priority = suggested_priority

            add_task(description, priority)
            print(f"Task added successfully with {priority} priority.")

        elif choice == "2":
            description = input("Enter task description to remove: ").strip()
            if description:
                remove_task(description)
            else:
                print("Task description cannot be empty!")

        elif choice == "3":
            list_tasks()

        elif choice == "4":
            recommend_task()

        elif choice == "5":
            print("Goodbye! Your tasks are saved.")
            break

        else:
            print("Invalid option. Please select a valid number between 1 and 5.")

if __name__ == "__main__":
    main()
