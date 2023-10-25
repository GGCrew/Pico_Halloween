import time

from light_strip import LightStrip, BLACK
from pixels import display_pixels


BAT = 0
PUMPKIN = 1
SKULL = 3

COLOR_1 = 1
COLOR_2 = 2


def copy_bat_data_to_pixel_array(pixels):
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


def copy_pumpkin_data_to_pixel_array(pixels):
  for pixel_index in range(len(pixels)):
    pixels[pixel_index] = BLACK

  row = 1
  column = 2

  row += 0
  offsets = [6, 7]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_2

  row += 1
  offsets = [5, 6]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_2

  row += 1
  offsets = range(2, 6)
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + (15 - column - offset)] = COLOR_1

  row += 1
  offsets = range(1, 6)
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + (15 - column - offset)] = COLOR_1

  row += 1
  offsets = [0, 1, 2, 4, 5]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + (15 - column - offset)] = COLOR_1

  row += 1
  offsets = [0, 1, 5]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + (15 - column - offset)] = COLOR_1

  row += 1
  offsets = range(0, 6)
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + (15 - column - offset)] = COLOR_1

  row += 1
  offsets = range(0, 5)
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + (15 - column - offset)] = COLOR_1

  row += 1
  offsets = [0, 2, 3, 4 ,5]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + (15 - column - offset)] = COLOR_1

  row += 1
  offsets = [0, 3 ,5]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + (15 - column - offset)] = COLOR_1

  row += 1
  offsets = [0, 1]
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + (15 - column - offset)] = COLOR_1

  row += 1
  offsets = range(1, 4)
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + (15 - column - offset)] = COLOR_1

  row += 1
  offsets = range(2, 6)
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + (15 - column - offset)] = COLOR_1

  row += 1
  offsets = range(3, 6)
  for offset in offsets:
    pixels[(16 * row) + column + offset] = COLOR_1
    pixels[(16 * row) + (15 - column - offset)] = COLOR_1


def copy_skull_data_to_pixel_array(pixels):
  row_data = [
    [ [COLOR_1, range(3, 6)] ],
    [ [COLOR_1, range(1, 6)] ],
    [ [COLOR_1, range(0, 6)] ],
    [ [COLOR_1, [0, 1, 5]] ],
    [ [COLOR_1, [0, 1, 5]], [COLOR_2, [3]] ],
    [ [COLOR_1, [0, 1, 5]] ],
    [ [COLOR_1, range(0, 6)] ],
    [ [COLOR_1, [0, 2, 3, 4]] ],
    [ [COLOR_1, [1, 3, 4, 5]] ],
    [ [COLOR_1, [1, 2, 4, 5]] ],
    [ [COLOR_1, [2, 3]] ],
    [ [COLOR_1, range(3, 6)] ],
    [ [COLOR_1, [4, 5] ]]
  ]

  for pixel_index in range(len(pixels)):
    pixels[pixel_index] = BLACK

  row = 1
  column = 2

  for index, row_pixel_data in enumerate(row_data):
    print(index, row_pixel_data)
    for pixel_data in row_pixel_data:
      print(pixel_data)
      color, offsets = pixel_data
      print(color, offsets)
      for offset in offsets:
        print(offset)
        pixels[(16 * (row + index)) + column + offset] = color
        pixels[(16 * (row + index)) + (15 - column - offset)] = color


def apply_colors(pixels, image):
  if image == BAT:
    colors = [
      int(1),
      BLACK,
      int((1 << 16))]
  elif image == PUMPKIN:
    colors = [
      BLACK,
      int((4 << 16) + (1 << 8)),
      int(1 << 8)]
  elif image == SKULL:
    colors = [
      BLACK,
      int((4 << 16) + (4 << 8) + 4),
      int(8 << 16)]

  for row in range(0, 16):
    for column in range(0, 16):
      index = (row * 16) + column
      color = colors[pixels[index]]
      pixels[index] = color


def display(pixels, light_strip: LightStrip, duration=60, image=SKULL):
  timeout = time.time() + duration

  if image == BAT:
    copy_bat_data_to_pixel_array(pixels=pixels)
  elif image == PUMPKIN:
    copy_pumpkin_data_to_pixel_array(pixels=pixels)
  elif image == SKULL:
    copy_skull_data_to_pixel_array(pixels=pixels)

  apply_colors(pixels=pixels, image=image)

  while time.time() < timeout:
    display_pixels(pixels=pixels, light_strip=light_strip)
    time.sleep_ms(500)
