print("🩺 QuickHealth Pro Max – Interactive Symptom Checker")
print("👋 Hello there! Let's check how you're doing today.")
print("👤 Personal Details")
name=input("Your name: ").title().strip()
age=int(input("Age: "))
Gender=input("Gender :").lower().strip()
if Gender=="male":
  print("⭕Male")
elif Gender=="female":
  print("⭕Female")
else:
  print("⭕Other")

city=input("City :").lower().strip()
if city=="newyork":
  print("Newyork")
elif city=="losAngeles":
  print("Los Angeles")
elif city=="phoenix":
  print("Phoenix")
elif city=="austin":
  print("Austin")
else:
  print("Chicago")

  print("🤒 Symptoms & Health Info")
print("Select all symptoms you're experiencing:")
print("Choose an option") 