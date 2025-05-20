const int ledPins[8] = {2, 3, 4, 5, 6, 7, 8, 9};  

void setup() {
    Serial.begin(9600);  
    for (int i = 0; i < 8; i++) {
        pinMode(ledPins[i], OUTPUT);
        digitalWrite(ledPins[i], LOW);  
    }
}

void loop() {
    if (Serial.available() > 0) {  
        char caracter = Serial.read();
        if (caracter != '\n' && caracter != '\r') {  // Ignorar saltos de línea
            int numero = (int)caracter;
            mostrarBinario(numero);  
            delay(5000);  
            apagarLeds();  // Apagar LEDs después del tiempo de espera
        }
    }
}

void mostrarBinario(int num) {
    int valores[8] = {0, 0, 0, 0, 0, 0, 0, 0};  

    for (int i = 7; i >= 0; i--) {
        if (num >= potencia(2, i)) {
            valores[i] = 1;
            num -= potencia(2, i);
        }
    }

    for (int i = 0; i < 8; i++) {
        digitalWrite(ledPins[i], valores[i]);
    }
}

int potencia(int base, int exponente) {
    int resultado = 1;
    for (int i = 0; i < exponente; i++) {
        resultado *= base;
    }
    return resultado;
}

void apagarLeds() {
    for (int i = 0; i < 8; i++) {
        digitalWrite(ledPins[i], LOW);
    }
}
