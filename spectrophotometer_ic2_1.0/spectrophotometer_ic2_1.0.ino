#include "AS726X.h"
AS726X sensor;
float v, b, g, y, o, r;

void setup() {
  sensor.begin();
}

void loop() {
  sensor.takeMeasurements();
  //sensor.printMeasurements();//Prints out all measurements (calibrated)
  v = sensor.getCalibratedViolet();
  b = sensor.getCalibratedBlue();
  g = sensor.getCalibratedGreen();
  y = sensor.getCalibratedYellow();
  o = sensor.getCalibratedOrange();
  r = sensor.getCalibratedRed();
  Serial.print(v); 
  Serial.print(" , ");
    Serial.print(b); 
  Serial.print(" , ");
    Serial.print(g); 
  Serial.print(" , ");
    Serial.print(y); 
  Serial.print(" , ");
    Serial.print(o); 
  Serial.print(" , ");
    Serial.println(r); 

  
}

