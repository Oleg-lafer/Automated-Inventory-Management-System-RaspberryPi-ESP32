import serial
import time
import subprocess
import os

# הגדר את הפורט הסדרתי ב-Raspberry Pi
PORT = "/dev/ttyUSB0"  # The detected port
BAUD_RATE = 115200
last_value = None
START = None  # משתנה שיכיל את הערך ההתחלתי

# הגדרת הנתיב לסביבה הווירטואלית
VENV_PATH = "/home/daniel/PycharmProjects/WMS/venv_name"

# פונקציה להפעלת צילום התמונה
def capture_image():
    print("🚀 מתחילים את צילום התמונה...")
    try:
        subprocess.run(["python3", "capture_image.py"], check=True)
        print("📸 התמונה צולמה בהצלחה!")
        
        # לאחר צילום התמונה, נפעיל את החיזוי בסביבה הווירטואלית
        run_predict_script()
    except subprocess.CalledProcessError as e:
        print(f"❌ שגיאה בצילום התמונה: {e}")

# פונקציה להפעלת זיהוי התמונה בתוך הסביבה הווירטואלית
def run_predict_script():
    print("🚀 מתחילים את חיזוי התמונה בסביבה הווירטואלית...")

    # יצירת נתיב לפייתון בסביבה הווירטואלית
    python_path = os.path.join(VENV_PATH, "bin", "python3")

    try:
        subprocess.run([python_path, "predict_image.py"], check=True)
        print("✅ חיזוי התמונה הושלם!")
    except subprocess.CalledProcessError as e:
        print(f"❌ שגיאה בחיזוי התמונה: {e}")
        return False
    return True

# חיבור ל-ESP32 והתחלת קריאה
try:
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    print("מתחברים ל-ESP32 לקריאת משקל...")

    while True:
        line = ser.readline().decode().strip()
        if line:
            print(f"🔔 נתון חדש שהתקבל: {line}")  # הדפסת הנתונים שהתקבלו
            try:
                value = int(line)

                if START is None:
                    # שמור את הערך ההתחלתי
                    START = value
                    last_value = value  # נשמור גם את הערך האחרון
                    print(f"✅ ערך התחלתי נקבע: {START}")
                    continue

                # חישוב השינוי בערך
                change = abs(value - last_value)
                print(f"⚖️ שינוי בחיישן: {change}")  # הדפסת השינוי בין הערכים

                if change > 1000:  # אם השינוי מעל 1000
                    print(f"⚠️ שינוי מעל 1000: {change}")
                    capture_image()  # הפעלת צילום התמונה רק אם השינוי מעל סף מסוים
                last_value = value  # עדכון הערך האחרון

            except ValueError:
                continue

except serial.SerialException:
    print("⚠️ שגיאה: לא ניתן להתחבר ל-Arduino.")
except KeyboardInterrupt:
    print("\n💡 יציאה מהתוכנית.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
