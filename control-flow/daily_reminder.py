task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound =input("Is it time-bound? (yes/no):")
match priority:
    case "high":
        reminder = f" '{task}' is a high priority task "
    case "medium":
        reminder = f"'{task}' is a medium priority task "
    case "low":
        reminder = f" '{task}' is a low priority task. "
if time_bound == "yes":
    reminder+="that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    reminder+="Consider completing it at your convenience."
    print(f"Note: {reminder}")