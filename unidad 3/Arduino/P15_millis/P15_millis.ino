long m;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  m= millis();
 int nm= m/1000;
  Serial.println(String(m)+" "+ String(nm));
  delay(1000);

}


//ejercicio 4 , prender apagar usando millis con leds. sin delays