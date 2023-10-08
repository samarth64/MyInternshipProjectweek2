def temp(val, unit_in, unit_out):
    SI = {"celsius": (val - 32) / 1.8, "fahrenheit": (val * 1.8) + 32}
    if unit_in == "celsius" or unit_in == "C":
        return SI["celsius"]
    else:
        return SI["fahrenheit"]


def Input():
    value = float(input("enter the value"))
    unit_in = input("enter the unit of value ")
    unit_in.lower()
    unit_out = input("enter the unit you want to convert ")
    unit_out.lower()
    S = ["celcius", "c", "fahrenheit", "f"]
    if (unit_in in S) and (unit_out in S):
        Ans = temp(value, unit_in, unit_out)
        print(value, unit_in, "is equivalent to:", Ans, unit_out)
    else:
        print("wrong units entered accepted units are", str(S))
Input()
