Algoritmo ProductoCociente
	//Se nos pide: Solcitar dos numeros y mostrar el porducto y el cociente
	
	Escribir "Ingresar el primer numero"
	Leer num1
	
	Escribir "Ingrese el segundo numero"
	Leer num2
	
	producto <- num1 * num2
	
		Si num2 <> 0 Entonces
			cociente <- num1/num2
			Escribir "El producto de los dos numeros es: producto"
			Escribir "El cociente de los dos numeros es: cociente"
		SiNo
			Escribir "El producto de los dos numeros es: .producto"
			Escribir "No se puede calcular el cociente porque el segundo numero es cero"
		Fin Si
	
	
FinAlgoritmo
