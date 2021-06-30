import os
import json
import random
import string

class Toll:

    def __init__(self):
        self.__confinit()

    def __init__(self,name,valueBase,increLeft,increRight):

        self.name = name
        self.valueBase = valueBase
        self.increLeft = increLeft
        self.increRight = increRight

        self.__confinit()

    # Configuración inicial para el almacenamiento de peajes
    def __confinit(self):

        if not os.path.exists('File/Toll'):
            os.makedirs('File/Toll')
        
        self.pathToll = 'File//Toll//'
        
    # Guardará un archivo del json
    def save(self):

        tollId = self.__get_random_string()
        print(tollId)
        jsonFile = {'id': tollId, 'name': self.name, 'valueBase': self.valueBase,'increLeft':self.valueBase,'increRight': self.increRight}

        with open(self.pathToll+tollId+'.json','w') as json_file:
            json.dump(jsonFile, json_file)

    def __get_random_string(self):
        # With combination of lower and upper case
        return ''.join(random.choice(string.ascii_letters) for i in range(8))
