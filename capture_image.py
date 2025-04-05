from picamera2 import Picamera2
from time import sleep

# יצירת אובייקט מצלמה
camera = Picamera2()

# התחלת המצלמה
camera.start()

# המתנה של שנייה כדי לוודא שהמצלמה מוכנה
sleep(1)

# צילום תמונה ושמירתה
camera.capture_file("image.jpg")

print("התמונה נשמרה כ-image.jpg")

# סיום השימוש במצלמה
camera.stop()
