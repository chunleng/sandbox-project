from machine import Pin, I2C, PWM
from picolab import SSD1306_I2C, ReadADC, WS2812
from picolab import DHT11, InvalidChecksum
import array
import framebuf
import machine
import utime as time
import time
buzzer = buzzer = PWM(Pin(20))
buzzer.duty_u16(0)
motor_1 = Pin(21, Pin.OUT)
motor_2 = Pin(22, Pin.OUT)
relay = Pin(12, Pin.OUT)
led = Pin(7, Pin.OUT)
 
ldr = ReadADC()
pot = ReadADC()
 

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c)                  # Init oled display

#Robotistan logo
buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xff\xff\xff\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xff\xff\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff_\xff\xcb\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xfc\x03\xff\x01\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf8\x01\xfc\x00~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf0\x00\xfc\x00>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xe0\x80\xf8 >\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xe3\xe0x\xf8\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xe7\xf0q\xfc\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xcf\xf8s\xfe\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xef\xf8s\xfe\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xcf\xf8w\xfe\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xef\xf8{\xfe>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xe1\xf8\xf8|>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf0\xf0\xfc|?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf9\xc1\xfcp~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xfc\x07\xff\x01\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff_\xff\xd7\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xff\xfd\xff\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xfew\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xff\x07\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xff\xff\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\xff\xff\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00m\xb6\xdbm\xb6\xdd\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x01\xbf\xff\xff\xff\xff\xff\xec\x00\x00\x00\x00\x00\x00\x00\x00\x01\x1f\xff\xff\xff\xff\xff\xc6\x00\x00\x00\x00\x00\x00\x00\x00\x01\x1f\xff\xff\xff\xff\xff\xc2\x00\x00\x00\x00\x00\x00\x00\x00\x01\x9bo\xff\xff\xff\xb6\xec\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf8\x03\xff\xff\xfe\x00~\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf0\x07\xff\xff\xff\x00~\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf8\x07\xff\xff\xff\x80~\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf8\x0f\xff\xff\xff\x80~\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf8\x0f\xff\xff\xff\xc0~\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf0\x1f\xff\xff\xff\xc0~\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf8\x1f\xff\xff\xff\xe0~\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf0\x1f\xff\xff\xff\xe0~\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf8?\xff\xff\xff\xe0~\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf8\x7f\xff\xff\xff\xf0\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x07\xfc\x7f\xff\xff\xff\xf9\xff\x00\x00\x00\x00\x00\x00\x00\x00\x07\xfc\x7f\xff\xff\xff\xf8\xff\x00\x00\x00\x00\x00\x00\x00\x00\x07\xbc\xff\xff\xff\xff\xf9\xef\x00\x00\x00\x00\x00\x00\x00\x00\x07\xbc\xff\xff\xff\xff\xfc\xf7\x00\x00\x00\x00\x00\x00\x00\x00\x03\xfd\xff\xff\xff\xff\xfd\xef\x00\x00\x00\x00\x00\x00\x00\x00\x07\xbd\xff\xff\xff\xff\xfe\xff\x00\x00\x00\x00\x00\x00\x00\x00\x02\x91\xff\xff\xff\xff\xfeB\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xff\xff\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xff\xff\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00*\xaa\xb6\xdb`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x8f\xff\xff\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x01\xdd\xbb\xbd\xce\xdb\x7f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x01\xcc\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xff\xff\xcf\xff\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x00\x01\xcc\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xdf\xff\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x00\x01\xcc\x00\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xff\xff\xcf\xff\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd5UU\xce\xaa\xaa\x9c\x00\x00\x00\x00\x00\x00\x00\x00\x01\xd5UU\xce\xaa\xaa\xbc\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x8f\xff\xff\xfc')
 
 
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
#     wrap()
   
#delay here is th0e reset time. You need a pause to reset the LED strip back to the initial LED
#however, if you have quite a bit of processing to do before the next time you update the strip
#you could put in delay=0 (or a lower delay)
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE,BLACK)
       
ws = WS2812();
pin = Pin(11, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)
    
while True:
    buzzer.duty_u16(2000)
    buzzer.freq(1000)
    time.sleep(0.5)
    buzzer.duty_u16(0)
    time.sleep(0.5)
    motor_1.high()
    motor_2.high()
    time.sleep(0.5)
    motor_1.low()
    motor_2.low()
    time.sleep(0.5)
    relay.high()
    time.sleep(0.5)
    relay.low()
    time.sleep(0.5)
    led.high()
    time.sleep(0.5)
    led.low()
    time.sleep(0.5)
     
     
    sensor.measure()
    temp  = (sensor.temperature)
    hum = (sensor.humidity)
    print("Temperature: {}".format(temp))
    print("Humidity: {}".format(hum))
    #Load the raspberry pi logo into the framebuffer (the image is 32x32)
    fb = framebuf.FrameBuffer(buffer, 128,64 , framebuf.MONO_HLSB)
    
    # Clear the oled display in case it has junk on it.
    oled.fill(0)
    # # Blit the image from the framebuffer to the oled display
    oled.blit(fb, 0, 0)
    # # Add some text
    oled.text("Sicaklik: ",0,0)
    oled.text(str(round(temp,2)),0,10)
    oled.text("Nem: ",0,20)
    oled.text(str(round(hum,2)),0,30)   
    
    # Finally update the oled display so the image & text is displayed
    oled.show()
    time.sleep(1)
    oled.fill(0)
    a = 10
    while a > 0:
        a -= 1
        oled.fill(0)
        (analog_value, voltage) =  pot.read_potentiometer()
        (analog_value1, voltage1) =  ldr.read_ldr()
        oled.text("POT: ",0,0)
        oled.text(str(round(analog_value,2)),0,10)
        oled.text("LDR: ",0,20)
        oled.text(str(round(analog_value1,2)),0,30)
        oled.show()
        time.sleep(0.2)
    oled.fill(0)
    oled.show()
    print("fills")
    for color in COLORS:
        ws.pixels_fill(color)
        ws.pixels_show()
        time.sleep(0.2)
    time.sleep(1)
    







