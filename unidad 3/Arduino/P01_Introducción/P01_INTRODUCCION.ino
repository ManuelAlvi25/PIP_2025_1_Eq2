
int led = 13;
void setup() {
  // put your setup code here, to run once:
 pinMode(led,OUTPUT);
 // input > sensores
 //output > actuadores
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(led,1);// 1,true,high (puede ser una de esas)
Delay(500);
digitalWrite(led,0);
delay(500);
}
