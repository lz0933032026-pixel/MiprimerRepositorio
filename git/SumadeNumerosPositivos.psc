Algoritmo SumadeNumerosPositivos 
	//Objetivo a lograr: Ingresar numeros continuamnete hasta que se
	// ingrese un numero negativo, para posteriormente mostrar la suma de todos los numeros positivos ingresados
	
	suma <- 0
	
	Repetir
		Escribir" Ingrese un numero(negativo para terminar)"
		Leer numero
	
		Si numero >= 0 Entonces
			suma <- suma + numero
		Fin Si
		
	Hasta Que numero < 0
	
	Escribir "La suma de los numeros positivos ingresados es:",suma
	  
FinAlgoritmo
