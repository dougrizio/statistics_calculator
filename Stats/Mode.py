from collections import Counter

def mode(data):
    numValues = len(data)

    numCount = Counter(data)
    calc_mode = dict(numCount)
    modeResult = [k for k, v in calc_mode.items() if v == max(list(numCount.values()))]

    if len(modeResult) == numValues:
        return
    else:
        return modeResult

    # lst = [3, 4, 5, 5, 6, 6, 7, 7, 7, 5, 5]
    # print(max(lst, key=lst.count))