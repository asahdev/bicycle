class bicycle(object):
#class containing model name of bicycle,weight and cost to produce
  def __init__(self,model_name,weight,cop):
    self.model_name = model_name
    self.weight = weight
    self.cop = cop

  def print_list(self):
    print(self.model_name,end=" ")
    print(self.weight,end=" ")
    print(self.cop)
    

#class bike_shops(self,shop_name,inventory,sel_price)


#class customers(self,cus_name,buget)

def main():
    model_a = bicycle("Model A","10 KG",int(120))
    model_b = bicycle("Model B","8 KG",int(220))
    model_c = bicycle("Model C","7 KG",int(500))
    model_d = bicycle("Model D","7 KG",int(550))
    model_e = bicycle("Model E","6 KG",int(600))
    model_f = bicycle("Model F","4 KG",int(1000))
    
    model_a.print_list()
    model_b.print_list()
    model_c.print_list()
    model_d.print_list()
    model_e.print_list()
    model_f.print_list()

#if __name__ == "__main__":
main()
