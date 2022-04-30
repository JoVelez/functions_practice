def hello():
  print("Wazzup.")

hello()

def pack(red,green,blue):
  return [red,green,blue]

print(pack("red","green","blue"))

#study solution code for here v

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

eat_lunch([])
eat_lunch(["Hamburger"])
eat_lunch(["cheese","sandwich","oranges","cookie"])