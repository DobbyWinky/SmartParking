int buzzer = 9;

int triggerPin1 = 7; //triggering on pin 7

int echoPin1 = 8; //echo on pin 8

int triggerPin2 = 5; //triggering on pin 7

int echoPin2 = 6; //echo on pin 8

void setup()
{

  Serial.begin(9600); //we'll start serial comunication, so we can see the distance on the serial monitor Serial.println("Tech Ponder's UltraSonic Sensor Tutorial");

  pinMode(triggerPin1, OUTPUT); //defining pins

  pinMode(echoPin1, INPUT);

  pinMode(triggerPin2, OUTPUT); //defining pins

  pinMode(echoPin2, INPUT);

  digitalWrite(buzzer, LOW);
}


int status1 = 1;
int status2 = 1;


void loop()

{ int duration1, distance1, duration2, distance2; //Adding duration and distance

  digitalWrite(triggerPin1, HIGH); //triggering the wave(like blinking an LED)

  delay(10);

  digitalWrite(triggerPin1, LOW);

  duration1 = pulseIn(echoPin1, HIGH); //a special function for listening and waiting for the wave

  distance1 = (duration1 / 2) / 29.1; //transforming the number to cm(if you want inches, you have to change the 29.1 with a suitable number

  delay(1000);


  digitalWrite(triggerPin2, HIGH); //triggering the wave(like blinking an LED)

  delay(10);

  digitalWrite(triggerPin2, LOW);

  duration2 = pulseIn(echoPin2, HIGH); //a special function for listening and waiting for the wave

  distance2 = (duration2 / 2) / 29.1; //transforming the number to cm(if you want inches, you have to change the 29.1 with a suitable number

  delay(1000);

  //

//  Serial.print("\n S1 :"); //just printing to a new line
//
//  Serial.print(distance1); //printing the numbers
//
//  Serial.print("cm"); //and the unit
//
//  Serial.print("\n S2 : "); //just printing to a new line

//  Serial.print(distance2); //printing the numbers
//
//  Serial.print("cm"); //and the unit

  if (distance1 < 5 && status1 != 0)

  {
    status1 = 0;
    Serial.println("5 0&");

  }
  else if (distance1 >= 5 && status1 == 0)
  {
    status1 = 1;
    Serial.println("5 1&");
  }
  else
  {
    
  }

  if (distance2 < 5 && status2 != 0)

  {
    status2 = 0;
    Serial.println("6 0&");

  }
  else if (distance2 >= 5 && status2 == 0)
  {
    status2 = 1;
    Serial.println("6 1&");
  }
  else
  {
    
  }

  //digitalWrite(buzzer,LOW);

}
