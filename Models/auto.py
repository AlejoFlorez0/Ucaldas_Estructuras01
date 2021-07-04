import os
import json
import random
import string

class Auto:

    def __init__(self):
        self.__confinit()

    # Settea la variable de nombre
    def setAutoType(self,autoType):
        self.autoType = autoType
    
    # Settea la variable del valor base
    def setLicensePlate(self,licensePlate):
        self.licensePlate = licensePlate
    
    # Settea la variable de incremento del valor izquierdo
    def setDaySurcharge(self,daySurcharge):
        self.daySurcharge = daySurcharge
    
    # Settea la variable de incremento del valor derecho
    def setNightSurcharge(self,nightSurcharge):
        self.nightSurcharge = nightSurcharge

    # Configuración inicial para el almacenamiento de peajes
    def __confinit(self):

        if not os.path.exists('File/Auto'):
            os.makedirs('File/Auto')
        
        self.pathAuto = 'File//Auto//'

    # Guardará un archivo del json
    def save(self):

        jsonFile = { 'licensePlate': self.licensePlate, 'autoType': self.autoType,'daySurcharge':self.daySurcharge,'nightSurcharge': self.nightSurcharge}

        with open(self.pathAuto+self.licensePlate+'.json','w') as json_file:
            json.dump(jsonFile, json_file)

        return True
