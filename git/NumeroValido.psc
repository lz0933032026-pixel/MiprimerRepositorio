Algoritmo NumeroValido
	//Objetivo: Solicitar un numero entre el 1 y el 10 ,y seguirlo pidiendo mientras 
	// el usuario siga ingresando numeros validos , finaliza cuando ingresa
	//un numero imvalido
	
	Escribir "Ingresar un numero entre 1 y10"
	Leer numero
	
	Mientras numero >=1 y numero <= 10 Hacer
		Escribir "Numero valido:",numero
		
		Escribir "Ingrese otro numero entre 1 y 10 (invalido para terminar)"
		Leer numero
		
	FinMientras
	
	Escribir "Numero invalido.El programa ha finalizado."
FinAlgoritmo
