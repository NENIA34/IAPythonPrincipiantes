# # Identifica y corrige los errores en el código proporcionado.
# class Coche:
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo

#     def obtener_informacion(self):
#         print(f"Coche: {marca} {modelo}")
    
# mi_coche = Coche("Toyota", "Corolla")
# mi_coche.obtener_informacion()



class Coche:           
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
       
    def __str__(self):
        return f"Coche: {self.marca} {self.modelo}"

    def obtener_informacion(self):
        print(f"Coche: {self.marca} {self.modelo}")    

mi_coche = Coche("Toyota", "Corolla")

print(mi_coche)
# Para que la clase Coche devuelva un string luego de pasarle los parámetros, usar el método 
# __str__ de la clase, que es un método especial que se llama automáticamente cuando se intenta
# convertir un objeto a string.
# Como la clase Coche me devuelve un string, entonces puedo imprimir el objeto mi_coche, ya que
# aparentemente es un objeto de tipo string. Pero no es así. El objeto mi_coche no es un objeto
# de tipo string, sino que es un objeto de tipo Coche. 
# Sin embargo, la clase Coche tiene un método __str__ que se encarga de convertir el objeto a 
# un string cuando se intenta imprimir. En Python, cuando se imprime un objeto, se llama 
# automáticamente al método __str__ de la clase del objeto para obtener una representación en 
# string del objeto. Por lo tanto, cuando imprimes mi_coche, se llama al método __str__ de la 
# clase Coche, que devuelve el string "Coche: Toyota Corolla". Así que, aunque mi_coche no es un
# objeto de tipo string, se puede imprimir como si lo fuera gracias al método __str__ de la 
# clase Coche.