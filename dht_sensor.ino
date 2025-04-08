#include <DHT.h>

#define DHTPIN 4           // הפין אליו מחובר החיישן
#define DHTTYPE DHT11      // סוג החיישן (DHT11 או DHT22)

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  Serial.println("Initializing DHT sensor...");
}

void loop() {
  delay(2000);  // חכה 2 שניות בין קריאות

  float humidity = dht.readHumidity();    // קריאה ללחות
  float temperature = dht.readTemperature();  // קריאה לטמפרטורה ב-Celsius

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" °C");
  Serial.print("   Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");
}
