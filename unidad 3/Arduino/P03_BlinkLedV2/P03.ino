
int led = 13;
int dEncendido = 1000;
int dApagado =500;
void setup() {
  // put your setup code here, to run once:
 pinMode(led,OUTPUT);
 // input > sensores
 //output > actuadores
}

void loop() {
  // put your main code here, to run repeatedly:
 digitalWrite(led,1);
 delay(dEncendido);
 digitalWrite(led,0);
 delay(dApagado);
}
