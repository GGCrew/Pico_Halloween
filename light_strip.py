import array
from machine import Pin
import rp2

RED = int(255 << 16)
GREEN = int(255 << 8)
BLUE = int(255)
MAGENTA = int(RED + BLUE)
YELLOW = int(RED + GREEN)
CYAN = int(GREEN + BLUE)
WHITE = int(RED + GREEN + BLUE)
BLACK = int(0)

class LightStrip:
  """
  A class for controling an LED light strip.

  Attributes:
    gpio_pin_number (int): The GPIO pin used for the `data` signal.
                           (Note: The GPIO pin number rarely corresponds with the physical pin number.)
    number_of_pixels (int):  The total number of addressable lights on the strip.
    brightness (float): A value between 0 (0%) and 1 (100%) to set the maximum brightness for all connected lights.
    rgb_order (str): The data order used by the connected light strip.
    pixels (array.array): An array of `unsigned int` representing the final color for each light.
    state_machine (rp2.StateMachine): Access to the RP2040's PIO interface.
  """

  def __init__(self, gpio_pin_number: int, number_of_pixels: int, brightness: float, rgb_order: str) -> None:
    """
    The constructor for the LightStrip class.

    Initializes the instance variables and activates the `state_machine` object.

    Parameters:
      gpio_pin_number (int): The GPIO pin used for the `data` signal.
                             (Note: The GPIO pin number rarely corresponds with the physical pin number.)
      number_of_pixels (int):  The total number of addressable lights on the strip.
      brightness (float): A value between 0 (0%) and 1 (100%) to set the maximum brightness for all connected lights.
      rgb_order (str): The data order used by the connected light strip.
                       Strips from different manufacturers will wire their LEDs in different orders. (eg BRG for the WS2812B strip from BTF-Lighting)
                       This value will convert standard RGB-ordered values into the specified order used for the connected lights.

    Returns:
      None
    """

    self.gpio_pin_number = gpio_pin_number
    self.number_of_pixels = number_of_pixels
    self.brightness = brightness
    self.rgb_order = rgb_order.upper()

    self.pixels = array.array("I", [0 for _ in range(self.number_of_pixels)])

    # Create the StateMachine with the ws2812 program, outputting on pin
    self.state_machine = rp2.StateMachine(0, self.ws2812, freq=8_000_000, sideset_base=Pin(self.gpio_pin_number))
    # Start the StateMachine
    self.state_machine.active(1)

  def __del__(self):
    """
    The deconstructor for the LightStrip class.

    Explicitly frees memory-intensive instance objects and deactivates the `state_machine` object.

    Parameters:
      None

    Returns:
      None
    """

    self.pixels = None
    self.state_machine.active(0)
    self.state_machine = None

  def set_pixels(self, pixels: array.array) -> None:
    """
    Assign color values to the instance `pixels` object.

    Iterates through each values in the supplied `pixels` object and copies the RGB data to the instance `pixels` object.
    The copy process performs the following actions:
      * convert each pixel value from RGB-ordered values to strip-specific order
      * applies the `brightness` value

    Parameters:
      pixels (list): color values for each pixel as RGB-ordered values

    Returns:
      None
    """

    # Clear existing pixels
    for index in range(self.number_of_pixels):
      self.pixels[index] = 0

    # Preparation to convert color data from standard RGB value order to LED signal order
    r_index = self.rgb_order.find('R')
    g_index = self.rgb_order.find('G')
    b_index = self.rgb_order.find('B')

    # Convert color data from RGB to strip order and adjust brightness
    for index, color in enumerate(pixels):
      # sanity check if provided data is more than the instantiated # of pixels
      if index < self.number_of_pixels:
        r = int(((color >> ((2 - r_index) * 8)) & 0xFF) * self.brightness)
        g = int(((color >> ((2 - g_index) * 8)) & 0xFF) * self.brightness)
        b = int(((color >> ((2 - b_index) * 8)) & 0xFF) * self.brightness)
        self.pixels[index] = (r << 16) + (g << 8) + b

  def show(self) -> None:
    """
    Sends the instance `pixels` data to connected lights.

    Parameters:
      None

    Returns:
      None
    """
    self.state_machine.put(self.pixels, 8)

  def off(self) -> None:
    """
    Turns off the connected lights.

    Parameters:
      None

    Returns:
      None
    """
    self.pixels = array.array("I", [0 for _ in range(self.number_of_pixels)])
    self.show()


  def cycle(self) -> None:
    """
    Test the lights by cycling through a defined set of colors.

    Sets all connected lights to the same color, then increases brightness from 0% to 100%.
    The color cycle is: RED, GREEN, BLUE, MAGENTA, YELLOW, CYAN, WHITE

    If the colors display in a different order (eg red, blue, green), then the `rgb_order` value
    in `settings/hardware.json` needs to be changed.

    Parameters:
      None

    Returns:
      None
    """
    # Preparation to convert color data from standard RGB value order to LED signal order
    r_index = self.rgb_order.find('R')
    g_index = self.rgb_order.find('G')
    b_index = self.rgb_order.find('B')

    # cycle through colors on all pixels
    colors = [RED, GREEN, BLUE, MAGENTA, YELLOW, CYAN, WHITE]
    for color in colors:
      for brightness in range(100):
        adjusted_brightness = brightness / 100
        r = int(((color >> ((2 - r_index) * 8)) & 0xFF) * adjusted_brightness)
        g = int(((color >> ((2 - g_index) * 8)) & 0xFF) * adjusted_brightness)
        b = int(((color >> ((2 - b_index) * 8)) & 0xFF) * adjusted_brightness)
        adjusted_color = (r << 16) + (g << 8) + b
        del adjusted_brightness
        del r
        del g
        del b

        for index in range(self.number_of_pixels):
          self.pixels[index] = adjusted_color
        del adjusted_color
        self.show()

    del colors


  def chase(self) -> None:
    """
    Turns on each connected light in their wired order.

    Turns on each light, seeming to "chase" along the connected lights.
    The first light will turn on, then the second, then third, and so on down the line.
    The chase will run multiple times, cycling through the following colors:
      RED, GREEN, BLUE, WHITE, BLACK (aka off)

    Parameters:
      None

    Returns:
      None
    """
    import time

    # Preparation to convert color data from standard RGB value order to LED signal order
    r_index = self.rgb_order.find('R')
    g_index = self.rgb_order.find('G')
    b_index = self.rgb_order.find('B')

    # chase lights along the pixels
    colors = [RED, GREEN, BLUE, WHITE, BLACK]
    for color in colors:
      print(color)
      r = int((color >> ((2 - r_index) * 8)) & 0xFF)
      g = int((color >> ((2 - g_index) * 8)) & 0xFF)
      b = int((color >> ((2 - b_index) * 8)) & 0xFF)
      adjusted_color = (r << 16) + (g << 8) + b
      del r
      del g
      del b

      for index in range(self.number_of_pixels):
        self.pixels[index] = adjusted_color
        self.show()
        time.sleep_ms(10) # delay to allow signal to propogate all along the strip
      del adjusted_color

    del colors
    del r_index
    del g_index
    del b_index


  def post(self) -> None:
    """
    Power On Self Test to quickly check the lights.

    Parameters:
      None

    Returns:
      None
    """
    self.cycle()
    self.chase()


  @rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
  def ws2812():
    """
    Assembly code to efficiently transmit data to the GPIO interface.

    Code pulled from MicroPython RP2 examples:
    https://github.com/micropython/micropython/blob/master/examples/rp2/pio_ws2812.py

    Parameters:
      None

    Returns:
      None
    """

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
    wrap()
