
#q2-write a python function that takes 3 and returns True if they atleast have on common member.

colors = ['blue', 'green', 'orange', 'brown', 'red']
fruits = ['apple', 'orange' ,'mango' ,'banana' ,'cherry']
names = ['lawrance', 'amaka', 'kingston' ,'thomas' ,'orange']
cars = ['benz' ,'orange' ,'lexus' ,'venza', 'hilux' ]
electronics = ["panasonic" ,"samsung" ,"hisense" ,"orange"]
wristwatches = ["rolex" ,"tissot" ,"apple" ,"orange" ,"hublot"]
phones = ["orange" ,"apple","nokia" ,"techno" ,"itel", "umidigi"]
wine = ["egovin" ,"orange", "azul" ,"meot" ,"red label" ]
shoes = ["addidas" ,"nike" ,"puma", "orange" ,"kappa" ]
music = ["amapiano" ,"jazz" ,"blues" ,"RnB" ,"hip hop" ,"orange"]

common_elements = set(colors).intersection(fruits, names, cars,electronics,wristwatches,phones,wine,shoes,music)
def myfun():
 if common_elements:
      print('True:' ,common_elements)
 else:
     print('False', common_elements)

myfun()
