import cv2
import numpy as np
import tensorflow as tf

# טעינת המודל
model = tf.keras.models.load_model("vegetable_classifier.keras")

# הגדרת מפת התוויות
label_map = {"Carrot": 0, "Cucumber": 1, "Potato": 2, "Tomato": 3}

def preprocess_image(image_path):
    """מעבד את התמונה כך שתתאים למודל."""
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ לא ניתן לקרוא את התמונה: {image_path}")
        return None

    # שינוי גודל התמונה
    img = cv2.resize(img, (75, 75))
    
    # נרמול
    img = img.astype(np.float32) / 255.0
    
    # הוספת ממד נוסף כדי להתאים לפורמט של המודל
    img = np.expand_dims(img, axis=0)

    return img


def predict_image(image_path, label_map, model):
    """מבצע חיזוי על התמונה שנמסרה."""
    img = preprocess_image(image_path)
    if img is None:
        return

    prediction = model.predict(img)[0]

    # מיון התוצאות מההתאמה הגבוהה לנמוכה
    top_indices = np.argsort(prediction)[::-1][:3]

    # הדפסת הזיהוי העיקרי
    predicted_label = list(label_map.keys())[top_indices[0]]
    print(f"✅ התווית החזויה: {predicted_label}")

    # הדפסת שלושת ההתאמות המובילות עם ציוני ההתאמה שלהם
    print("🔍 שלושת ההתאמות המובילות:")
    for i in top_indices:
        vegetable_name = list(label_map.keys())[i]
        confidence_score = prediction[i]
        print(f"{vegetable_name}: {confidence_score:.4f}")
    print("-" * 40)


if __name__ == "__main__":
    # ספק כאן את הנתיב של התמונה שברצונך לחזות עליה
    image_path = "image.jpg"
    if image_path:
        predict_image(image_path, label_map, model)
