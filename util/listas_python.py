def lista_nativa (lista):                               # Esta es una función creada para pasar a datos nativos de python elementos antes de crear un objeto.
    lista_limpia = []
    for elemento in lista:
        if "int" in type(elemento).__name__:
            lista_limpia.append(int(elemento))
        elif "float" in type(elemento).__name__:
            lista_limpia.append(float(elemento))
        else:
            lista_limpia.append(elemento)
    return lista_limpia
    

