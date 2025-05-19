
void setup() {
 Serial.begin(9600);
}

byte var = 0;

void loop() {
  var += 1;
 Serial.println(var);
 delay(100);
}
