import json
import os

class Toll:

    def __init__(self):
        self.__confinit()

    def __init__(self,id,name,valueBase,increLeft,increRight):
        self.id = id
        self.name = name
        self.valueBase = valueBase
        self.increLeft = increLeft
        self.increRight = increRight

        self.__confinit()

    # Configuración inicial para el almacenamiento de peajes
    def __confinit(self):

        if not os.path.exists('File/Toll'):
            os.makedirs('File/Toll')
        
    # Guardará un archivo del json
    def save(self):

        jsonFile = {'id': self.id, 'name': self.name, 'valueBase': self.valueBase,'increLeft':self.valueBase,'increRight': self.increRight}

        with open('File/T_'+self.id+'.json','w') as json_file:
            json.dump(jsonFile, json_file)

