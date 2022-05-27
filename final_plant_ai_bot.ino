#include <Arduino.h>
#include <DHT.h>

//ldr
const int ldrPin = 35; // analog pin

//dht11
#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

#define DEVICE_UID "1X"

//soil moisture
int sensorPin = 33; 
int sensorValue; 


void setup() {
  //soil
  Serial.begin(115200);
  
  //ldr
  pinMode(ldrPin, INPUT);

  //dht11
  dht.begin();
  
}

void loop() {
  //soil
  sensorValue = analogRead(sensorPin); 
  //Serial.println("Analog Value : ");
  Serial.println(sensorValue);
  //delay(10000);//1000

  //ldr
  int ldrStatus = analogRead(ldrPin);
  Serial.println(ldrStatus);
  /*if (ldrStatus <= 200) {
    Serial.print("Darkness over here,turn on the LED :");
    Serial.println(ldrStatus);
  }
  else {
    Serial.println(ldrStatus);
  */
  

  //dht11
  //delay(10000);//2000
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  float hi = dht.computeHeatIndex(f, h);
  //Serial.print("Humidity: "); 
  Serial.print(h);
  Serial.print(" %\n");
  //Serial.print("Temperature: "); 
  Serial.print(t);
  Serial.print(" *C\n ");
  Serial.print(f);
  Serial.print(" *F\n");
  //Serial.print("Heat index: ");
  Serial.print(hi);
  Serial.println(" *F");
  delay(10000);//not mentioned
  }
