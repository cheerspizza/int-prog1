### Ejercicio 1
### Pyhton 3.8.2 (default, Feb 26 2020, 02:56:10)
###Pizzaaaaaa
'''
print("¡hola mundo!")
print("pizza suprema de carne")

### Ejercicio 2
x= "Hola Mundo"
print(x)

### Ejercicio 3
nombre= input("¿Como te llamas?")
print("¡Hola", nombre, "Bienvenido!")
print("¡Hola "+ nombre+ " Bienvenido!")

### Ejercicio 4
print(((3+2)/(2*5))**2)

### Ejercicio 5
Horas= int(input("Cuantas horas has trabajado?"))
Precio = int(input("Cuanto vale tu hora laboral?"))
Total_Paga= Horas*Precio
print("Tu pago correspondiente es de $", Total_paga)

### Ejercicio 6
Numero= int(input("ingrese un numero entero positivo"))
suma= round(Numero*(Numero+1)/2)
print('la suma de los primeros numeros de 1 a '+str(Numero)+ ' es', suma)

### Ejercicio 7

Peso= float(input("Ingrese su peso en Kg"))
Estatura= float(input("Ingrese su estatura en metros"))
IMC= round(Peso/(Estatura)**2,2)
print("Su indice de masa corporal es de:", IMC)
'''

### Ejercicio 8
Entero1= int(input("Ingrese el dividendo"))
Entero2= int(input("Ingrese el divisor"))
Cociente= Entero1//Entero2
Resto= Entero1%Entero2
Div= Entero1/Entero2
print("El resultado de la division es: ", Div, "el cociente: ", Cociente, "y el resto: ",Resto)