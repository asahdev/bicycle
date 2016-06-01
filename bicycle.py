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
  def __init__(self,model_name,count):
    self.model_name = model_name
    self.count = count

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
    model_a_in = shop("Model A",int(5))
    model_b_in = shop("Model B",int(7))
    model_c_in = shop("Model C",int(9))
    model_d_in = shop("Model D",int(7))
    model_e_in = shop("Model E",int(3))
    model_f_in = shop("Model F",int(2))
    
    list_bikes = { model_a.cop:model_a.model_name,model_b.cop:model_b.model_name,model_c.cop:model_c.model_name,model_d.cop:model_d.model_name,model_e.cop:model_e.model_name,model_f.cop:model_f.model_name }

    print("%s can afford " %(customer_a.cus_name))    
    for key in list_bikes:
      if customer_a.buget >= key:
        print(list_bikes[key])

    print("%s can afford " %(customer_b.cus_name)) 
    for key in list_bikes:
      if customer_b.buget >= key:
        print(list_bikes[key])

    print("%s can afford " %(customer_c.cus_name))
    for key in list_bikes:
      if customer_c.buget >= key:
        print(list_bikes[key])
    list_bikes = [model_a.cop,model_b.cop,model_c.cop,model_d.cop,model_e.cop,model_f.cop]

<<<<<<< HEAD
    print("Printing inventorty of the shop")
    print("%s : %s " %(model_a_in.model_name,model_a_in.count)) 
    print("%s : %s " %(model_b_in.model_name,model_b_in.count))
    print("%s : %s " %(model_c_in.model_name,model_c_in.count))
    print("%s : %s " %(model_d_in.model_name,model_d_in.count))
    print("%s : %s " %(model_e_in.model_name,model_f_in.count))
    print("%s : %s " %(model_f_in.model_name,model_f_in.count))

if __name__ == "__main__":
  main()
=======
#if __name__ == "__main__":
main()
>>>>>>> 2c2f1951f12044733d189b0e3a5e63e851fbf96e
