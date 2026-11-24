# Write your imports here
from .item import Bill, Product
from .entity import Buyer



class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1

# Clases que realiza el estudio de las factuars.
class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    # Buscamos en todas las facturas el producto más vendido.
    def find_top_sell_product(self) -> (Product, int):
        # Write here your code

        # Vamos almacenando el producto y el número de veces que parece.
        dic_productos = {}

        # Recorremos todas las facturas 
        for bill in self.bills:

            # Busca el producto dentro de la factura.
            for product in bill.products:

                # Vamos añadiendo a un diccionario el producto y acumulamos 
                # el número de veces que aparece
                if dic_productos.get(product.product_id) == None:
                    dic_productos[product.product_id] = [product, 1]
                else:
                    dic_productos[product.product_id] = [product, dic_productos.get(product.product_id)[1] + 1]

        #Buscamos el producto que tenga un mayor valor en el diccionario.
        prod = None
        amount = 0
        for key, val in dic_productos.items():
            if val[1] > amount:
                amount = val[1]
                prod = val[0]
                              
        # devolvermos el producto más vendido y el número de veces que aparece.
        return (prod, amount)

    # Calculamos el total de ventas por vendedor y devolveremos una lista con el nombre
    # de los dos con mayor ventas.
    def find_top_two_sellers(self) -> list:

        # Write here your code

        # Creamos un diccionario que contiene Vendedor e importe de ventas.
        dic_selers = {}

        # Vamos acumulando el total de ventas por vendedor.
        for bill in self.bills:

            if dic_selers.get(bill.seller) == None:
                dic_selers[bill.seller] = bill.calculate_total()
            else:
                dic_selers[bill.seller] += bill.calculate_total()

        # Ordenamos el diccionario por el valor de las ventas de vendedores.
        # Dict -> Sorted devuelve un listado así que lo que obtengamos queremos traducirlo a dicciónario.
        # Sorted -> Ordenamos. Obtenemos el par clave 
        #    key contiene cual va a ser la clave de ordenación le decimos que será el valor
        # reverse -> queremos que ordene de mayor a menor.valor le decimos que queremos 
        dic_selers = dict(sorted(dic_selers.items(), key= lambda x : x[1], reverse= True ))

        # Obtenemo un iterador para coger los dos primeros vendedores si los hay.
        iterador = iter(dic_selers.items())
        list_sellers = []
        cnt = 0
        while cnt < 2 and cnt < len(dic_selers):
            key = next(iterador)[0] # solo queremos el sellers.
            list_sellers.append(key)
            cnt +=1  

        # Devolvemos los dos primeros primeros vendedores si los hay.. 
        return list_sellers

    # Ordenamos el diccionario por el valor de ventas por compradores.
    # Devolvemos el de menor venta.
    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        # Write here your code
            # Write here your code

        # Creamos un diccionario que contiene compradores y total de compras.
        dic_selers = {}

        # Vamos acumulando el total de ventas por comprador.
        for bill in self.bills:

            if dic_selers.get(bill.buyer) == None:
                dic_selers[bill.buyer] = bill.calculate_total()
            else:
                dic_selers[bill.buyer] += bill.calculate_total()

        # Ordenamos el diccionario por el valor de las ventas de comprador.
        # Dict -> Sorted devuelve un listado así que lo que obtengamos queremos traducirlo a dicciónario.
        # Sorted -> Ordenamos. Obtenemos el par clave 
        #    key contiene cual va a ser la clave de ordenación le decimos que será el valor
        # reverse -> queremos que ordene de mayor a menor.valor le decimos que queremos 
        dic_selers = dict(sorted(dic_selers.items(), key= lambda x : x[1]))

        # Obtenemos el primer valor
        key, val = next(iter(dic_selers.items()))

        # Lo devolvemos en forma de tupla.
        return (key, val)

    # Devolvemos una lista ordenada de los productos por el total de los impuestos.
    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        # Write here your code
        # Generamos un diccionario don tendremos el par Producto, acumulato tasas
        dic_productos = {}

        # Debemos recorrer todos los productos de todas las factuas. 
        for bill in self.bills:

            # Por cada producto calculamos el total de las tasas 
            # y vamos generando un diccionario con él.
            for producto in bill.products:

                # Si el producto no existe lo introducimos en el diccionario junto con el total de impuestos.
                if dic_productos.get(producto.name) == None:
                        dic_productos[producto.name] = [producto, producto.calculate_total_taxes()]
                else: # Si existe vamos acumulan las tasas que se van pagando.
                        dic_productos[producto.name] = [producto, dic_productos.get(producto.name)[1] + producto.calculate_total_taxes()]


        # Ahora ordenamos el diccionario por el valor teniendo en 
        # cuenta si hemos indicado ascendente o descendente. 
        # X es una lista de listas de dos valors (objeto, taxas)
        dic_productos = dict(sorted( dic_productos.items(), key=lambda x: x[1][1], reverse=order_type))

        # Vamos añadiendo los valors en forma de tuplas (objeto, total_tasas)
        prod_tax = []
        for valor in dic_productos.values():
            prod_tax.append(tuple(valor))

        return prod_tax

        

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
