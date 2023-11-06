import Monochromator
import Photodiode
import csv
import numpy as np
import time 

##########################################
# Example file. For gathering photodiode readings
# Should give an idea how to use the classes.
# Methods are run in main at the bottom of this file.  
##########################################


def runPhotodiode(start=400, stepSize=100, file_name = 'photodiodeData'):
    """
    Gather photodiode readings. Initial wavelength at start and goes till 700 + stepSize.
    data is saved as a csv in data/photodiode.

    Args:
        start (int, optional): Starting wavelength in nm. Defaults to 400.
        stepSize (int, optional): Wavelength stepsize in nm. Defaults to 100.
        file_name (str, optional): filename for saved data. In csv format. Defaults to 'photodiodeData'.
    """
     # Create instrument objects
    monochromator = Monochromator()
    photodiode = Photodiode() 
    
    # List for wavelengths 
    wavelengths = []
    data = {} 
    
    # Directory where data will be saved
    dirPath = 'data/photodiode'
    
    # Go to starting wl and wait extra long
    monochromator.goWave(start)
    time.sleep(5) 
    
    for n in range(start, 700 + stepSize, stepSize):
        wl = monochromator.goWave(n)
        wavelengths.append(wl) 
        photodiode.setWavelength(wl) 
        time.sleep(1)
        
        readings = [] 
        
        # Get 5 minutes of readings in 1s intervals
        for i in range(300):
            readings.append(photodiode.readData()) 
            time.sleep(1) 
            
        if wl not in data:
            data[wl] = []
        
        data[wl] = readings
        
        # Define the CSV file name
        file_name += '.csv'  
        filePath = f'{dirPath}/{file_name}'
                
        # Write csv file 
        with open(filePath, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            # Write the header row with column names
            csv_writer.writerow(['Wavelength', 'Readings'])
            # Write data
            for wavelength, readings in data.items():
                for reading in readings:
                    csv_writer.writerow([wavelength, reading])
    print("Photodiode Readings Finished :)")
    return
    
    
def photodiodeDark(start=400, stepSize = 100, file_name = 'photodiode_dark'):
    """
    Take photodiode readings.

    Args:
        start (int, optional): Wavelength setting start. Defaults to 400.
        stepSize (int, optional): Wavelength setting step size. Defaults to 100.
        file_name (str, optional): csv filename. Defaults to 'photodiode_dark'.
    """
    # Create instrument objects
    monochromator = Monochromator()
    photodiode = Photodiode() 
    
    # List for wavelengths 
    wavelengths = []
    data = {} 
    
    # Directory where data will be saved
    dirPath = 'data/photodiode'
    
    for n in range(start, 700 + stepSize, stepSize):
        photodiode.setWavelength(next) 
        time.sleep(1)
        readings = [] 
        
        # Get 5 minutes of readings in 1s intervals
        for i in range(300):
            readings.append(photodiode.readData()) 
            time.sleep(1) 
            
        if n not in data:
            data[n] = []
        data[n] = readings
        # add csv extension to filename
        file_name += '.csv'  
        filePath = f'{dirPath}/{file_name}'
       
        # Write csv file 
        with open(filePath, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            # Write the header row with column names
            csv_writer.writerow(['Wavelength', 'Readings'])
            # Write data
            for wavelength, readings in data.items():
                for reading in readings:
                    csv_writer.writerow([wavelength, reading])

if __name__ == '__main__':    
    duration = [7,10,12]
    photodiodeDark() 

        
        


        
   