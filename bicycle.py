class bicycle(object):
#class containing model name of bicycle,weight and cost to produce
  def __init__(self,model_name,weight,cop):
    self.model_name = model_name
    self.weight = weight
    self.cop = int(cop + cop * .20)
   
  def print_list(self):
    print(self.model_name,end=" ")
    print(self.weight,end=" ")
    print(self.cop)
    

#class bike_shops(self,shop_name,inventory,sel_price)
class shop(object):
  def __init__(self,count_a,count_b,count_c,count_d,count_e,count_f):
    self.count_a = count_a
    self.count_b = count_b
    self.count_c = count_c
    self.count_d = count_d
    self.count_e = count_e
    self.count_f = count_f
  
#class customers(self,cus_name,buget)
class customers(object):
  def __init__(self,cus_name,buget):
    self.cus_name = cus_name
    self.buget = buget

   
def main():
    model_a = bicycle("Model A","10 KG",int(120))
    model_b = bicycle("Model B","8 KG",int(220))
    model_c = bicycle("Model C","7 KG",int(500))
    model_d = bicycle("Model D","7 KG",int(550))
    model_e = bicycle("Model E","6 KG",int(600))
    model_f = bicycle("Model F","4 KG",int(800))
    customer_a = customers("Anshul",int(200))
    customer_b = customers("Ram",int(500))
    customer_c = customers("Sham",int(1000))
    bike_shop = shop(int(5),int(6),int(10),int(3),int(9),int(6)) 

    list_bikes = { model_a.cop:model_a.model_name,model_b.cop:model_b.model_name,model_c.cop:model_c.model_name,model_d.cop:model_d.model_name,model_e.cop:model_e.model_name,model_f.cop:model_f.model_name}    

    d_inven = { model_a.model_name:bike_shop.count_a,model_b.model_name:bike_shop.count_b,model_c.model_name:bike_shop.count_c,model_d.model_name:bike_shop.count_d,model_d.model_name:bike_shop.count_d,model_e.model_name:bike_shop.count_e,model_f.model_name:bike_shop.count_f }

    list_a = []
    list_b = []
    list_c = []
    choice_b = []
    list_inv = [ bike_shop.count_a,bike_shop.count_b,bike_shop.count_c,bike_shop.count_d,bike_shop.count_e,bike_shop.count_f ]
#Checking what bikes Customer can afford
    print("%s can afford " %(customer_a.cus_name))    
    for key,value in list_bikes.items():
      if customer_a.buget >= key:
         list_a.append(value)
         print(list_bikes[key])

#Checking what bikes Customer can afford
    print("%s can afford " %(customer_b.cus_name))
    for key,value in list_bikes.items():
      if customer_b.buget >= key:
        list_b.append(value)
        print(list_bikes[key])

#Checking what bikes Customer can afford
    print("%s can afford " %(customer_c.cus_name))
    for key,value in list_bikes.items():	
      if customer_c.buget >= key:
        list_c.append(value)
        print(list_bikes[key])

#Printing Inventory of shop
    print("Printing inventorty of the shop")
    print("%s : Inventory: %s   Product code:001 " %(model_a.model_name,bike_shop.count_a)) 
    print("%s : Inventory: %s   Product code:002" %(model_b.model_name,bike_shop.count_b))
    print("%s : Inventory: %s   Product code:003" %(model_c.model_name,bike_shop.count_c))
    print("%s : Inventory: %s   Product code:004" %(model_d.model_name,bike_shop.count_d))
    print("%s : Inventory: %s   Product code:005" %(model_e.model_name,bike_shop.count_e))
    print("%s : Inventory: %s   Product code:006" %(model_f.model_name,bike_shop.count_f))
    print("\n")
#Customers buying bikes
    print("Welcome Anshul , please enter the bike name to buy bike" )
    choice = input()
    if choice in list_a:
      for key, value in list_bikes.items(): 
        if value == choice:
          print("You have choosen bike %s " %(value))
          print("The cost of the bike is %s " %(key))
          print("The buget left with customer is %s" %(customer_a.buget - key))
          d_inven[value] = d_inven[value] - 1
          print(d_inven[value])
          choice_b.append(value)          
          
    else:
      print("No Bike name found or cant afford bike")
  
    print("Welcome Ram , please enter the bike name to buy bike" )
    choice = input()
    if choice in list_b:
      for key, value in list_bikes.items():
        if value == choice:
          print("You have choosen bike %s " %(value))
          print("The cost of the bike is %s " %(key))
          print("The buget left with customer is %s" %(customer_b.buget - key))
          choice_b.append(value)
          d_inven[value] = d_inven[value] - 1
    else:
      print("No Bike name found or cant afford bike")

    print("Welcome Sham , please enter the bike name to buy bike" )
    choice = input()
    if choice in list_c:
      for key, value in list_bikes.items():
        if value == choice and value in list_c:
          print("You have choosen bike %s " %(value))
          print("The cost of the bike is %s " %(key))
          print("The buget left with customer is %s" %(customer_c.buget - key))
          choice_b.append(value)
          d_inven[value] = d_inven[value] - 1
    else:
      print("No Bike name found or cant afford bike")

#Printing Inventory of shop
    print("Printing Inventory of the shop")
    print("%s : Inventory: %s   Product code:001 " %(model_a.model_name,d_inven[model_a.model_name]))
    print("%s : Inventory: %s   Product code:002" %(model_b.model_name,d_inven[model_b.model_name]))
    print("%s : Inventory: %s   Product code:003" %(model_c.model_name,d_inven[model_c.model_name]))
    print("%s : Inventory: %s   Product code:004" %(model_d.model_name,d_inven[model_d.model_name]))
    print("%s : Inventory: %s   Product code:005" %(model_e.model_name,d_inven[model_e.model_name]))
    print("%s : Inventory: %s   Product code:006" %(model_f.model_name,d_inven[model_f.model_name]))
if __name__ == "__main__":

   
  main()
