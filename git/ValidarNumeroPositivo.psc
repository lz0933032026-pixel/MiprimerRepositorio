Algoritmo ValidarNumeroPositivo
	//Autor: Bayron
	//Fecha: 05/03/26
	//Descripcion:
	//Solcita un numero postivo y valida con Hacer-Mientras
	//que no sea negativo.luego realiza operaciones matematicas:
	//y usa operadores logicos 
	
	Definir numero Como Entero
	Definir suma Como Real 
	Definir resta Como Real
	Definir division Como Real 
	Definir esValido Como Logico 
	
	esValido = Falso 
	
	//Ciclo Hacer-Mientras
	Hacer
		Escribir "Ingrese un numero positivo"
		Leer numero 
		esValido = NO(numero <0) //Se repite mientras el numero sea negativo 
	Mientras que esValido = falso 
	
	
	Escribir "Numero valido ingresado", numero 
	
	suma = numero + 10
	resta = numero - 5
	division = numero / 2
	
	Escribir "Suma:",suma
	Escribir "	Resta:",resta
	Escribir "Division:", division
	
	Si(numero > 0 y numero < 100) o (numero = 200) Entonces 
		Escribir "El numero esta en el rango permitido o es igual a 200"
	SiNo
		Escribir "El numero no cumple las condiciones"
	FinSi
	FinAlgoritmo
	
