import time

print("QuickHealth Pro Max – Interactive Symptom Checker")
time.sleep(1)
print("\n👋 Hello there! Let's check how you're doing today.")
time.sleep(1)

# 👤 1. We need to ask for user profile inouts
print("\n👤 Personal Details")
name = input("Your name: ").strip()
while len(name) == 0:
    print("Error: Name cannot be empty!")
    name = input("Your name: ").strip()

age = input("Age: ").strip()
while not age.isdigit():
    print("Error: Age must be a number!")
    age = input("Age: ").strip()
age = int(age)

gender = input("Gender (male/female/other): ").lower().strip()
while gender not in ["male", "female", "other"]:
    print("Error: Please choose exactly one from: male/female/other")
    gender = input("Gender (male/female/other): ").lower().strip()

city = input("📍 Your city (for nearby care suggestions): ").strip()
while len(city) == 0:
    print("Error: City cannot be empty!")
    city = input("📍 Your city: ").strip()

# 🤒 2. We need to ask for health inputs 
print("\n🤒 Symptoms & Health Info")
print("Select all symptoms you're experiencing (comma separated):")
print("Available options: fever, cough, fatigue, headache, chest pain, breathlessness")
all_symptoms = input("> ").lower().strip()
all_symptoms = [s.strip() for s in all_symptoms.split(",")]