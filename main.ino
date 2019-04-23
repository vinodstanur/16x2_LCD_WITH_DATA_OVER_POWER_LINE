void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT); //D7
  pinMode(3, OUTPUT); //D6
  pinMode(4, OUTPUT); //D5
  pinMode(5, OUTPUT); //D4
  pinMode(6, OUTPUT); //EN
  pinMode(7, OUTPUT); //RS
  analogWrite(10, 255); //set backlight to maximum brightness
}

void setData(uint8_t d) {
  //not optimized. But it is okay.
  digitalWrite(5, 0);
  digitalWrite(4, 0);
  digitalWrite(3, 0);
  digitalWrite(2, 0);
  if (d & 1) digitalWrite(5, 1);
  if (d & 2) digitalWrite(4, 1);
  if (d & 4) digitalWrite(3, 1);
  if (d & 8) digitalWrite(2, 1);
}

void setEN(uint8_t d) {
  if (d) digitalWrite(6, 1);
  else digitalWrite(6, 0);
}

void setRS(uint8_t d) {
  if (d) digitalWrite(7, 1);
  else digitalWrite(7, 0);
}

void setLED(uint8_t d) {
  analogWrite(10, (d << 4));
}

void loop() {

  if (Serial.available()) {
    uint8_t a = Serial.read();
    //Serial.write(a);
    if ((a & 0xF0) == 0xA0) { //MS nibble A means LS nibble is 4 bit data
      setData(a & 0xf);
    } else if ((a & 0xF0) == 0xB0) {//MS nibble B means LSBit is RS
      setRS(a & 0xf);
    } else if ((a & 0xF0) == 0xC0) {//MS nibble C means LSBit is EN
      setEN(a & 0xf);
    } else if ((a & 0xF0) == 0xD0) {//MS nibble D means LS nibble is led brightness. MAX 15, min 0
      setLED(a & 0xf);
    }
  }

}