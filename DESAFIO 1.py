
# # Convierte de Programación estructurada a POO
# def calcular_area_triangulo(base, altura):
#     return (base * altura) / 2
# def calcular_area_rectangulo(base, altura):
#     return base * altura
# base_triangulo = 5
# altura_triangulo = 8
# area_triangulo = calcular_area_triangulo (base_triangulo, altura_triangulo)
# print(f"Área del triángulo: {area_triangulo}")
# base_rectangulo = 6
# altura_rectangulo = 4
# area_rectangulo = calcular_area_rectangulo (base_rectangulo, altura_rectangulo)
# print(f"Área del rectángulo: {area_rectangulo}")


class AreaTriangulo:
    #
	# Quiero llamar a la clase AreaTriangulo como si fuera una función 
	# y obtener un valor numérico, sin tener que conocer los nombres de los 
	# métodos internos de la clase. Para lograr esto, se usa el método especial 
	# __call__ en la clase AreaTriangulo. Este método se llama automáticamente cuando
	# se intenta llamar a la clase como si fuera una función. El método __call__ 
	# devuelve el resultado del método calcular_area del triángulo. Nota que, 
	# en este caso, no necesitas crear un objeto de la clase AreaTriangulo explícitamente. 
	# La clase se comporta como una función que devuelve un valor numérico cuando 
	# se la llama con los parámetros correspondientes.
    def __init__(self, base, altura):
        # El método __init__ se utiliza para inicializar las variables de instancia.
		#  En este código, el método __init__ guarda los parámetros base y altura como 
		# atributos de la clase, y el método __call__ utiliza estos atributos para calcular 
		# el área. Nota que, en este caso, debes llamar a la clase AreaTriangulo con los
		# parámetros base y altura, y luego llamar al método __call__ utilizando los 
		# paréntesis () para obtener el resultado numérico.
		# Self: Si tuviéramos la clase Persona,self se refiere al objeto Persona que se está 
		# creando o utilizando, y puede acceder a todos sus atributos y métodos, como 
		# nombre, edad, direccion, saludar y mostrar_direccion. Así que, en resumen, 
		# self no es solo una variable, sino que es una referencia a un objeto complejo 
		# que puede tener múltiples atributos y métodos. Cuando se utiliza self en un 
		# método, se está accediendo a los múltiples atributos y métodos del objeto que 
		# se está creando o utilizando.
		# El método calcular_area depende de self, única variable, para definir las 
		# variables base y altura, se deberían asignar los valores de los parámetros
		#  a estas variables, de la siguiente manera:
        self.base = base
        self.altura = altura    
    def calcular_area(self):		
        area = self.base * self.altura / 2
        return area
    def __call__(self):
        return self.calcular_area()

class AreaRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area
    def __call__(self):
        return self.calcular_area()

# Crear objetos
base_triangulo = 5
altura_triangulo = 8
AreaTriang = AreaTriangulo(base_triangulo, altura_triangulo) # Crear objetos, ahora si quiero poder usar la clase cual si fuera 
#una función, y hacer un print(AreaTriangulo(5,8)), debo agregar a la definición de la clase el método def __call__(self): con sig
# linea indentada return self.calcular_area(), hay otros métodos con distintos usos como __str__ o __repr__
print(f"Area del triángulo: {AreaTriang()}")

base_rectangulo = 6
altura_rectangulo = 4
AreaRectan = AreaRectangulo(base_rectangulo, altura_rectangulo) # esto es un objeto  no lo imprime salvo que agregue ()
print(f"Base del rectángulo:, {base_rectangulo}")
print(f"Altura del rectángulo: {altura_rectangulo}")
print(f"Area del triángulo: {AreaRectan()}")	# Los () le dicen a Python: "ejecuta esta función y usa su valor retornado".
# Si la función requiriera parámetros, irían dentro de los paréntesis: print(f"Area del rectángulo: {AreaRectan()}")