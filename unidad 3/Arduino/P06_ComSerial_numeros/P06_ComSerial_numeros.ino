int v;

void setup() {
 v = 0;
 Serial.begin(9600);
}

void loop() {
  
 Serial.println("valor" + String(v));
 v += 1;
 delay(100);


}