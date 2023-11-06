## Class: Monochromator

**Description:** This class represents a monochromator device and provides methods for controlling and interfacing with it via a serial connection.

### Attributes:

- `ser` (Serial): An instance of the `serial.Serial` class for serial communication.

### Methods:

#### Method: `__init__(self, port='/dev/ttyUSB0')`

**Description:** Constructor method for initializing the `Monochromator` object.

**Arguments:** 
- `port` (str, optional): The serial port for communication (default is "/dev/ttyUSB0").

**Returns:** 
- An instance of the `Monochromator` class with default attributes and an opened serial connection.

#### Method: `__del__(self)`

**Description:** Destructor method to close the serial connection.

**Arguments:** None

**Returns:** None

#### Method: `open(self)`

**Description:** Open the serial connection.

**Arguments:** None

**Returns:** None

#### Method: `write(self, msg)`

**Description:** Send a specified command through the serial port.

**Arguments:** 
- `msg` (str): Command to be sent.

**Returns:** 
- int: Number of bytes written.

#### Method: `openShutter(self)`

**Description:** Opens the shutter on the device.

**Arguments:** None

**Returns:** None

#### Method: `closeShutter(self)`

**Description:** Closes the shutter on the device.

**Arguments:** None

**Returns:** None

#### Method: `goWave(self, waveLength)`

**Description:** Go to a specified wavelength.

**Arguments:** 
- `waveLength` (int): Desired wavelength.

**Returns:** 
- float: Current wavelength.

#### Method: `readWavelength(self, display=False)`

**Description:** Read the current wavelength setting.

**Arguments:** 
- `display` (bool, optional): Display response message in the console. Defaults to False.

**Returns:** 
- str: Current wavelength setting.

This class allows you to control and interface with a monochromator device via a serial connection, making it convenient for various monochromator-related tasks.
