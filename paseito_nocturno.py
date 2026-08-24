import random
from operator import truediv
from random import randint

titulo = "¡Bienvenido a Evening Stroll!"
print("\n" + titulo + "\n" + "-" * len(titulo))
enter = input(r"""
         / \__
         (    @\___
         /         O
        /   (_____/
       /_____/   U

Presiona ENTER para Comenzar:""")

print("""
Una noche como cualquier otra, decides ir a dar una caminata por un bosque oscuro con tu perro, Roco, porque te aburres muchísimo. 
De repente, escuchas las hojas secas de los árboles crujir detrás de ti. ¡Un hombre encapuchado, con un hacha y una pipa, aparece de entre los árboles! 
Antes de que puedas reaccionar, el hombre mata a Roco :( y comienza a dirigirse hacia ti... 
      """)

# Reacción a la muerte de Roco
reaccion_mr = input(r"""           
   ¡Elige rápido qué hacer!

      (a) Huir hacia una cueva cercana.
      (b) Huir hacia un túnel bajo las raíces de un árbol gigante.
      (c) Enfrentar al hombre.

                ¯\_(ツ)_/¯
                
Teclea a, b o c:
""")

while reaccion_mr.lower() != "a" and reaccion_mr.lower() != "b" and reaccion_mr.lower() != "c":
    reaccion_mr = input(" {} No es un carácter válido. Por favor, introduce a, b o c: " .format(reaccion_mr))

# Camino de la cueva
if reaccion_mr.lower() == "a":
    objeto_brillante = input(r"""
   Encuentras un camino húmedo y oscuro. A lo lejos, ves algo que brilla peligrosamente en el suelo.

                     ~ ~ ~ ~
                   /         \
                  /           \
                 |    O   O    |
                 |     __      |
                  \___________/

      (a) Examinar el objeto brillante. 
      (b) Ignorar el objeto y seguir avanzando.

   Escribe a o b: 
""")

    while objeto_brillante.lower() != "a" and objeto_brillante.lower() != "b":
        objeto_brillante = input(" {} No es un carácter válido. Por favor, introduce a o b: ".format(objeto_brillante))

# Objeto brillante bajo el árbol
    cuchillo = False
    if objeto_brillante.lower() == "a":
        cuchillo = input(r"""
   Es un cuchillo oxidado cubierto de fósforo. ¿Lo quieres recoger? 

                     ________
                  _ /  _____ \
                 | \__/     \_|
                  \   o  o   /
                   |________|

   Escribe S para llevártelo o N para dejarlo en la cueva: 
   """)

        while cuchillo.lower() != "s" and cuchillo.lower() != "n":
            cuchillo = input(" {} No es un carácter válido. Por favor, introduce S o N: ".format(cuchillo))


# Agarrar cuchillo
        if cuchillo.lower() == "s":
            print(r"""
   ¡¡¡Felicidades! Ahora llevas un cuchillo con muy mala pinta en tu bolsillo.

                        ________
                     _ /  _____ \
                    | \__/     \_|
                     \   >  <   /
                      |________|
                      
            """)
            cuchillo = True
        elif cuchillo.lower() == "n":
            print(r"""
   Sigues corriendo sin mirar atrás.

                   O
                  /|\\
                  / \\
                  
""")
            cuchillo = False
        else:
            print("Por favor, introduce los caracteres admitidos.\nInténtalo nuevamente.")
            exit()

    # No observar objeto brillante
    elif objeto_brillante.lower() == "b":
        print(r"""
   Sigues corriendo para poder sobrevivir.

                   O
                  /|\\
                  / \\
                     
""")

        cuchillo = False

    else:
        print("Por favor, introduce los caracteres admitidos.\nInténtalo nuevamente.")
        exit()

# Lobo en la salida
    lobo = input(r"""
   Sigues avanzando, pero el hombre con capucha saca una navaja y no para de perseguirte. 
   Al final del camino, te encuentras con un obstáculo...

                     /\_____/\
                    /         \
                   /   O   O   \
                  /     >^<     \
                 /_______________\
                /                 \
               /                   \

   ¡Hay un lobo en la salida de la cueva! ¿Qué quieres hacer?

      (a) Usar el cuchillo oxidado. 
      (b) Intentar pasar corriendo. 

   Escribe a o b: 
""")
    while lobo.lower() != "a" and lobo.lower() != "b":
        lobo = input(" {} No es un carácter válido. Por favor, introduce a o b: ".format(lobo))

    numero_random_lobo = random.randint(1, 100)
    if lobo.lower() == "a" and cuchillo == True:
        print(r"""
   Si quieres salir con vida, debes matar al lobo. 
   Para poder hacerlo, debes clavarle el cuchillo de manera acertada.

                     ________
                  _ /  _____ \
                 | \__/     \_|
                  \   X  X   /
                   |________|

   ¡Rápido! Tu vida depende de ello. ¿Cuánto es 3 * {}?
        
""".format(numero_random_lobo))

        multiplicacion_1 = int(
            input("¿Cuál es el resultado?: "))  # resultado de la multiplicación randint para matar al lobo

        if multiplicacion_1 == (3 * numero_random_lobo):
            print(r"""
   ¡Has estado cerca! Has logrado esquivar al lobo y seguir escapando del hombre con capucha.

                            O
                           /|\\
                           / \\
   
""")
        else:
            print(r"""
   No has logrado zafarte de las garras del lobo, 
   pero, por lo menos, te has convertido en comida de una familia canina. :)

                     ________
                  _ /  _____ \
                 | \__/     \_|
                  \   X  X   /
                   |________|
                      
""")
            exit()

    elif lobo.lower() == "a" and cuchillo == False:
        print(r"""
   El lobo te ataca sin piedad y recuerdas que no agarraste el cuchillo, pero aún tienes una posibilidad de zafarte de sus garras con tu fuerza mental.
   
                     ________
                  _ /  _____ \
                 | \__/     \_|
                  \   o  o   /
                   |________|
                   
   Para poder hacerlo, debes resolver la siguiente operación 6 * {}:

""".format(numero_random_lobo))

        multiplicacion_2 = int(input("¿Cuál es el resultado?: "))

        if multiplicacion_2 == (6 * numero_random_lobo):
            print(r"""
   ¡Ha estado cerca! Has logrado escapar del lobo y seguir escapando del hombre con capucha.

                          O
                         /|\\
                         / \\
                         
                """)
        else:
            print(r"""
   No has logrado escapar de las garras del lobo, 
   pero, por lo menos, te has convertido en comida de una familia canina. :)

                         ________
                      _ /  _____ \
                     | \__/     \_|
                      \   X  X   /
                       |________|
                       
                """)
            exit()

    elif lobo.lower() == "b":
        print(r"""
   El lobo te ataca sin piedad, pero aún tienes una posibilidad de zafarte de sus garras con tu fuerza mental.

                     ________
                  _ /  _____ \
                 | \__/     \_|
                  \   o  o   /
                   |________|
                   
   Para poder hacerlo, debes resolver la siguiente operación 5 * {}:

""".format(numero_random_lobo))

        multiplicacion_2 = int(input("¿Cuál es el resultado?: "))

        if multiplicacion_2 == (5 * numero_random_lobo):
            print(r"""
   ¡Ha estado cerca! Has logrado escapar del lobo y seguir escapando del hombre con capucha.

                      O
                     /|\\
                     / \\
                     
""")
        else:
            print(r"""
   No has logrado escapar de las garras del lobo, 
   pero, por lo menos, te has convertido en comida de una familia canina. :)

                     ________
                  _ /  _____ \
                 | \__/     \_|
                  \   X  X   /
                   |________|
                   
""")
            exit()

# Caracter erróneo
    else:
        print("Por favor, introduce los caracteres admitidos.\nInténtalo nuevamente.")
        exit()


if reaccion_mr.lower() == "b":
    rama_puntiaguda = input(r"""
   El túnel bajo las raíces es angosto y caliente. Al seguir avanzando, en un rincón, ves una rama puntiaguda sobresaliendo de las raíces del árbol.

                /\
               /  \   Raíces caídas
              /____\________
              ||    |  <== Entrada del túnel
              ||____|
              
      (a) ¿Quieres tomar la rama puntiaguda?
      (b) Seguir avanzando sin tomar nada.

   Teclea a o b: 
""")

    while rama_puntiaguda.lower() != "a" and rama_puntiaguda.lower() != "b":
        rama_puntiaguda = input(" {} No es un carácter válido. Por favor, introduce a o b: ".format(rama_puntiaguda))

# Agarrar rama
    rama = False
    if rama_puntiaguda.lower() == "a":
        print(r"""
   ¡¡Felicidades! Ahora llevas una rama húmeda y puntiaguda en tu bolsillo.

                         //\\
                        ||  ||
                        ||  ||
                         \\//
                          ||
                
    """)

        rama = True

    elif rama_puntiaguda.lower() == "b":
        print("Sigues corriendo sin parar.")
        rama = False
    else:
        print("Por favor, introduce los caracteres admitidos.\nInténtalo nuevamente.")
        exit()

# Obstáculo en el árbol
    muro = input(r"""
   Sigues huyendo sin parar y, de la nada, te percatas de que hay un muro bloqueando la salida del túnel. ¿Qué quieres hacer?

      (a) Usar la rama puntiaguda para mover las rocas.
      (b) Intentar mover las rocas con las manos.

                    ###########
                    # #  #  # # 
                    ###########
                    # ## #  # #
                    ###########
          
   Teclea a o b:
""")

    while muro.lower() != "a" and muro.lower() != "b":
        muro = input(" {} No es un carácter válido. Por favor, introduce a o b: ".format(muro))

# User ha elegido tumbar el muro con la rama
    numero_random_muro = randint(1, 100)
    if muro.lower() == "a" and rama == True:
        muro_rama = int(input("""
   Tienes que descifrar en qué fila de rocas del muro debes usar tu rama como palanca!
   
                    ###########
                    # #  #  # # 
                    ###########
                    # ## #  # #
                    ###########

      RÁPIDO, ¿CUÁNTO ES 2*{}:
      
""".format(numero_random_muro)))

        multiplicacion_muro_rama = 2 * numero_random_muro

        if muro_rama == multiplicacion_muro_rama:
            print(r"""
   ¡¡OLE! La respuesta era {}, y has logrado seguir escapando.

              O
             /|\
             / \\
             
""".format(multiplicacion_muro_rama))

        else:
            print(r"""
   Lamentablemente, la respuesta era {}. :(
   Te has quedado atrapado y descubres que el hombre encapuchado era Dalas. No le ha bastado con destruir a tu perro, así que decide 
   destruir tu reputación publicando en un hilo de X todos tus secretos por tu poca capacidad para multiplicar.

                     ________
                  _ /  _____ \
                 | \__/     \_|
                  \   X  X   /
                   |________|
             
""".format(multiplicacion_muro_rama))
            exit()

# User quiere tumbar el muro con la rama, pero no tiene rama
    elif muro.lower() == "a" and rama == False:
        muro_mano = int(input("""
   Aúnque anteriormente no agarraste la rama, aun puedes escaparte. Calcula qué piedra debes quitar del muro para derribarlo entero.

      PIENSA RÁPIDO, ¿CUÁNTO ES 2 * {} + 7:
           
""".format(numero_random_muro)))

        multiplicacion_muro_mano = 2 * numero_random_muro + 7

        if muro_mano == multiplicacion_muro_mano:
            print(r"""
   ¡¡OLE! La respuesta era {}, y has logrado seguir escapando.

                   O
                  /|\
                  / \\
                  
""".format(multiplicacion_muro_mano))

        else:
            print(r"""
   Lamentablemente, la respuesta era {}. :(
   Te has quedado atrapado y descubres que el hombre encapuchado era Dalas. No le ha bastado con destruir a tu perro, así que decide 
   destruir tu reputación publicando en un hilo de X todos tus secretos por tu poca capacidad para multiplicar.

                     ________
                  _ /  _____ \
                 | \__/     \_|
                  \   X  X   /
                   |________|
                   
            """.format(multiplicacion_muro_mano))
            exit()

# User ha elegido tumbar el muro con las manos
    elif muro.lower() == "b":
        muro_mano = int(input("""
   Aún te da tiempo de lograrlo; solo debes calcular qué piedra debes quitar del muro para derribarlo entero.

      PIENSA RÁPIDO, ¿CUÁNTO ES 2 * {} + 7:
      
        """.format(numero_random_muro)))

        multiplicacion_muro_mano = 2 * numero_random_muro + 7

        if muro_mano == multiplicacion_muro_mano:
            print(r"""
   ¡¡OLE! La respuesta era {}, y has logrado seguir escapando.

                      O
                     /|\
                     / \\

""".format(multiplicacion_muro_mano))

        else:
            print(r"""
   Lamentablemente, la respuesta era {}. :(
   Te has quedado atrapado y descubres que el hombre encapuchado era Dalas. No le ha bastado con destruir a tu perro, así que decide 
   destruir tu reputación publicando en un hilo de X todos tus secretos por tu poca capacidad para multiplicar.

                     ________
                  _ /  _____ \
                 | \__/     \_|
                  \   X  X   /
                   |________|
             
""".format(multiplicacion_muro_mano))
            exit()


#3 ARCO DE PARARSE DURO POR ROCO

numero_random_yuyitsu = randint(1, 50)

if reaccion_mr.lower() == "c" :
   atacar = int(input("""
   ¡Menudo coraje, colega! Aúnque sea arriesgado, te abalanzas sobre el hombre encapuchado y, con todas tus fuerzas, tratas de derribarlo.
   Si resuelves la siguiente operación aritmética, a lo mejor podrías ganarle: 
    
      TU VIDA DEPENDE DE ESTO (4 * {}) / 2 + 5:
      
""".format(numero_random_yuyitsu)))

   multiplicacion_ataque = (4 * numero_random_yuyitsu) / 2 + 5

   if atacar == multiplicacion_ataque :
       print(r"""
   Espabila, tío. ¿Cómo crees que el hombre de la capucha ha matado a Roco?
   A pesar de tus buenas matemáticas, tu pecho no está preparado para soportar navajazos. Mueres lentamente desangrado.
          
                                 ___       /|
                                  O       / |      ø
                                 /|\     /  |      /x\
                                 / \     |==|      / \
                                 | |     \__|
                                    
   Inténtalo de nuevo :)                                    
""")
       exit()

   else:
       print (r"""
       
   Te abalanzas sobre el hombre encapuchado y, con todas tus fuerzas, tratas de derribarlo, pero, lamentablemente, eres horroroso en matemáticas...
   Sientes cómo algo te atraviesa el lado izquierdo del pecho. Te han clavado una navaja y mueres lenta y dolorosamente.
      
      
                                 ___       /|
                                  O       / |       ø
                                 /|\     /  |      /x\
                                 / \     |==|      / \
                                 | |     \__|
             
             
   Inténtalo de nuevo :)   
""")
       exit()

# Finales
escondite = input("""

   Por fin logras salir del bosque y lo primero que ves es una tienda de kebabs y un Juan Valdez.
      
      (a) Esconderte con los turcos.
      (b) Esconderte con los cafeteros.

 Teclea a o b:
 """)

while escondite.lower() != "a" and escondite.lower() != "b":
    escondite = input(" {} No es un carácter válido. Por favor, introduce a o b: ".format(escondite))


# Arco de los turcos

if escondite.lower() == "a" :
    turquia = input(r"""
   El hombre con capucha entra al kebab, se quita la capucha y se lleva las manos a la cabeza. 
   Se quita lentamente la capucha y descubres que es DALAS... ¡¡¿¿Qué??!!

                   _______
                 /        \
                /   O   O  \
                |     ^     |  Dalas Review
                |    ___    |
                 \_________/
             
   Rápido, está a punto de atacarte.
    
       (a) Le tiras un kebab
       (b) Le tiras una botella de Fanta
      
    Teclea a o b:
""")

    while turquia.lower() != "a" and turquia.lower() != "b":
        turquia = input("{} No es un carácter válido. Por favor, introduce a o b: ".format(turquia))

    if turquia.lower() == "a" :
        kbab = input(r"""
        
   Dalas tenía hambre, así que se come el kebab.

      (a) Le haces una foto y le hundes la reputación en X por matar a Roco?
      (b) Lo atacas sin piedad por haber matado a Roco
      
                                  ________
                                 /        \
                                |  KEBAB   |
                                |   | |    |
                                |  | | |   |
                                |  | | |   |
                                 \ ______ /
        
   Teclea a o b:
""")

        while kbab.lower() != "a" and kbab.lower() != "b":
            kbab = input("{} No es un carácter válido. Por favor, introduce a o b: ".format(kbab))

        if kbab.lower() == "a" :
            print("""
   De puta madre, has destrozado la carrera de Dalas vengando a Roco y has sobrevivido. ¡Vamos por un tinto de verano para celebrar!
   
                                   .     .     .  
                                . '.   .   . '.  .
                                 .   . '.    .   .  
                                .   .   . '.     .
                              *     .     .     .    *
                              .   '.     . '.   .    .
                                .   .    .   .    .  
                                .  '.   .   . '.  .
                                    *     .    *
                                    
""")

        elif kbab.lower() == "b" :
            print(r"""
   Empujas a Dalas y su cabeza cae en el bordillo de una mesa, lo que lo mata automáticamente :0. 
   Has logrado vengar a Roco, pero, por desgracia, has terminado en la cárcel en el proceso.
   
                            | | | | | | | | |
                            | | | | | | | | |
                            | | | | | | | | |           X_X
                            | | | | | | | | |           /|\
                            | | | | | | | | |           / \\
                            | | | | | | | | |
                            | | | | | | | | |    
                            
   Fin del juego

""")
            exit()
        else:
            print("Por favor, introduce los caracteres admitidos.\nInténtalo nuevamente.")
            exit()

    elif turquia.lower() == "b" :
        print(r"""
   Dalas se enoja por el exceso de azúcar que le acabas de lanzar y explota, matándose a sí mismo, a los turcos y a ti...
   
                       _______
                      /       \
                     |  FANTA  |                      X_X
                     |         |                      /|\
                     |         |                      / \
                      \_______/
                          |
                          |
                         / \  
        
   Fin del juego.
""")
        exit()

    else:
        print("Por favor, introduce los caracteres admitidos.\nInténtalo nuevamente.")
        exit()


# Arco del Cafe

elif escondite.lower() == "b" :
    colombia = input(r"""
   El hombre con capucha entra al Juan Valdez y se lleva las manos a la cabeza. 
   Se quita lentamente la capucha y descubres que es DALAS... ¡¡¿¿Qué??!!

                   _______
                 /        \
                /   O   O  \
                |     ^     |  Dalas Review
                |    ___    |
                 \_________/

   Rápido, está a punto de atacarte.
   
      (a) Le tiras un capuchino
      (b) Le tiras una mesera
    
    Teclea a o b:
""")

    while colombia.lower() != "a" and colombia.lower() != "b":
        colombia = input(" {} No es un carácter válido. Por favor, introduce a o b: ".format(colombia))


    if colombia.lower() == "a":
        print(r"""
   Dalas se enoja porque odia la cafeína y explota, destruyéndose a sí mismo, a los colombianos y a ti...
   
                                   x   x     x   x     x   x    
                                    \_/       \_/       \_/
                                    
""")
        exit()
    elif colombia.lower() == "b":
        mesera = input(r"""    
   Dalas se ha distraído completamente con la mesera.
   
                     O
                    /|\
                    / \
                 ( Mesera )

      (a) Le haces una foto con la mesera y le hundes la reputación en X por asesino y simp.
      (b) Lo atacas sin piedad mientras está distraído por haber matado a Roco.


   Teclea a o b:
""")
        while mesera.lower() != "a" and mesera.lower() != "b":
            mesera = input(
                " {} No es un carácter válido. Por favor, introduce a o b: ".format(mesera))

        if mesera.lower() == "a" :
            print("""
   De puta madre, has destrozado la carrera de Dalas; todos sus enemigos se han cargado todo lo que amaba.  
   
                                   .     .     .  
                                . '.   .   . '.  .
                                 .   . '.    .   .  
                                .   .   . '.     .
                              *     .     .     .    *
                             .   '.     . '.   .    .
                                .   .    .   .    .  
                                .  '.   .   . '.  .
                                    *     .    *
                 
""")# las feministas y los animalistas
        elif mesera.lower()== "b" :
            print("""
   Lo empujas, pero Dalas tiene más fuerza de la que creías. Logra tirarte al suelo y te clava su navaja en el pecho. Has muerto... 
""")
            #destroza la mandibula
        else:
            print("Por favor, introduce los caracteres admitidos.\nInténtalo nuevamente.")
            exit()
    else:
        print("Por favor, introduce los caracteres admitidos.\nInténtalo nuevamente.")
        exit()
else:
    print("Por favor, introduce los caracteres admitidos.\nInténtalo nuevamente.")
    exit()



#Coded in a 75% keyboard with brown tactile switches in a hotswapabble board (probably from an unknown fabric in China)
# looking as less as possible the cheap white ABS key caps to practice my typography in Rottweil, Germany
#Coded by Paco (Pacode)
