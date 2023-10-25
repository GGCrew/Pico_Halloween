import array
import json
import machine

from light_strip import LightStrip, BLACK

import holidays.halloween


def load_settings():
  with open('settings/hardware.json') as file:
    hardware = json.load(file)

  return {
    'hardware': hardware,
  }


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
    counter = 0
    while True:
      counter += 1
      print(counter)

      holidays.halloween.display(pixels=pixels, light_strip=light_strip, duration=1)

  except KeyboardInterrupt:
    print('Ctrl+C received')

  print('Exiting...')
  light_strip.off()
  del light_strip


if __name__ == '__main__':
  main()
