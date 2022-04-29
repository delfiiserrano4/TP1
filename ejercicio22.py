vector_mochila_del_jedi = ["sabledeluz", "tunicas", "creditos", "libros"]:

print ('Mochila del jedi', vector_mochila_del_jedi)
    
cantidad_de_objetos =len(vector_mochila_del_jedi)    
    
def usar_la_fuerza(mochila_del_jedi):
    if (len(mochila_del_jedi) ==0):
        return (False)
    elif (len(mochila_del_jedi[0] =="Sable de luz")):
        return (True)
    else:
        del mochila_del_jedi[0]
        return usar_la_fuerza(mochila_del_jedi)
    
    
if (usar_la_fuerza(vector_mochila_del_jedi):
    print("Se pudo encontrar el sable de luz")
    print("Para encontrar el sable de luz se sacaron previamente estos objetos", cantidad_de_objetos - len(vector_mochila_del_jedi))
else:
    print("No hay ningun sable de luz en la mochila")