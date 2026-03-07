Algoritmo CompararNumeros
	//Objetivo: Solcitar dos numeros y mostrar cual es mayor y cual es menor
	
	Escribir "Ingresar el primer numero"
	Leer num1
	
	Escribir "Ingrese el segundo numero"
	Leer num2
	
	Si num1 > num2  Entonces
		Escribir "El mayor es: num1"
		Escribir "El menor es : num2"
	SiNo
		Si num2 > num2 Entonces
			Escribir "	El mayor es:num1"
			Escribir "El menor es : num2"
		SiNo
			Escribir "Ambos numeros son iguales: num1"
		Fin Si
	Fin Si
	FinAlgoritmo
