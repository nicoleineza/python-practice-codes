#
level 1: The program will display Babatunde
#level 2: The program will display Babatunde
#level 3: The program will display Babatunde and None
#level 4: The program will display Babatunde and 35
#level 5: the program will display Babatunde and 35
#level 6: the program will display Babatunde,none,35 and none
#level 7: nothing will be displayed
#level 8: nothing will be displayed
#level 9: Program will display Babatunde
#level 10: nothing will be displayed
#level 11: nothing will be displayed
#level 12: Program will display 37
#level 13: program will display Darren and 37
#level 14: program will display none and 37
#section b

#level 1
def show_name():
    print("hello", name)

show_name(name)
#level 2
def area_of_room(length, width):
    area=length*width

    print(area)
#level 3
def area_of_room(length, width):
    area=length*width
    area_in_acres=area/43560
    print(area_in_acres, "acres")
#level 4
def summation(number):
    summation=0
    for i in range(1,number+1)
    print (summation)
#level 5
def day_old_bread(number):
    price=(10-(10*0.55))*number
    print(price)
#level 6
def temperature_in_celcius(number):
    fahrenheit= (number*(9/5))+35
    kelvin=number+273.15
    print(kelvin,"degrees kelvin")
    print(fahrenheit,"degrees fahrenheit")
#level 7
def area_of_triangle(base,height):
    area=((base*height)/2)
    print(area)
#level 8
def amaount_of_gas(p,v,t):
    n=(p*v)/(8.314*t)
    print(n,"moles")
#level 9
def volume_of_cylinder(r,h):
    v=2*3.14*r*r*h
    volume=(round(v,1))
    print(volume)
