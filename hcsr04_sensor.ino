#define TRIG_PIN 9  // הפין לשליחת האות (TRIG)
#define ECHO_PIN 10 // הפין לקבלת האות (ECHO)

void setup() {
  Serial.begin(115200);
  
  pinMode(TRIG_PIN, OUTPUT); // הגדרת TRIG כיציאה
  pinMode(ECHO_PIN, INPUT);  // הגדרת ECHO כהכניסה
}

void loop() {
  // שלח פולס קצר ב-TRIG
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  // חכה עד שמתקבל אוד אקו
  long duration = pulseIn(ECHO_PIN, HIGH);
  
  // המר את הזמן למרחק (מהירות הקול = 343 מטר לשנייה)
  long distance = (duration / 2) * 0.0344;  // המר לזמן לשני כיוונים

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  delay(500);  // עיכוב קצר בין קריאות
}
