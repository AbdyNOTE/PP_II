x = int(input())
list = (input() for i in range(x))

dict ={
    "Macbook": 5000,
    "PC": 6000,
    "Iphone": 2000,
    "Fridge": 1000,
    "TV": 3000,
    "Chair": 500
    }
s = 0
for i in list:
    if i in dict:
        s += dict[i]
print(s)