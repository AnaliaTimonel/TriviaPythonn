def usuario():
    print("***BIENVENIDO A TRIVIA PYTHON***")
    nombre=input("Por favor ingrese su nombre: ")
    edad=int(input("Ingrese su edad: "))
    
    
    if edad >=18:
        print(" ")
        
        
        def bienvenida(nombre):
                    print(f"""Hola {nombre}, te damos la bienvenida a este juego de trivia que
                    pondra tus conocimientos sobre Python a prueba.
                    El juego consiste en responder la mayor cantidad de preguntas correctas,
                    teniendo solo la oportunidad de fallar 3 veces! 
          
          
                          ¡¡¡¡ MUCHA SUERTE Y A JUGAAAAR =) !!!!""")
        bienvenida(nombre)

        def preguntas_juego():
              import random
              preguntas= ["¿Que es un algoritmo? RESPUESTAS:A- es un conjunto ordenado de instrucciones para solucionar un problema.B: es una funcion que permite iterar valores",
              "¿Cual es la palabra reservada para crear una funcion? RESPUESTAS:A- int . B- def",
              "¿ Cual es la funcion del BREAK dentro de un bucle while? RESPUESTAS:A-permite saltear iteraciones que cumplan con un condicional.B-el Break corta la ejecucion una vez se cumpla una condicion",
              "¿Que es una funcion LAMBDA?RESPUESTAS:A-es una funcion anonima, en una sola linea. B- es una funcion que cuenta los valores de una cadena",
              "¿Para que sirven los PARAMETROS y ARGUMENTOS?RESPUESTAS:A- sirven para verificar si un valor esta dentro de una lista o diccionario. B-para pasar datos que utilizaremos en las funciones",
              "¿Que funcion cumple la funcion RANGE?RESPUESTAS: A- se utiliza para generar una secuencia de números enteros.B- se utiliza para organizar los datos de forma ascendente",
              "¿Que hace la funcion LEN? RESPUESTA A: devuelve el numero de valores de un elemento iterable. B- nos marca en que indice se encuentra un valor"]
              respuestas= ["a","b","b","a","b","a","a"]
              preguntas_respuestas=(preguntas[0],respuestas[0]),(preguntas[1],respuestas[1]),(preguntas[2],respuestas[2]),(preguntas[3],respuestas[3]),(preguntas[4],respuestas[4]),(preguntas[5],respuestas[5]),(preguntas[6],respuestas[6])
              random.shuffle(preguntas)
              
              puntos=0
              vidas=3
              while vidas!= 0:
                   
               for p,r in preguntas_respuestas:
                  print("                                                                                    ")
                  print("* Pregunta:", p)
                  print("                                                                                    ")
                  respuesta_usuario=input("Ingrese su repuesta: ")
                  respuesta_usuario.lower()
                  if respuesta_usuario== r:
                     puntos+=1
                     
                     print("Su repuesta en correcta!!!")
                     print("                                    ")
                     print(f"Puntos:{puntos}")
                  else:
                   print("                                    ")
                   print("Respuesta incorrecta, la respuesta correcta es", r)
                   vidas-=1
                   
                   print("                                    ")
                   print(f"Usted tiene {vidas} vidas =( ")
                  if vidas==0:
                     break
                 
                  
              print(f"Su puntaje final es de {puntos}")    
              print("                                         ")
              print("FIN DEL JUEGO, HASTA LA PROXIMA!!!")
              
        preguntas_juego()
  
        
    else:
         print("Usted no cumple con el requisito de edad minima, hasta pronto!")
        
        
    
usuario()