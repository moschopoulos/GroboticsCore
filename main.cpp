#include <Arduino.h>
 
//int ledPin =  13;    // LED connected to digital pin 13
int analoguePin = 0;
 
void setup() 
{
  Serial.begin(9600); 
  pinMode(analoguePin, INPUT);
}
 
void loop() 
{
  int val = 0;
  val = analogRead(analoguePin);   
  Serial.println(val);
  delay(500);                   // wait for a 1/2 second
}
 
int main(void) 
{
  init();
  setup();
  bool running = true;
  while(running) 
  {
    loop();
  }
}


