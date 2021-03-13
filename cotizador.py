
edadTitular = int(input("Ingrese su edad:\t"))
seleccionConyuge =input("¿Agrega a su Cónygue:? (si/no)\t")
seleccionHijos =input("¿Agrega a sus hijos? (si/no):\t")
desregulado = input("¿Es desregulado?\t(si/no):\t" )
seleccionPlan = input("¿Que plan quiere cotizar?\n(ej: 2500s, 2500, 4500S, 6500, etc...)\t")
ponderadorAportes = 2.1266660
precio = 0
precioFinal = 0

#listas de precios diciembre 2020
#            0=0 25   1=26 35  2=3654  3=55 59  4=+60     5=h1    6=h2
p2500_24s = [2686.26, 4015.23, 4640.22, 8455.83, 13046.06, 2286.20, 1926.84]
p2500_24  = [3192.44, 4568.54, 5208.29, 9141.36, 14206.27, 2775.17, 2401.70]
p4500_23s = [3605.79, 5404.92, 6425.26, 11399.14, 17082.02, 3085.48, 2617.77] 
p4500_23  = [4111.53, 5955.81, 6992.35, 12057.89,18291.86, 3574.26,	3092.99]    
p6500_21s = [4572.64, 6776.03, 8030.65,	12964.63,19023.86, 3922.73, 3332.08]
p6500_21 =  [5316.83, 7602.99, 8904.73,	14921.62,22219.84, 4642.50,	4029.66]


seleccionPlan = seleccionPlan.upper()
desregulado = desregulado.upper()
seleccionConyuge = seleccionConyuge.upper()
seleccionHijos = seleccionHijos.upper()


if (seleccionPlan == "2500S"):
    seleccionPlan = p2500_24s
elif(seleccionPlan =="2500"):
    seleccionPlan = p2500_24
elif(seleccionPlan =="4500"):
    seleccionPlan =p4500_23
elif(seleccionPlan =="4500S"):
    seleccionPlan =p4500_23s
elif(seleccionPlan =="6500s"):
    seleccionPlan =p6500_21s
else:
    pass


if (edadTitular <26):
    precio = seleccionPlan[0]
elif (edadTitular >25 and edadTitular < 36): 
    precio = seleccionPlan[1]
elif (edadTitular >35 and edadTitular < 55):
    precio =seleccionPlan[2]
elif (edadTitular >54 and edadTitular < 60): 
    precio =seleccionPlan[3]
else:
    precio = seleccionPlan[4]



if (seleccionConyuge == "SI"):
    edadConyuge = int(input("Ingrese la edad de su cónyuge"))
    if (edadConyuge <26):
        cprecio = seleccionPlan[0]
    elif (edadConyuge >25 and edadConyuge < 36): 
        cprecio = seleccionPlan[1]
    elif (edadConyuge >35 and edadConyuge < 55):
        cprecio =seleccionPlan[2]
    elif (edadConyuge >54 and edadConyuge < 60): 
        cprecio =seleccionPlan[3]
    else:
        cprecio = seleccionPlan[4]
else:
    cprecio = 0

if(seleccionHijos == "SI"):
    cantidadHijos = int(input("¿Cuantos hijos agrega?"))
    if (cantidadHijos == 1):
        hprecio = seleccionPlan[5]
    else:
        hprecio = seleccionPlan[5] + seleccionPlan[6]*(cantidadHijos-1)
else:
    hprecio = 0

if(desregulado =="SI"):
    montoAportes = float(input("Ingrese el monto de sus aportes"))
    recupero = montoAportes*ponderadorAportes
else:
    recupero = 0

if seleccionConyuge == "SI" and seleccionHijos == "SI":
    precioFinal = precio + cprecio + hprecio
elif seleccionConyuge =="SI" and seleccionHijos == "NO":
    precioFinal = precio + cprecio
elif seleccionConyuge == "NO" and seleccionHijos == "SI":
    precioFinal = precio + hprecio
else:
    precioFinal = precio


print("El precio de su plan es:\t$", precioFinal)
print("La diferencia a pagar de su plan es:\t$", + precioFinal - recupero)
