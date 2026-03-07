Algoritmo CalificaciondeEstudiantes 
	//Objetivo: Designar nota (0-10) y mostrar resultados
	Repetir
		Escribir "Ingresar la nota del estudiante (0-10) "
		Leer nota
	Hasta Que nota >= 0 y nota <= 10
	
	Si nota >= 6 Entonces 
		Escribir " Aprobado"
	Sino
		Si nota = 5 Entonces
		Escribir "Recuperacion"
	SiNo
		Escribir " Reprobado"
	Fin Si
	FinSi	

	Segun nota Hacer
		0,1,2,3,4:
			Escribir "Resultado (swicth):Reprobado"
			5 :
			Escribir "Resultado (swicth):Recuperacion"
		6,7,8,9,10:
			Escribir "Resultado (swicth):Aprobado"
	Fin Segun
	
	Escribir " Ingresar notas de 3 estudiantes"
	Para i<-1 Hasta 3 Hacer 
		Leer nota
		Si nota >= 6 Entonces 
			Escribir " Estudiante ",i,": Aprobado"
		SiNo
			Si nota = 5 Entonces
				Escribir "Estudiante ",i,":Recuperacion"
			SiNo
				Escribir "Estudiante ",i," : Reprobado"
			FinSi
		Fin Si
	Fin Para
	
	Escribir "Ingresar otra nota valida (0-10) "
	Leer nota
	Mientras (nota < 0) o (nota > 10) Hacer
		Escribir "Nota no valida, intente de nuevo"
		Leer nota
	Fin Mientras
	
	Escribir "Calculamos el promedio de 3 notas"
	suma <- 0
	Para i <-1 Hasta 3 Hacer
		Leer nota
		suma <- suma + nota 
	Fin Para
	promedio <- suma/3
	Escribir "Promedio:",promedio
	
	Si (promedio >= 6) y (promedio <= 10) Entonces
		Escribir " El grupo ha aprobado"
	SiNo
		Escribir " El grupo no alcanzo el promedio asignado"
	Fin Si
	
	
	
	
	
	
FinAlgoritmo
