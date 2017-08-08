"""Module to check an Array to Station GAS."""


def validate_starr(p_stt_arr):
    """Method to check array the of GAS.

    Receive an array with amount of gas in gallons and
    amount GAS needed to the get following next GAS station.

    Param: Array
    return: Index
    """
    station = 0
    totg = 0
    length_gas = len(p_stt_arr)
    for index in p_stt_arr:
        if ':' in index:
            station += 1
            g, c = index.split(':')
            totg += int(g) - int(c)
            if totg < 0:
                raise Exception('Impossible')
        if ((station + 1) == length_gas) and (int(c) > 0):
            station = 1
    return station


def GasStation(strArr):
    """Method Default of the Problems."""
    length_gas = len(strArr)
    if length_gas >= 2:
        return str(validate_starr(strArr[1:]))

    raise Exception("Invalid Array")



print (GasStation(a))