//Project Name: Temperature control bot
//Serial communication configuration -  9600
// Open the serial monitor and set the baud rate to 9600 and see the temperature


int reading = 0;
int sensorPin = A0;

// initialize the library with the numbers of the interface pins


void setup() {
  // set up the LCD's number of columns and rows: 

   pinMode(7,OUTPUT);// IN1(Connect IN1 of motor driver to arduino pin 7)                
    pinMode(6,OUTPUT); // IN2(Connect IN2 of motor driver to arduino pin 6)               
    pinMode(5,OUTPUT); // IN3(Connect IN3 of motor driver to arduino pin 5)               
    pinMode(4,OUTPUT); // IN4(Connect IN4 of motor driver to arduino pin 4) 
  Serial.begin(9600);
}

void loop() 
{
 reading = analogRead(sensorPin);// A0 lm35
  int celsius = reading/2;
 
   Serial.println(celsius);
  
  if (celsius >35) {
  digitalWrite(7,LOW);
  digitalWrite(6,LOW);
  digitalWrite(5,LOW);
  digitalWrite(4,LOW);
  Serial.println("BOT OFF");
  } 
  
  else {
  digitalWrite(7,HIGH);
  digitalWrite(6,LOW);
  digitalWrite(5,HIGH);
  digitalWrite(4,LOW);
  Serial.println("BOT MOVE");
  }
  delay(500);
  
}
