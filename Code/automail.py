import yagmail
import os
import glob
import getpass


def get_latest_attendance_file():
    files = glob.glob(os.path.join("Attendance", "Attendance_*.csv"))
    if not files:
        return None
    return max(files, key=os.path.getmtime)


receiver = input("Enter receiver email: ").strip()
sender = input("Enter sender Gmail address: ").strip()
password = getpass.getpass("Enter Gmail app password: ")
body = "Attendance File"
filename = get_latest_attendance_file()

if not filename:
    print("No attendance file found in Attendance folder.")
else:
    try:
        yag = yagmail.SMTP(sender, password)
        yag.send(
            to=receiver,
            subject="Attendance Report",
            contents=body,
            attachments=filename,
        )
        print("Attendance email sent successfully.")
    except Exception as error:
        print("Failed to send attendance email:", error)

