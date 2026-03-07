Algoritmo Diasemana
	//Que se quiere lograr: Recibir un numero del 1 al 7 y mostrar el dia de la semana a cual corresponde
	//Si el numero no es valido, se mostrara un mensaje de error
	
	Escribir "Ingresar un numero del 1 al 7"
	Leer numero
	
	Segun numero Hacer
		1:
			Escribir "Lunes"
		2:
			Escribir "Martes"
		3:
			Escribir "Miercoles"
		4:
			Escribir "Jueves"
	    5: 
			Escribir "Viernes"
		6:
			Escribir "Sabado"
		7:
			Escribir "Domingo"
		De Otro Modo:
			Escribir "Numero invalido. Debe ser entre 1 y 7"
	Fin Segun
	
FinAlgoritmo

