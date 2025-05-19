
int led = 13;
void setup() {
  // put your setup code here, to run once:
 pinMode(led,OUTPUT);
 // input > sensores
 //output > actuadores
}

void loop() {
  // put your main code here, to run repeatedly:
delay(500);
digitalWrite(led,1);
delay(500);
digitalWrite(led,0);
}
