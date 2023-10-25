import array
import time

from light_strip import LightStrip


def load_image_data(image_file):
  try:
    with open(image_file) as file:
      data = file.read().splitlines()
  except:
    data = []

  data_dict = []
  for item in data:
    [r, g, b] = item.split(',')
    data_dict.append({'r': int(r), 'g': int(g), 'b': int(b)})

  return data_dict


def copy_image_data_to_pixels(pixels: array.array, image_data):
  """
  Update the `pixels` array with new color values based on `image_data`.

  All data in the `pixels` array will be overwritten.

  Parameters:
    pixels (array.array): Array of pixels
    image_data (dict): Locations and utilization percentage for each location
    settings (dict): Object containing `location_id_pixel_index_map` and `utilization_colors` settings

  Returns
    None
  """

  # reset all pixels
  for index in range(len(pixels)):
    pixels[index] = 0

  for pixel_index, item in enumerate(image_data):
    color = int(
      int(item['r'] * (256 ** 2)) +
      int(item['g'] * (256 ** 1)) +
      int(item['b'] * (256 ** 0)))
    pixels[pixel_index] = color


def map_pixels(pixels):
  """
  Reorder pixel data to match the LED positions on the display
  """
  mapped_pixels = array.array("I", [0 for _ in range(len(pixels))])

  for row in range(16):
    for column in range(16):
      pixel_index = (row * 16) + column
      if (column % 2) == 0:
        mapped_row = row
      else:
        mapped_row = 15 - row
      mapped_column = (column * 16)
      # print(mapped_column, mapped_row)
      mapped_pixel_index = mapped_column + mapped_row
      mapped_pixels[mapped_pixel_index] = pixels[pixel_index]

  return mapped_pixels


def display_pixels(pixels, light_strip: LightStrip):
  pixels = map_pixels(pixels=pixels)
  light_strip.set_pixels(pixels)
  light_strip.show()


def display_image(filename, milliseconds, pixels, light_strip: LightStrip):
  image_data = load_image_data(filename)
  copy_image_data_to_pixels(pixels=pixels, image_data=image_data)
  display_pixels(pixels=pixels, light_strip=light_strip)
  time.sleep_ms(milliseconds)
