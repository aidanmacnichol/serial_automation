## Class: Photodiode

**Description:** This class represents a power meter and provides methods for controlling and interfacing with it via a serial connection.

### Attributes:

- `ser` (Serial): An instance of the `serial.Serial` class for serial communication.

### Methods:

#### Method: `__init__(self, port="/dev/ttyUSB1")`

**Description:** Constructor method for initializing the `Photodiode` object.

**Arguments:** 
- `port` (str, optional): The serial port for communication (default is "/dev/ttyUSB1").

**Returns:** 
- An instance of the `Photodiode` class with default attributes and an opened serial connection.

#### Method: `__del__(self)`

**Description:** Destructor method to close the serial connection.

**Arguments:** None

**Returns:** None

#### Method: `open(self)`

**Description:** Open the serial connection. Ran in constructor. 

**Arguments:** None

**Returns:** None

#### Method: `setUnits(self)`

**Description:** Make sure the correct unit setting is set. Ran in constructor. 

**Arguments:** None

**Returns:** None

#### Method: `disableEcho(self)`

**Description:** Checks and disables Echo mode. Needs to be disabled for proper flushing out output. Ran in constructor. 

**Arguments:** None

**Returns:** None

#### Method: `setRange(self)`

**Description:** Set the measurement range. Ran in constructor

**Arguments:** None

**Returns:** None

#### Method: `attenuationOn(self)`

**Description:** Turn on the detector-attenuation combo. Ran in constructor. 

**Arguments:** None

**Returns:** None

#### Method: `write(self, msg)`

**Description:** Send a specified command through the serial port.

**Arguments:** 
- `msg` (str): Command to be sent.

**Returns:** 
- int: Number of bytes written.

#### Method: `writeAndRead(self, msg, display=False)`

**Description:** Write a message and return the response from the power meter.

**Arguments:** 
- `msg` (_type_): Command to be sent. 
- `display` (bool, optional): Display response message in the console. Defaults to False.

**Returns:** 
- response (str): Response message from the power meter.

#### Method: `getRange(self, display=False)`

**Description:** Get the current range of the power meter and print it.

**Arguments:** 
- `display` (bool, optional): Print response message to the console. Defaults to False.

**Returns:** 
- str: Current range of the power meter.

#### Method: `readData(self, display=False)`

**Description:** Read data from the power meter.

**Arguments:** 
- `display` (bool, optional): Display response message in the console. Defaults to False.

**Returns:** 
- float: Value of the power meter.

#### Method: `setWavelength(self, wl)`

**Description:** Set the power meter to a given wavelength.

**Arguments:** 
- `wl` (int): Desired wavelength.

**Returns:** None

#### Method: `curWavelength(self)`

**Description:** Get the current wavelength setting and print it.

**Arguments:** None

**Returns:** 
- int: Current wavelength.

This class allows you to control and interface with a photodiode via a serial connection, making it convenient for various photodiode-related tasks.
