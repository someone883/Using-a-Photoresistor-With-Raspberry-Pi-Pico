#importing libraries
import machine
import utime
#making variables
photoresistor = machine.ADC(28)
while True:
    light_value  = photoresistor.read_u16()
    print(light_value)#<-- high value = more light les value = less light
    utime.sleep_ms(10)