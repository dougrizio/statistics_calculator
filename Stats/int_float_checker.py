
def check_for_number_parameters (a = "c", b = None, c = None, d = None):
    answer = 0

    if (int(a) or float(a)) and (int(b) or float(b)) and (int(c) or float(c)):
        pass

'''
try:
    check_for_number_parameters(7, 7)
except:
    print("Values are bad!")
else:
    print("Values are good!")
'''