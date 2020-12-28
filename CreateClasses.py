import os
from datetime import datetime, timedelta

# For every class day the class needs to create a file with
# the name of the class
#      diaStart format init dd/mm/yyyy
#      diaFin format init dd/mm/yyyy

class CreateClasses:
    global weekdays 
    weekdays = ["L","M","X","J","V","S","D"]
    
    def __init__(self, diaStart, diaFin, mascara, directorio, prefijo):
        self.diaStart = diaStart
        self.diaFin = diaFin
        self.mascara = list(mascara.split(","))
        self.directorio = "D:/clases/" + directorio
        self.prefijo = prefijo

    def convertirLista (mascara):
        li = list (mascara.split(","))
        return li

    def createClasses (self):
        diaComienzo = datetime.strptime(self.diaStart , "%d/%m/%Y")
        diaFin = datetime.strptime(self.diaFin, "%d/%m/%Y")

        if not os.path.exists(self.directorio):
            os.makedirs(self.directorio)
        
        while diaFin >= diaComienzo:
            
            if weekdays[diaComienzo.weekday()] in self.mascara:
                filename = self.prefijo + "_clase_" + diaComienzo.strftime("%d_%m") + ".md"

                f = open (os.path.join(self.directorio, filename),"a")
                f.write ("#Clase fecha: " + diaComienzo.strftime("%d_%m"))
                f.close()

            diaComienzo += timedelta(days=1)


