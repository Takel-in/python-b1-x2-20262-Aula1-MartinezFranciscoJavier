from enum import Enum
import datetime
from .entity import *

# Do not change the value of ISD_FACTOR var
ISD_FACTOR = 0.25


class TaxType(Enum):
    # Do not change this enum
    IVA = 1
    ISD = 2

# Clase que representa los impuestos
class Tax:
    # Write the parameters in the next line
    def __init__(self, tax_id :str, tax_type: TaxType, percentage :float):
        # Write here your code
        self.tax_id = tax_id, 
        self.tax_type = tax_type
        self.percentage = percentage


# Clase que representa los productos
class Product:
     # Write the parameters in the next line
    def __init__(self, prduct_id :str, name :str, expiration_date :datetime, bar_code :str, quantity :int, price :float, taxes :list[Tax]):
        self.product_id = prduct_id
        self.name = name
        self.expiration_date = expiration_date
        self.bar_code = bar_code
        self.quantity = quantity
        self.price = price
        self.taxes = taxes
        # Write here your code
        pass        

    # Calcula el impuesto.
    def calculate_tax(self, tax: Tax) -> float:
        # Write here your code

        if tax == None:
            return 0.0

        # Primero calculamo el coste
        cal_tot = self.quantity * self.price 

        # Calculo el impuesto dependiendo del tipo.
        if tax.tax_type == TaxType.IVA:
            return float(cal_tot *  tax.percentage)
        
        if tax.tax_type == TaxType.ISD:
            return float(cal_tot * tax.percentage * ISD_FACTOR)

        # Si no se ha indicado un tipo de impuesto válido damos error.
        raise TypeError (f"No se ha indicado un tipo de impuesto correo {tax}")



        pass

    # Cogemos el listado de impuestos del producto y calculamos su acumulado.
    def calculate_total_taxes(self ) -> float:
        # Write here your code

        # Recorrer los impuestos que tiene este producto.
        tot_tax = 0.0
        for tax in self.taxes:
            
            # vamos acumulando el calculo de impuesto en esa línea.
            tot_tax += self.calculate_tax(tax)

        return tot_tax
        
    # Calculamos el coste total del producto.
    def calculate_total(self) -> float:
        
        # Write here your code
        return float((self.quantity * self.price) + self.calculate_total_taxes())

        pass

    def __eq__(self, another):
        # Do not change this method
        return hasattr(another, 'product_id') and self.product_id == another.product_id

    def __hash__(self):
        # Do not change this method
        return hash(self.product_id)

    def print(self):
        # Do not change this method
        print(
            f"Product Id:{self.product_id} , name:{self.name}, quantity:{self.quantity}, price:{self.price}")
        for tax in self.taxes:
            print(f"Tax:{tax.tax_type} , percentage:{tax.percentage}")

# Clase que representa las facturas.
class Bill:
    def __init__(self, bill_id: str, sale_date: datetime, seller: Seller, buyer: Buyer, products: list[Product]):
        # Write here your code
        self.bill_id = bill_id
        self.sale_date = sale_date
        self.seller = seller  # Vendedor
        self.buyer = buyer  # Comprador
        self.products = products
       
    # Devuelve el total de la factura.
    def calculate_total(self) -> float:
        # Write here your code

        # Se recorre la lista de productos y va sumando el gasto.
        tot_bill = 0.0
        for product in self.products:
            tot_bill += product.calculate_total()

        return tot_bill


    def print(self):
        # Do not change this method
        self.buyer.print()
        self.seller.print()
        for product in self.products:
            product.print()