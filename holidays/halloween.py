import time

from light_strip import LightStrip, BLACK
from pixels import display_pixels


def copy_data_to_pixel_array(pixels):
  COLOR_1 = 1
  COLOR_2 = 2

  for pixel_index in range(len(pixels)):
    pixels[pixel_index] = BLACK

  row = 3
  column = 0

  row += 0
  offsets = [6]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + column + (15 - offset)] = COLOR_1

  row += 1
  offsets = [1,2,6]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + column + (15 - offset)] = COLOR_1
  offsets = [7]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_2
    pixels[(16 * row) + column + (15 - offset)] = COLOR_2

  row += 1
  offsets = [2,3,4,7]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + column + (15 - offset)] = COLOR_1

  row += 1
  offsets = [3,4,5,6,7]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + column + (15 - offset)] = COLOR_1

  row += 1
  offsets = [4,5,6,7]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + column + (15 - offset)] = COLOR_1

  row += 1
  offsets = [5,6,7]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + column + (15 - offset)] = COLOR_1

  row += 1
  offsets = [6,7]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + column + (15 - offset)] = COLOR_1

  row += 1
  offsets = [6,7]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + column + (15 - offset)] = COLOR_1

  row += 1
  offsets = [7]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + column + (15 - offset)] = COLOR_1

  row += 1
  offsets = [7]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + column + (15 - offset)] = COLOR_1

  row += 1
  offsets = [6]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + column + (15 - offset)] = COLOR_1


def apply_colors(pixels):
  colors = [
    int(1),
    BLACK,
    int((1 << 16))]
  for row in range(0, 16):
    for column in range(0, 16):
      index = (row * 16) + column
      color = colors[pixels[index]]
      pixels[index] = color


def display(pixels, light_strip: LightStrip, duration = 60):
  timeout = time.time() + duration

  copy_data_to_pixel_array(pixels=pixels)
  apply_colors(pixels=pixels)

  while time.time() < timeout:
    display_pixels(pixels=pixels, light_strip=light_strip)
    time.sleep_ms(500)
