
def check_for_number_parameters (a = 0, b = 0, c = 0):

    result = a
    bresult = b


    try:
        if (int(a) or float(a)) + (int(b) or float(b)) + (int(c) or float(c)) :
            pass


    except:
        print("Values must be integers or floats!")


    return result, bresult

