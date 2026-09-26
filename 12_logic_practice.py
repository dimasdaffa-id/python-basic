score = 80
attendance = 85
has_project = True

if score >= 75:
    if attendance >= 80:
        if has_project:
            print("Student passed!")
        else:
            print("Project required.")
    else:
        print("Attendance too low.")

else:
    print("Score too low.")