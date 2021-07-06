import os
import json
import random
import string

class Toll:

    def __init__(self,Tree = None):

        if Tree is not None:
            self.Tree = Tree
        self.__confinit()

    # Settea la variable id
    def __setId(self,id):
        self.id = id

    # Obtiene el id
    def getId(self):
        return self.id

    # Settea la variable de nombre
    def setName(self,name):
        self.name = name
    
    # Obtiene el nombre
    def getName(self):
        return self.name
    
    # Settea la variable del valor base
    def setvalueBase(self,valueBase):
        self.valueBase = valueBase

    # Obtiene la variable del valor base
    def getValueBase(self):
        return self.valueBase
    
    # Settea la variable de incremento del valor izquierdo
    def setIncreLeft(self,increLeft):
        self.increLeft = increLeft

    # Obtiene la variable de incremento del valor izquierdo
    def getIncreLeft(self):
        return self.increLeft
    
    # Settea la variable de incremento del valor derecho
    def setIncreRight(self,increRight):
        self.increRight = increRight

    # Obtiene la variable de incremento del valor derecho
    def getIncreRight(self):
        return self.increRight

    # Settea la variable de incremento del valor derecho
    def setCategory(self,category):
        self.category = category

    # Obtiene la variable de incremento del valor derecho
    def getCategory(self):
        return self.category

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

    # Cargará un peaje desde un archivo json
    def loadFromFile(self,fileName):
        file = open (self.pathToll+fileName, "r")
        data = json.loads(file.read())

        self.__setId(data['id'])
        self.setName(data['name'])
        self.setvalueBase(data['valueBase'])
        self.setIncreLeft(data['increLeft'])
        self.setIncreRight(data['increRight'])
        self.setCategory(data['category'])
        
        # Closing file
        file.close()

    # Obtendra un string único para almacenar el json
    def __get_random_string(self):
        return ''.join(random.choice(string.ascii_letters) for i in range(8))
