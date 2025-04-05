import subprocess
import time
import os

# שם הסביבה הווירטואלית שלך
VENV_PATH = "/home/daniel/PycharmProjects/PythonProject/venv_name"

# פונקציה להפעלת צילום התמונה בסביבה הכללית
def run_capture_script():
    print("🚀 מתחילים את צילום התמונה בסביבה הכללית...")
    try:
        subprocess.run(["python3", "capture_image.py"], check=True)
        print("📸 התמונה צולמה בהצלחה!")
    except subprocess.CalledProcessError as e:
        print(f"❌ שגיאה בצילום התמונה: {e}")
        return False
    return True

# פונקציה להפעלת קריאת החיישן מה-ESP32
def run_esp32_reader():
    print("🔌 מתחברים ל-ESP32 לקריאת משקל...")
    try:
        esp_process = subprocess.Popen(["python3", "esp32_hx711_reader.py"])
        return esp_process
    except Exception as e:
        print(f"❌ שגיאה בקריאת ESP32: {e}")
        return None

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

# הפעלת התהליך בסדר הנכון עם תנאי שינוי משמעותי של 1000
def sync_process():
    # התחלת חיישן ESP32 (רץ ברקע)
    esp_process = run_esp32_reader()
    if esp_process:
        print("✅ חיישן ESP32 מופעל ברקע.")
    
    # חיבור לחיישן כדי לקבל נתונים, ויש לשמור את הערך הראשון
    start_value = None
    while start_value is None:
        line = esp_process.stdout.readline().decode().strip()  # קריאת ערך מהחיישן
        if line:
            try:
                start_value = int(line)
                print(f"✅ ערך התחלתי נקבע: {start_value}")
            except ValueError:
                continue
    
    # המרת השינוי בתנאי
    prev_value = start_value
    while True:
        line = esp_process.stdout.readline().decode().strip()
        if line:
            try:
                current_value = int(line)
                if abs(current_value - prev_value) >= 1000:  # שינוי משמעותי של 1000 יחידות
                    print(f"⚖️ שינוי בחיישן: {abs(current_value - prev_value)}")
                    if run_capture_script():  # צילום התמונה
                        time.sleep(1)  # המתנה קצרה לוודא שהתמונה נשמרה

                        # חיזוי תמונה
                        if run_predict_script():
                            print("✅ כל התהליך הושלם בהצלחה!")
                        else:
                            print("❌ הייתה בעיה במהלך חיזוי התמונה.")
                    prev_value = current_value
            except ValueError:
                continue

    # סיום חיישן ה-ESP32
    if esp_process:
        print("🛑 סוגרים את תהליך ה-ESP32...")
        esp_process.terminate()
        esp_process.wait()
        print("✅ תהליך ה-ESP32 נסגר בהצלחה.")

if __name__ == "__main__":
    sync_process()
