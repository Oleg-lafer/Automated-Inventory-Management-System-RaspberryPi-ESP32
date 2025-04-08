#include "HX711.h"

// הגדרת הפינים של ה-HX711
#define DOUT  4  // Pin for data output
#define CLK   5  // Pin for clock

HX711 scale;

void setup() {
  Serial.begin(115200);
  
  // אתחול ה-HX711
  scale.begin(DOUT, CLK);
  
  // חכות עד שהחיישן יתייצב
  Serial.println("Initializing...");
  delay(1000);
}

void loop() {
  // בודק אם יש נתונים לחיישן
  if (scale.is_ready()) {
    long weight = scale.get_units(10);  // קבלת משקל ממוצע מתוך 10 קריאות
    Serial.print("Weight: ");
    Serial.println(weight);  // מציג את המשקל ב-SERIAL MONITOR
  } else {
    Serial.println("HX711 not found.");
  }
  
  delay(500);  // עיכוב קצר בין קריאות
}
