import array
import json
import machine
import random
import time

from light_strip import LightStrip, BLACK

import holidays.halloween


def load_settings():
  with open('settings/hardware.json') as file:
    hardware = json.load(file)

  with open('settings/sensors.json') as file:
    sensors = json.load(file)

  return {
    'hardware': hardware,
    'sensors': sensors
  }


def get_sensor_data(sensors: array.array) -> array.array:
  data = array.array("f", [0 for _ in range(len(sensors))])

  for index, sensor in enumerate(sensors):
    trigger_pin = int(sensor['trigger_gpio_pin_number'])
    echo_pin = int(sensor['echo_gpio_pin_number'])
    trigger = machine.Pin(trigger_pin, machine.Pin.OUT, pull=None)
    echo = machine.Pin(echo_pin, machine.Pin.IN, pull=None)

    # Stabilize the sensor
    trigger.value(0)
    time.sleep_ms(250)

    # Send pulse
    trigger.value(1)
    time.sleep_ms(1)
    trigger.value(0)
    pulse_time = machine.time_pulse_us(echo, 1, 500*2*30)

    distance_mm = pulse_time * 100 // 582

    data[index] = distance_mm

  return data


def main():
  # use built-in LED as a power light
  led = machine.Pin("LED", machine.Pin.OUT)
  led.on()

  settings = load_settings()
  print(settings)

  light_strip = LightStrip(
    rgb_order=settings['hardware']['rgb_order'],
    brightness=settings['hardware']['brightness'],
    gpio_pin_number=settings['hardware']['gpio_pin_number'],
    number_of_pixels=settings['hardware']['number_of_pixels'])

  # update lights
  try:
    pixels = array.array("I", [BLACK for _ in range(settings['hardware']['number_of_pixels'])])
    while True:

      sensor_data = get_sensor_data(sensors=settings['sensors'])
      for index, datum in enumerate(sensor_data):
        print(index, datum)

      if sensor_data[0] < 500.0:
        image = random.choice(holidays.halloween.IMAGES)
        holidays.halloween.display(pixels=pixels, light_strip=light_strip, duration=3, image=image)
        light_strip.off()
      else:
        time.sleep_ms(250)

  except KeyboardInterrupt:
    print('Ctrl+C received')

  print('Exiting...')
  light_strip.off()
  del light_strip


if __name__ == '__main__':
  main()
