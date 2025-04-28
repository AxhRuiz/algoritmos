def usar_la_fuerza(mochila, objetos_sacados=0):

    if len(mochila) > 0:

        if mochila[0] == "sable de luz":
            return True, objetos_sacados + 1
        else:

            return usar_la_fuerza(mochila[1:], objetos_sacados + 1)
    else:

        return False, objetos_sacados
