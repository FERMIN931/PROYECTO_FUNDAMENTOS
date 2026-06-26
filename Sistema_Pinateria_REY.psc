Proceso Sistema_Pinateria_REY
	
	Definir opcion, i, nProductos, nVentas, nPedidos Como Entero
	Definir cantidad, pos Como Entero
	Definir total, totalVentas, anticipo Como Real
	Definir codigo, nombre, categoria, evento Como Cadena
	Definir cliente, tipoEvento, fechaEvento, detalle Como Cadena
	Definir textoBuscar Como Cadena
	Definir encontrado Como Logico
	
	Definir codigos, nombres, categorias, eventos Como Cadena
	Dimension codigos[100], nombres[100], categorias[100], eventos[100]
	
	Definir precios Como Real
	Dimension precios[100]
	
	Definir stocks Como Entero
	Dimension stocks[100]
	
	Definir ventaProducto Como Cadena
	Dimension ventaProducto[300]
	
	Definir ventaCantidad Como Entero
	Dimension ventaCantidad[300]
	
	Definir ventaTotal Como Real
	Dimension ventaTotal[300]
	
	Definir pedidoCliente, pedidoEvento Como Cadena
	Dimension pedidoCliente[100], pedidoEvento[100]
	
	Definir pedidoAnticipo Como Real
	Dimension pedidoAnticipo[100]
	
	nProductos <- 10
	nVentas <- 0
	nPedidos <- 0
	
	codigos[1] <- "R001"
	nombres[1] <- "Piñata mediana"
	categorias[1] <- "Piñatas"
	eventos[1] <- "Cumpleaños"
	precios[1] <- 45
	stocks[1] <- 20
	
	codigos[2] <- "R002"
	nombres[2] <- "Globo metalizado"
	categorias[2] <- "Globos"
	eventos[2] <- "Cumpleaños"
	precios[2] <- 12
	stocks[2] <- 80
	
	codigos[3] <- "R003"
	nombres[3] <- "Cinta decorativa"
	categorias[3] <- "Decoración"
	eventos[3] <- "Matrimonio"
	precios[3] <- 8.5
	stocks[3] <- 50
	
	codigos[4] <- "R004"
	nombres[4] <- "Caja sorpresa"
	categorias[4] <- "Regalos"
	eventos[4] <- "Día de la Madre"
	precios[4] <- 35
	stocks[4] <- 25
	
	codigos[5] <- "R005"
	nombres[5] <- "Taza personalizada"
	categorias[5] <- "Regalos"
	eventos[5] <- "Día del Profesor"
	precios[5] <- 18
	stocks[5] <- 30
	
	codigos[6] <- "R006"
	nombres[6] <- "Guirnalda de colores"
	categorias[6] <- "Decoración"
	eventos[6] <- "Cumpleaños"
	precios[6] <- 15
	stocks[6] <- 40
	
	codigos[7] <- "R007"
	nombres[7] <- "Bolsa para sorpresa"
	categorias[7] <- "Fiesta infantil"
	eventos[7] <- "Cumpleaños"
	precios[7] <- 2
	stocks[7] <- 100
	
	codigos[8] <- "R008"
	nombres[8] <- "Adorno para torta"
	categorias[8] <- "Accesorios"
	eventos[8] <- "Cumpleaños"
	precios[8] <- 10
	stocks[8] <- 35
	
	codigos[9] <- "R009"
	nombres[9] <- "Set de decoración"
	categorias[9] <- "Decoración"
	eventos[9] <- "Día del Padre"
	precios[9] <- 28
	stocks[9] <- 22
	
	codigos[10] <- "R010"
	nombres[10] <- "Recuerdo para matrimonio"
	categorias[10] <- "Recuerdos"
	eventos[10] <- "Matrimonio"
	precios[10] <- 6
	stocks[10] <- 60
	
	Repetir
		
		Escribir ""
		Escribir "====================================="
		Escribir "       SISTEMA PIÑATERÍA REY"
		Escribir "====================================="
		Escribir "1. Registrar producto"
		Escribir "2. Listar productos"
		Escribir "3. Registrar venta"
		Escribir "4. Registrar pedido"
		Escribir "5. Buscar producto"
		Escribir "6. Generar reporte"
		Escribir "7. Cargar 50 ventas simuladas"
		Escribir "8. Salir"
		Escribir "Seleccione una opción:"
		Leer opcion
		
		Segun opcion Hacer
			
			1:
				Escribir ""
				Escribir "--- REGISTRAR PRODUCTO ---"
				Escribir "Ingrese código del producto:"
				Leer codigo
				
				encontrado <- Falso
				
				Para i <- 1 Hasta nProductos Hacer
					Si codigos[i] = codigo Entonces
						encontrado <- Verdadero
					FinSi
				FinPara
				
				Si encontrado = Verdadero Entonces
					Escribir "El producto ya existe."
				Sino
					nProductos <- nProductos + 1
					
					Escribir "Ingrese nombre del producto:"
					Leer nombres[nProductos]
					
					Escribir "Ingrese categoría:"
					Leer categorias[nProductos]
					
					Escribir "Ingrese evento relacionado:"
					Leer eventos[nProductos]
					
					Repetir
						Escribir "Ingrese precio:"
						Leer precios[nProductos]
					Hasta Que precios[nProductos] > 0
					
					Repetir
						Escribir "Ingrese stock:"
						Leer stocks[nProductos]
					Hasta Que stocks[nProductos] >= 0
					
					codigos[nProductos] <- codigo
					
					Escribir "Producto registrado correctamente."
				FinSi
				
			2:
				Escribir ""
				Escribir "--- LISTA DE PRODUCTOS ---"
				
				Para i <- 1 Hasta nProductos Hacer
					Escribir "Código: ", codigos[i]
					Escribir "Producto: ", nombres[i]
					Escribir "Categoría: ", categorias[i]
					Escribir "Evento: ", eventos[i]
					Escribir "Precio: S/ ", precios[i]
					Escribir "Stock: ", stocks[i]
					Escribir "-----------------------------"
				FinPara
				
			3:
				Escribir ""
				Escribir "--- REGISTRAR VENTA ---"
				Escribir "Ingrese código del producto:"
				Leer codigo
				
				pos <- 0
				
				Para i <- 1 Hasta nProductos Hacer
					Si codigos[i] = codigo Entonces
						pos <- i
					FinSi
				FinPara
				
				Si pos = 0 Entonces
					Escribir "Producto no encontrado."
				Sino
					Escribir "Producto: ", nombres[pos]
					Escribir "Precio: S/ ", precios[pos]
					Escribir "Stock disponible: ", stocks[pos]
					
					Repetir
						Escribir "Ingrese cantidad vendida:"
						Leer cantidad
					Hasta Que cantidad > 0
					
					Si cantidad > stocks[pos] Entonces
						Escribir "Stock insuficiente."
					Sino
						total <- cantidad * precios[pos]
						stocks[pos] <- stocks[pos] - cantidad
						
						nVentas <- nVentas + 1
						ventaProducto[nVentas] <- nombres[pos]
						ventaCantidad[nVentas] <- cantidad
						ventaTotal[nVentas] <- total
						
						Escribir "Venta registrada correctamente."
						Escribir "Total a pagar: S/ ", total
					FinSi
				FinSi
				
			4:
				Escribir ""
				Escribir "--- REGISTRAR PEDIDO PARA EVENTO ---"
				
				Escribir "Ingrese nombre del cliente:"
				Leer cliente
				
				Escribir "Ingrese tipo de evento:"
				Leer tipoEvento
				
				Escribir "Ingrese fecha del evento:"
				Leer fechaEvento
				
				Escribir "Ingrese detalle del pedido:"
				Leer detalle
				
				Repetir
					Escribir "Ingrese anticipo recibido:"
					Leer anticipo
				Hasta Que anticipo >= 0
				
				nPedidos <- nPedidos + 1
				pedidoCliente[nPedidos] <- cliente
				pedidoEvento[nPedidos] <- tipoEvento
				pedidoAnticipo[nPedidos] <- anticipo
				
				Escribir "Pedido registrado correctamente."
				Escribir "Cliente: ", cliente
				Escribir "Evento: ", tipoEvento
				Escribir "Fecha del evento: ", fechaEvento
				Escribir "Detalle: ", detalle
				Escribir "Anticipo: S/ ", anticipo
				
			5:
				Escribir ""
				Escribir "--- BUSCAR PRODUCTO ---"
				Escribir "Ingrese código, nombre, categoría o evento exacto:"
				Leer textoBuscar
				
				encontrado <- Falso
				
				Para i <- 1 Hasta nProductos Hacer
					Si codigos[i] = textoBuscar O nombres[i] = textoBuscar O categorias[i] = textoBuscar O eventos[i] = textoBuscar Entonces
						Escribir "Producto encontrado:"
						Escribir codigos[i], " - ", nombres[i], " - ", categorias[i], " - ", eventos[i]
						Escribir "Precio: S/ ", precios[i], " | Stock: ", stocks[i]
						encontrado <- Verdadero
					FinSi
				FinPara
				
				Si encontrado = Falso Entonces
					Escribir "No se encontraron coincidencias."
				FinSi
				
			6:
				Escribir ""
				Escribir "--- REPORTE GENERAL ---"
				
				totalVentas <- 0
				
				Para i <- 1 Hasta nVentas Hacer
					totalVentas <- totalVentas + ventaTotal[i]
				FinPara
				
				Escribir "Cantidad de ventas registradas: ", nVentas
				Escribir "Cantidad de pedidos registrados: ", nPedidos
				Escribir "Monto total vendido: S/ ", totalVentas
				
				Escribir ""
				Escribir "Productos con stock bajo:"
				
				encontrado <- Falso
				
				Para i <- 1 Hasta nProductos Hacer
					Si stocks[i] <= 5 Entonces
						Escribir nombres[i], " - Stock: ", stocks[i]
						encontrado <- Verdadero
					FinSi
				FinPara
				
				Si encontrado = Falso Entonces
					Escribir "No hay productos con stock bajo."
				FinSi
				
			7:
				Escribir ""
				Escribir "--- CARGAR 50 VENTAS SIMULADAS ---"
				
				Para i <- 1 Hasta 50 Hacer
					pos <- Aleatorio(1, nProductos)
					cantidad <- Aleatorio(1, 2)
					
					Si cantidad <= stocks[pos] Entonces
						total <- cantidad * precios[pos]
						stocks[pos] <- stocks[pos] - cantidad
						
						nVentas <- nVentas + 1
						ventaProducto[nVentas] <- nombres[pos]
						ventaCantidad[nVentas] <- cantidad
						ventaTotal[nVentas] <- total
					FinSi
				FinPara
				
				Escribir "Ventas simuladas cargadas correctamente."
				
			8:
				Escribir ""
				Escribir "Guardando información del sistema..."
				Escribir "Fin del sistema Piñatería REY."
				
			De Otro Modo:
				Escribir "Opción inválida. Intente nuevamente."
				
		FinSegun
		
	Hasta Que opcion = 8

FinProceso
