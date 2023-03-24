import os
os.system('cls')
import s12p1modulo


a=s12p1modulo.ClasePersona('Juan',50)
a.muestra()
b=s12p1modulo.ClaseTrabajador('TDR',35000)
b.muestra()

for  x in s12p1modulo.EnumeracionDepartamento:
    print(str(x) + " " + x.name +" " +str(x.value))


class ClaseEmpleado(s12p1modulo.ClasePersona, s12p1modulo.ClaseTrabajador):

    def __init__(self,nombre, edad, codigo, salario,departamento):
        s12p1modulo.ClasePersona.__init__(self,nombre,edad)
        s12p1modulo.ClaseTrabajador.__init__(self, codigo, salario)
        self.dpt=departamento

    def muestra(self):
        print(self.Nombre+" "+str(self.Salario)+" "+str(self.Edad)+" "+ str(self.Codigo)+" "+ str(self.dpt.name))

c=ClaseEmpleado('Juan',50,'TDR',35000, s12p1modulo.EnumeracionDepartamento.tesoreria)
c.muestra()

