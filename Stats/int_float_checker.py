
def check_for_number (a = "c", b = None, c = None):
    answer = 0

    if int(a) or float(a):
        pass

try:
    check_for_number(7, "q")
except:
    print("Oh no!")
else:
    print("It's good")