// Code from https://dronesandrovs.wordpress.com/2012/11/24/how-to-control-a-brushless-motor-esc-with-arduino/
// We can learn how to connect the pins as well
// Note on the website the red wire from ESC is connected. 
// These do not need to be connected to the arduino (only ground) 

#include <Servo.h>
 
Servo esc;
//int throttlePin = 0;
 
void setup()
{
esc.attach(9);
}

// Connection right now moves it clockwise
void loop()
{
int throttle = analogRead(A0);
throttle = map(throttle, 0, 1023, 0, 179);
esc.write(throttle);
delay(500);cci
}
