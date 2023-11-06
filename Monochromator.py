import serial 
import time 
import numpy as np 



class Monochromator:
    
    def __init__(self, port='/dev/ttyUSB0'):
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = 9600
        self.ser.bytesize = serial.EIGHTBITS # Number of bits per bytes
        self.ser.parity = serial.PARITY_NONE # Set parity check: no parity
        self.ser.stopbits = serial.STOPBITS_ONE # Number of stop bits
        self.ser.timeout = 1            # Non-block read
        self.ser.writeTimeout = 2     # Timeout for write
        
        self.terminating = '\r\n' # Terminating characters
        self.encoding = 'utf-8' # Encoding format
    
        self.open() # Open serial conenction
        
        
    def __del__(self):
        self.ser.close() 
        
    def open(self):
        """
        Open serial connection 
        """
        self.ser.open() 

    def write(self, msg):
        """
        Send a sepcified command through the serial port.

        Args:
            msg (str): Command to be sent

        Returns:
            int: Number of bytes written. 
        """
        msg = f"{msg}{self.terminating}".encode(self.encoding)
        return self.ser.write(msg)  
    
    
    def openShutter(self):
        """
        Opens the shutter on the device. 
        """
        return self.write("SHUTTER O") 
    
    
    def closeShutter(self):
        """
        Closes the shutter on the device. 
        """
        return self.write("SHUTTER C")
    
    
    def goWave(self, waveLength):
        """
            Go to specified wavelength.

        Args:
            waveLength (int): Desired wavelength

        Returns:
            float: current wavelength
        """
        self.write(f"GOWAVE {waveLength}")
        self.ser.readline() 
        time.sleep(3) 
        self.write("WAVE?")
        # Super scuffed way of getting most recent response 
        # Could also use a separate thread to keep track but I AM LAZY!>!>!
        self.ser.readline()
        response = self.ser.readline().decode(self.encoding).strip()
        return response
    
    def readWavelength(self, display=False):
        """
        Read the current wavelength setting. 

        Returns:
            str: Current wavelength setting. 
        """
        self.write("WAVE?")
        time.sleep(3) 
        response = self.ser.readline().decode(self.encoding)
        if display: 
            print(response)
        return response 
    