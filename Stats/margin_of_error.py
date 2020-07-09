from Calc.Calculator import Calculator


calc = Calculator()

def margin_of_error(crit_val, standard_error):

    result = calc.multiply(crit_val,standard_error)

    return result

