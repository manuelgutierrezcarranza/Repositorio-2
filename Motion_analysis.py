#Tomamos un plano bidimensional en el que unicamente tocamos el eje x, la y es una constante (0)
posicion_inicial = float(input("Introduce la posición inicial del objeto: "))
velocidad_inicial = float(input("Introduce la velocidad inicial del objeto: "))
aceleracion_inicial = float(input("Introduce la aceleración inicial del objeto: "))
tiempo = float(input("Introduce el tiempo en el que se da el movimiento: "))
#tomamos tiempo=0 como punto inicial

#usamos las formulas de MRUA para conocer los valores 

velocidad_final = velocidad_inicial + aceleracion_inicial*tiempo
posicion_final = posicion_inicial + velocidad_inicial*tiempo + 0.5*aceleracion_inicial*tiempo**2
aceleracion_final = (velocidad_final - velocidad_inicial)//tiempo

print("posición: ",posicion_final,"m")
print("velocidad: ",velocidad_final," m/s")
print("aceleración: ",aceleracion_final," m/s^2")