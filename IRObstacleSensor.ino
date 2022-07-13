String in, out;
int total = 0;

void setup() {
  pinMode(8, INPUT);
  pinMode(7, INPUT);
  Serial.begin(9600);
}

void show() {
  Serial.println(total);
    //Serial.println("");
}
void loop() {
  if (digitalRead(7) == LOW) {
    while (digitalRead(8) == HIGH) {
    }
    analogWrite(A1, 255);
    //Serial.print("Person entered there are ");
    total++;
    show();
    delay(1000);  
    analogWrite(A1, 0);
  } else if (digitalRead(8) == LOW) {
    while (digitalRead(7) == HIGH) {
    }
    analogWrite(A0, 255);
    //Serial.print("Person exited there are ");
    total--;
    show();
    delay(1000);
    analogWrite(A0, 0);
  }
}
