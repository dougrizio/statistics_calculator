from Calc.Calculator import Calculator

crit_val = 1.645
standard_error = .013
calc = Calculator()

def margin_of_error(crit_value, standard_error):

    result = calc.multiply(crit_val,standard_error)

    return result

me = margin_of_error(crit_val, standard_error)

print("Critical Value: " + str(crit_val))
print("Standard Error: " + str(standard_error))
print("Margin of Error: " + str(me))
