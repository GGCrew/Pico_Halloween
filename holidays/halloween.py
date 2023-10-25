import time

from light_strip import LightStrip, BLACK
from pixels import display_pixels


BAT = 0
PUMPKIN = 1
SKULL = 3

IMAGES = [
  BAT,
  PUMPKIN,
  SKULL
]

COLOR_1 = 1
COLOR_2 = 2


def load_image_data(image=SKULL, frame=0) -> dict:
  row = 0
  column = 0
  row_data = []

  if image == BAT:
    row = 3
    column = 0
    row_data = [
      [ [COLOR_1, [6]] ],
      [ [COLOR_1, [1,2,6]], [COLOR_2, [7]] ],
      [ [COLOR_1, [2,3,4,7]] ],
      [ [COLOR_1, [3,4,5,6,7]] ],
      [ [COLOR_1, [4,5,6,7]] ],
      [ [COLOR_1, [5,6,7]] ],
      [ [COLOR_1, [6,7]] ],
      [ [COLOR_1, [6,7]] ],
      [ [COLOR_1, [7]] ],
      [ [COLOR_1, [7]] ],
      [ [COLOR_1, [6]] ]
    ]
  elif image == PUMPKIN:
    row = 1
    column = 2
    row_data = [
      [ [COLOR_2, [6, 7]] ],
      [ [COLOR_2, [5]] ],
      [ [COLOR_1, range(2, 6)] ],
      [ [COLOR_1, range(1, 6)] ],
      [ [COLOR_1, [0, 1, 2, 4, 5]] ],
      [ [COLOR_1, [0, 1, 5]] ],
      [ [COLOR_1, range(0, 6)] ],
      [ [COLOR_1, range(0, 5)] ],
      [ [COLOR_1, [0, 2, 3, 4 ,5]] ],
      [ [COLOR_1, [0, 3 ,5]] ],
      [ [COLOR_1, [0, 1]] ],
      [ [COLOR_1, range(1, 4)] ],
      [ [COLOR_1, range(2, 6)] ],
      [ [COLOR_1, range(3, 6)] ]
    ]
  elif image == SKULL:
    row = 1
    column = 2
    frame = frame % 2
    if frame == 0:
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
        [ [COLOR_1, [4, 5]] ]
      ]
    elif frame == 1:
      row_data = [
        [ [COLOR_1, range(3, 6)] ],
        [ [COLOR_1, range(1, 6)] ],
        [ [COLOR_1, range(0, 6)] ],
        [ [COLOR_1, [0, 1, 5]] ],
        [ [COLOR_1, [0, 1, 5]], [COLOR_2, [3]] ],
        [ [COLOR_1, [0, 1, 5]] ],
        [ [COLOR_1, range(0, 6)] ],
        [ [COLOR_1, [2, 3, 4]] ],
        [ [COLOR_1, [0, 3, 4, 5]] ],
        [ [COLOR_1, [1, 4, 5]] ],
        [ [COLOR_1, [1, 2]] ],
        [ [COLOR_1, [2, 3]] ],
        [ [COLOR_1, range(3, 6)] ],
        [ [COLOR_1, [4, 5]] ]
      ]

  return {
    'row': row,
    'column': column,
    'frame': frame,
    'row_data': row_data
  }


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


def display(pixels, light_strip: LightStrip, duration=60, image=BAT):
  timeout = time.time() + duration

  frame = 0

  while time.time() < timeout:
    image_data = load_image_data(image=image, frame=frame)
    row = image_data['row']
    column = image_data['column']
    frame = image_data['frame']
    row_data = image_data['row_data']

    frame += 1

    # reset pixels
    for pixel_index in range(len(pixels)):
      pixels[pixel_index] = BLACK

    # assign image data
    for index, row_pixel_data in enumerate(row_data):
      for pixel_data in row_pixel_data:
        color, offsets = pixel_data
        for offset in offsets:
          pixels[(16 * (row + index)) + column + offset] = color
          pixels[(16 * (row + index)) + (15 - column - offset)] = color

    apply_colors(pixels=pixels, image=image)

    display_pixels(pixels=pixels, light_strip=light_strip)
    time.sleep_ms(50)
