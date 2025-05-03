import time

print("QuickHealth Pro Max – Interactive Symptom Checker")
time.sleep(3)

print("\n👋 Hello there! Let's check how you're doing today.")
time.sleep(3)

# 👤 We need to ask user for personal details
print("\n👤 Personal Details")
name = input("Your name: ").strip()
if len(name) == 0:
    print("Error: Name cannot be empty!")
    name = input("Your name: ").strip()

age = input("Age: ").strip()
if age.isdigit():
    age = int(age)
else:
    print("Error: Age must be a number!")
    age = input("Age: ").strip()
    if age.isdigit():
        age = int(age)

gender = input("Gender (male/female/other): ").strip().lower()
if gender != "male" and gender != "female" and gender != "other":
    print("Error: Please choose exactly one from: male/female/other")
    gender = input("Gender (male/female/other): ").strip().lower()

city = input("📍 Your city (for nearby care suggestions): ").strip()
if len(city) == 0:
    print("Error: City cannot be empty!")
    city = input("📍 Your city: ").strip()

time.sleep(3)

# 🤒 2. We need to ask for health inputs 
print("\n🤒 Symptoms & Health Info")
print("Select all symptoms you're experiencing (comma separated):")
print("Options: fever, cough, fatigue, headache, chest pain, breathlessness")
all_symptoms = input("Your symptoms: ").strip().lower()

has_fever = "fever" in all_symptoms
has_cough = "cough" in all_symptoms
has_fatigue = "fatigue" in all_symptoms
has_headache = "headache" in all_symptoms
has_chest_pain = "chest pain" in all_symptoms
has_breathlessness = "breathlessness" in all_symptoms

valid_found = has_fever or has_cough or has_fatigue or has_headache or has_chest_pain or has_breathlessness

if valid_found == False:
    print("Error: Please enter at least one valid symptom")
    all_symptoms = input("Your symptoms: ").strip().lower()

# now we need to ask the most troubling symptom
print("\nYou entered: " + all_symptoms)
print("Which one is the most troubling symptom?")
most_troubling = input("Choose one from your list: ").strip().lower()

if most_troubling != "fever" and most_troubling != "cough" and most_troubling != "fatigue" and most_troubling != "headache" and most_troubling != "chest pain" and most_troubling != "breathlessness":
    print("Error: Must choose one valid symptom")
    most_troubling = input("Most troubling symptom: ").strip().lower()

temp = input("🌡️ Body Temperature (°F): ").strip()
if temp.replace('.', '').isdigit():
    temp = float(temp)
else:
    print("Error: Temperature must be a number!")
    temp = input("🌡️ Body Temperature (°F): ").strip()
    if temp.replace('.', '').isdigit():
        temp = float(temp)

sick_days = input("📅 Days you've felt unwell: ").strip()
if sick_days.isdigit():
    sick_days = int(sick_days)
else:
    print("Error: Days must be a whole number!")
    sick_days = input("📅 Days you've felt unwell: ").strip()
    if sick_days.isdigit():
        sick_days = int(sick_days)

smoker = input("🚬 Do you smoke? (yes/no): ").strip().lower()
if smoker != "yes" and smoker != "no":
    print("Error: Please answer exactly 'yes' or 'no'")
    smoker = input("🚬 Do you smoke? (yes/no): ").strip().lower()

sleep_hours = input("🛌 Hours of sleep last night: ").strip()
if sleep_hours.replace('.', '').isdigit():
    sleep_hours = float(sleep_hours)
else:
    print("Error: Hours must be a number!")
    sleep_hours = input("🛌 Hours of sleep last night: ").strip()
    if sleep_hours.replace('.', '').isdigit():
        sleep_hours = float(sleep_hours)

mood = input("🧠 Current Mood (calm/anxious/sad/irritable): ").strip().lower()
if mood != "calm" and mood != "anxious" and mood != "sad" and mood != "irritable":
    print("Error: Please choose exactly one from: calm/anxious/sad/irritable")
    mood = input("🧠 Current Mood: ").strip().lower()

conditions = input("Do you have any pre-existing conditions? (yes/no): ").strip().lower()
if conditions != "yes" and conditions != "no":
    print("Error: Please answer exactly 'yes' or 'no'")
    conditions = input("Pre-existing conditions? (yes/no): ").strip().lower()

time.sleep(3)

risk_score = 0

if most_troubling == "fever":
    if temp >= 102:
        risk_score = risk_score + 3
    if age >= 60 and temp >= 100:
        risk_score = risk_score + 2

if most_troubling == "cough":
    if sick_days >= 5:
        risk_score = risk_score + 2

if most_troubling == "fatigue":
    if age > 30:
        risk_score = risk_score + 2

if most_troubling == "headache":
    if temp > 100:
        risk_score = risk_score + 2

if most_troubling == "chest pain":
    risk_score = risk_score + 3

if most_troubling == "breathlessness":
    risk_score = risk_score + 4

if smoker == "yes":
    risk_score = risk_score + 2

if sleep_hours < 6:
    risk_score = risk_score + 1

if mood == "anxious" or mood == "sad" or mood == "irritable":
    risk_score = risk_score + 1

if conditions == "yes":
    risk_score = risk_score + 2

print("\n⚖️ Your Health Risk:")
time.sleep(3)

if risk_score <= 3:
    print("🟢 Low Risk: Your symptoms appear mild")
elif risk_score <= 6:
    print("🟠 Moderate Risk: You should take care of your health and consult with a good doctor")
else:
    print("🔴 High Risk: Please seek medical attention")

time.sleep(3)

print("\n💡 Personalized Health Advice:")

if gender == "female" and age >= 45:
    print("- Consider scheduling a health screening")

if gender == "male" and smoker == "yes":
    print("- Smoking increases health risks, consider quitting")

if gender == "male" and smoker == "no":
    print("- You are already doing good by not smoking!")

if sleep_hours < 6:
    print("- Aim for 7-9 hours of sleep for better health")

if mood == "anxious":
    print("- Please talk to your mother and you will be fine")

if conditions == "yes":
    print("- Monitor your pre-existing conditions closely")

print("- Nearest urgent care in " + city + ": Park Hospital")

time.sleep(3)

print("\n🧘 Mental Health Tip:")

if mood == "calm":
    print("- Please be positive!")
elif mood == "sad":
    print("- Please talk to your best friend")
elif mood == "anxious":
    print("- Please talk to your mother and you will be fine")
elif mood == "irritable":
    print("- Listen to your favorite music")

print("\nThank you for using QuickHealth Pro Max! Get well soon! ❤️")
