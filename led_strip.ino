int green_led=3,red_led=5,blue_led=6;
int speed_time=1000;

int inPin = A0;         // the number of the input pin

int state = HIGH;      // the current state of the output pin
int reading;           // the current reading from the input pin
int previous = LOW;    // the previous reading from the input pin

// the follow variables are long's because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
long time = 0;         // the last time the output pin was toggled
long debounce = 200;   // the debounce time, increase if the output flickers

void setup() {
  // put your setup code here, to run once:
  pinMode(green_led,OUTPUT);
  pinMode(red_led,OUTPUT);
  pinMode(blue_led,OUTPUT);
  Serial.begin(9600);
  analogWrite(green_led,0); 
  analogWrite(red_led,255); 
  analogWrite(blue_led,0); 
  randomSeed(analogRead(1));
}

void loop() {
  // if there's any serial available, read it:
    while (Serial.available() > 0) {
  
      // look for the next valid integer in the incoming serial stream:
      int red = Serial.parseInt();
      // do it again:
      int green = Serial.parseInt();
      // do it again:
      int blue = Serial.parseInt();
  
      // look for the newline. That's the end of your sentence:
      if (Serial.read() == '\n') {
  
        // fade the red, green, and blue legs of the LED:
        analogWrite(red_led, red);
        analogWrite(green_led, green);
        analogWrite(blue_led, blue);
  
        // print the three numbers in one string as hexadecimal:
        Serial.print(red, HEX);
        Serial.print(green, HEX);
        Serial.println(blue, HEX);
      }
    }

}
