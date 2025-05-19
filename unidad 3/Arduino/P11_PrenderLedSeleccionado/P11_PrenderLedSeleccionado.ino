int index;

int led1 = 6;
int led2 = 7;
int led3 = 8;
int led4 = 9;
int led5 = 10;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);

}


void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){ // Devuelve cuantos bytes hay en el buffer de entrada
   index = Serial.readString().toInt();
   // suponiendo usuarios perfectos >.<

   digitalWrite(led1, index);
   digitalWrite(led2, index);
   digitalWrite(led3, index);
   digitalWrite(led4, index);
   digitalWrite(led5, index);
   
   
   switch(index){
    case 1:
       digitalWrite(led1, 1);
    case 2:
       digitalWrite(led2, 1);
    case 3:
       digitalWrite(led3, 1);
    case 4:
       digitalWrite(led4, 1);
    case 5:
       digitalWrite(led5, 1);
   
   }
   
  
   
   
   }
   delay(100); 
}
