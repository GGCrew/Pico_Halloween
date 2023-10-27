import random
import time

from light_strip import LightStrip, BLACK
from pixels import display_pixels


BAT = 0
PUMPKIN = 1
SKULL = 3
BOO = 4
EYES = 5
GHOST = 6

IMAGES = [
  BAT,
  PUMPKIN,
  SKULL,
  EYES,
  GHOST
]


# assign row data for "BOO" image
boo_row_data = []
boo_row_data.append([range(0, 8),     range(16, 22),                range(32, 38),                [44, 45]])
boo_row_data.append([range(0, 9),     range(15, 23),                range(31, 39),                [44, 45]])
boo_row_data.append([[0, 1, 6, 7, 8], [14, 15, 16],   [21, 22, 23], [30, 31, 32],   [37, 38, 39], [44, 45]])
boo_row_data.append([[0, 1, 7, 8],    [13, 14, 15],   [22, 23, 24], [29, 30, 31],   [38, 39, 40], [44, 45]])
boo_row_data.append([[0, 1, 7, 8],    [13, 14],       [23, 24],     [29, 30],       [39, 40],     [44, 45]])
boo_row_data.append([[0, 1, 6, 7, 8], [13, 14],       [23, 24],     [29, 30],       [39, 40],     [44, 45]])
boo_row_data.append([range(0, 8),     [13, 14],       [23, 24],     [29, 30],       [39, 40],     [44, 45]])
boo_row_data.append([range(0, 9),     [13, 14],       [23, 24],     [29, 30],       [39, 40],     [44, 45]])
boo_row_data.append([[0, 1, 7, 8, 9], [13, 14],       [23, 24],     [29, 30],       [39, 40],     [44, 45]])
boo_row_data.append([[0, 1, 8, 9],    [13, 14],       [23, 24],     [29, 30],       [39, 40],     [44, 45]])
boo_row_data.append([[0, 1, 8, 9],    [13, 14, 15],   [22, 23, 24], [29, 30, 31],   [38, 39, 40]])
boo_row_data.append([[0, 1, 7, 8, 9], [14, 15, 16],   [21, 22, 23], [30, 31, 32],   [37, 38, 39]])
boo_row_data.append([range(0, 10),    range(15, 23),                range(31, 39),                [44, 45]])
boo_row_data.append([range(0, 9),     range(16, 22),                range(32, 38),                [44, 45]])

boo_image_rows = len(boo_row_data)
boo_image_columns = 46

# initialize the "BOO" image space
boo_image = [[0 for _ in range(boo_image_columns)] for _ in range(boo_image_rows)]

# set image data
for row, row_datum in enumerate(boo_row_data):
  for column_data in row_datum:
    for column in column_data:
      boo_image[row][column] = 1

padding = [0 for _ in range(16)]
boo_image = [(padding + image_row + padding) for image_row in boo_image]


def load_image_data(image=SKULL, frame=0) -> dict:
  COLOR_1 = 1
  COLOR_2 = 2
  COLOR_3 = 3
  COLOR_4 = 4

  row = 0
  column = 0
  mirror = False
  row_data = []

  if image == BAT:
    row = 3
    column = 0
    mirror = True
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
    mirror = True
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
    mirror = True
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
        [ [COLOR_1, [2, 3, 4]] ],
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
        [ [COLOR_1, [3, 4, 5]] ],
        [ [COLOR_1, [1, 4, 5]] ],
        [ [COLOR_1, [1, 2]] ],
        [ [COLOR_1, [2, 3]] ],
        [ [COLOR_1, range(3, 6)] ],
        [ [COLOR_1, [4, 5]] ]
      ]
  elif image == BOO:
    # In development
    # TODO: test on actual hardware

    # display image in terminal for debugging/previewing
    # for row in boo_image:
    #   print(''.join([' ' if item == 0 else '#' for item in row]))

    total_frames = len(boo_image[0]) - 16
    frame = frame % total_frames

    row_data = [[[item, [index]] for index, item in enumerate(image_row[frame:(frame + 16)])] for image_row in boo_image]

    row = 1
    column = 0
    mirror = False
  elif image == EYES:
    row = 3
    column = 1
    mirror = True
    row_data = [
      [ [COLOR_1, [0, 1]] ],
      [ [COLOR_1, [2, 3]] ],
      [ [COLOR_1, [4, 5]], [COLOR_2, [1]] ],
      [ [COLOR_2, range(0, 4)] ],
      [ [COLOR_2, [0, 1, 4, 5]] ],
      [ [COLOR_2, [0, 1, 4, 5]] ],
      [ [COLOR_2, range(0, 6)] ],
      [ [COLOR_2, range(1, 5)] ],
    ]
  elif image == GHOST:
    positions = [
      [2, 3],
      [1, 2],
      [2, 1],
      [2, 0],
      [3, 1],
      [4, 2],
      [3, 3],
      [2, 4],
      [3, 5],
      [2, 6],
      [1, 5],
      [2, 4],
      [3, 4],
      [2, 3],
      [1, 4],
    ]

    internal_frame_delay = 2

    frame = frame % (len(positions) * internal_frame_delay)
    row, column = positions[frame // internal_frame_delay]

    mirror = False
    row_data = [
      [ [COLOR_1, [4, 5]] ],
      [ [COLOR_1, range(3, 7)] ],
      [ [COLOR_1, [0, 1, 3, 6, 8, 9]], [COLOR_2, [4, 5]] ],
      [ [COLOR_1, range(1, 9)] ],
      [ [COLOR_1, range(2, 8)] ],
      [ [COLOR_1, range(3, 7)] ],
      [ [COLOR_1, range(3, 7)] ],
      [ [COLOR_1, [4, 5]], [COLOR_3, [3, 6]] ],
      [ [COLOR_3, range(3, 7)] ],
      [ [COLOR_3, [4, 5]], [COLOR_4, [2, 3, 6, 7]] ],
      [ [COLOR_4, range(2, 8)] ],
    ]

  return {
    'row': row,
    'column': column,
    'mirror': mirror,
    'frame': frame,
    'row_data': row_data
  }


def apply_colors(pixels, image):
  colors = []
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
  elif image == BOO:
    colors = [
      BLACK,
      int((1 << 16) + (1 << 8) + 4)]
  elif image == EYES:
    colors = [
      BLACK,
      int(4 << 16),
      [
        int(6 << 16),
        int(2 << 16),
        int(3 << 16),
        int(4 << 16),
        int(5 << 16)
      ],
      int((2 << 16) + (2 << 8))]
  elif image == GHOST:
    colors = [
      BLACK,
      int((4 << 16) + (4 << 8) + 4),
      int((1 << 16)),
      [
        int((4 << 16) + (4 << 8) + 4),
        int((3 << 16) + (3 << 8) + 3),
      ],
      [
        int((2 << 16) + (2 << 8) + 2),
        int((1 << 16) + (1 << 8) + 1),
        BLACK
      ]]

  for row in range(0, 16):
    for column in range(0, 16):
      index = (row * 16) + column
      color = colors[pixels[index]]
      if type(color) is int:
        pixels[index] = color
      elif type(color) is list:
        pixels[index] = random.choice(color)


def display(pixels, light_strip: LightStrip, duration=60, image=BAT):
  timeout = time.time() + duration

  previous_frame = -1
  animation_in_progress = True

  while (time.time() < timeout) or (time.time() >= timeout and animation_in_progress):
    frame = previous_frame + 1
    image_data = load_image_data(image=image, frame=frame)
    row = image_data['row']
    column = image_data['column']
    mirror = image_data['mirror']
    row_data = image_data['row_data']

    animation_in_progress &= (previous_frame < image_data['frame'])
    previous_frame = image_data['frame']

    # display image in terminal for debugging/previewing
    # for row_pixel_data in row_data:
    #   print(''.join([' ' if color == 0 else '#' for color, _ in [pixel_data for pixel_data in row_pixel_data]]))

    # reset pixels
    for pixel_index in range(len(pixels)):
      pixels[pixel_index] = BLACK

    # assign image data
    for index, row_pixel_data in enumerate(row_data):
      for pixel_data in row_pixel_data:
        color, offsets = pixel_data
        for offset in offsets:
          pixels[(16 * (row + index)) + column + offset] = color
          if mirror:
            pixels[(16 * (row + index)) + (15 - column - offset)] = color

    apply_colors(pixels=pixels, image=image)

    display_pixels(pixels=pixels, light_strip=light_strip)
    time.sleep_ms(50)
