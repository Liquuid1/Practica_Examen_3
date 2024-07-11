import fun 

op = 0


telefonistas = []

while op!=6:
    fun.menu()
    op = fun.validar_dato_numerico(1,6)

    if op == 1:
        fun.asignar_llamadas(telefonistas)
        print(telefonistas)
    elif op == 2:
        fun.clasificar_llamadas(telefonistas)
    elif op == 3:
        print(3)
    elif op == 4:
        print(4)
    elif op == 5:
        fun.listar_csv(telefonistas)

