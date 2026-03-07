Algoritmo Numerospares
	//Nuestro objetivo es: Obtener un numero N y mostrar los primeros N numeros
	
	Escribir "Ingresar un numero N:"
	Leer N 
	
	Si N > 0 Entonces
		Para i <- 1 Hasta N Hacer
			numeropar <- i * 2
			Escribir numeropar
		Fin Para
		
	SiNo
		Escribir "	Numero invalido.Debe ser mayor que 0"
	Fin Si
	
FinAlgoritmo
