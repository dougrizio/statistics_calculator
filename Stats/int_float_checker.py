
def check_for_number (a = "c", b = None, c = None):
    answer = 0

    if (int(a) or float(a)) and (int(b) or float(b)):
        pass


try:
    check_for_number(2, 12.0)
except:
    print("Values are bad!")
else:
    print("Values are good!")