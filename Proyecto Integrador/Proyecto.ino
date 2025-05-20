#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Pines del Joystick
const int VRx = A0;
const int VRy = A1;

// Pines de los pulsadores
const int buttonA = 2;
const int buttonB = 3;
const int buttonC = 10;
const int buttonD = 11;

// Pines de los LEDs
const int ledArriba = 4;
const int ledAbajo = 5;
const int ledIzquierda = 6;
const int ledDerecha = 7;
const int ledPulsadorA = 8;
const int ledPulsadorB = 9;
const int ledPulsadorC = A2;
const int ledPulsadorD = A3;

// LCD con dirección I2C
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Para evitar imprimir repetidamente lo mismo
String mensajeAnterior = "";

void setup() {
  Serial.begin(9600);

  lcd.init();
  lcd.backlight();
  lcd.clear();

  pinMode(VRx, INPUT);
  pinMode(VRy, INPUT);

  pinMode(buttonA, INPUT_PULLUP);
  pinMode(buttonB, INPUT_PULLUP);
  pinMode(buttonC, INPUT_PULLUP);
  pinMode(buttonD, INPUT_PULLUP);

  pinMode(ledArriba, OUTPUT);
  pinMode(ledAbajo, OUTPUT);
  pinMode(ledIzquierda, OUTPUT);
  pinMode(ledDerecha, OUTPUT);
  pinMode(ledPulsadorA, OUTPUT);
  pinMode(ledPulsadorB, OUTPUT);
  pinMode(ledPulsadorC, OUTPUT);
  pinMode(ledPulsadorD, OUTPUT);
}

void loop() {
  int xValue = leerPromedio(VRx);
  int yValue = leerPromedio(VRy);
  bool movimientoDetectado = false;

  if (yValue < 450) {
    mensaje("Arriba ↑");
    digitalWrite(ledArriba, HIGH);
    movimientoDetectado = true;
  } else if (yValue > 570) {
    mensaje("Abajo ↓");
    digitalWrite(ledAbajo, HIGH);
    movimientoDetectado = true;
  } else if (xValue < 450) {
    mensaje("Izquierda ←");
    digitalWrite(ledIzquierda, HIGH);
    movimientoDetectado = true;
  } else if (xValue > 570) {
    mensaje("Derecha →");
    digitalWrite(ledDerecha, HIGH);
    movimientoDetectado = true;
  }

  if (digitalRead(buttonA) == LOW) {
    mensaje("Pulsador A");
    digitalWrite(ledPulsadorA, HIGH);
    movimientoDetectado = true;
  }

  if (digitalRead(buttonB) == LOW) {
    mensaje("Pulsador B");
    digitalWrite(ledPulsadorB, HIGH);
    movimientoDetectado = true;
  }

  if (digitalRead(buttonC) == LOW) {
    mensaje("Pulsador C");
    digitalWrite(ledPulsadorC, HIGH);
    movimientoDetectado = true;
  }

  if (digitalRead(buttonD) == LOW) {
    mensaje("Pulsador D");
    digitalWrite(ledPulsadorD, HIGH);
    movimientoDetectado = true;
  }

  if (!movimientoDetectado) {
    mensaje("Centro");
    apagarLeds();
  }

  delay(150);
}

void mensaje(String texto) {
  if (texto != mensajeAnterior) {
    if (texto != "Centro") {
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print(texto);
    }
    // Siempre enviar al puerto serial (para Python)
    Serial.println(texto);
    mensajeAnterior = texto;
  }
}

void apagarLeds() {
  digitalWrite(ledArriba, LOW);
  digitalWrite(ledAbajo, LOW);
  digitalWrite(ledIzquierda, LOW);
  digitalWrite(ledDerecha, LOW);
  digitalWrite(ledPulsadorA, LOW);
  digitalWrite(ledPulsadorB, LOW);
  digitalWrite(ledPulsadorC, LOW);
  digitalWrite(ledPulsadorD, LOW);
}

int leerPromedio(int pin) {
  int suma = 0;
  const int N = 5;
  for (int i = 0; i < N; i++) {
    suma += analogRead(pin);
    delay(2);
  }
  return suma / N;
}
