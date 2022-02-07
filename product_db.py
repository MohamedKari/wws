from ssl import OP_NO_RENEGOTIATION
import sys

TODAY = 38

class Product():
  def __init__(self, name, tax_rate, net_price):
    self.name = name
    self.tax_rate = tax_rate
    self.net_price = net_price
  
  def compute_gross_price(self):
    gross_price = self.net_price * (1 + self.tax_rate)
    return gross_price
  
  def describe(self):
    print("Dieses Produkt heißt", self.name, ", kostet netto", self.net_price, "und hat einen MwSt-Satz von ", self.tax_rate, "% und der Brutto-Preis ist", self.compute_gross_price())

class FreshProduct(Product):
  def __init__(self, name, tax_rate, net_price, best_before_date):
    self.name = name
    self.tax_rate = tax_rate
    self.net_price = net_price
    self.best_before_date = best_before_date

  def days_to_expiration(self):
    return self.best_before_date - TODAY


class Assortment:
  def __init__(self, products):
    self.products = products

  def get_product(self, name):
    for product in self.products:
      if product.name == name:
          return product
    

assortmentEssen = Assortment([
  Product("Victory SuperShoes", 0.19, 15.50), 
  Product("Vicory MegaFlops", 0.07, 3.43),
  FreshProduct("KerryGold", 0.07, 0.92, 62)
])

product = assortmentEssen.get_product(sys.argv[1])
print("Server returns", product.compute_gross_price(), "as price")



