import os
import json
import random
import string

class Toll:

    def __init__(self,Tree):
        self.Tree = Tree
        self.__confinit()

    # Settea la variable de nombre
    def setName(self,name):
        self.name = name
    
    # Settea la variable del valor base
    def setvalueBase(self,valueBase):
        self.valueBase = valueBase
    
    # Settea la variable de incremento del valor izquierdo
    def setIncreLeft(self,increLeft):
        self.increLeft = increLeft
    
    # Settea la variable de incremento del valor derecho
    def setIncreRight(self,increRight):
        self.increRight = increRight

    # Settea la variable de incremento del valor derecho
    def setCategory(self,category):
        self.category = category

    # Configuración inicial para el almacenamiento de peajes
    def __confinit(self):

        if not os.path.exists('File/Toll'):
            os.makedirs('File/Toll')
        
        self.pathToll = 'File//Toll//'
        
    # Guardará un archivo del json
    def save(self):

        tollId = self.__get_random_string()
        jsonFile = {'id': tollId, 'name': self.name, 'valueBase': self.valueBase,'increLeft':self.increLeft,'increRight': self.increRight,'category':self.category}

        with open(self.pathToll+tollId+'.json','w') as json_file:
            json.dump(jsonFile, json_file)

        self.Tree.AgregarPeaje(self.name,tollId,self.valueBase,self.increLeft,self.increRight,self.category)

        return True

    # Obtendra un string único para almacenar el json
    def __get_random_string(self):
        return ''.join(random.choice(string.ascii_letters) for i in range(8))
