# Creating PR (merge conflict) in second-homework-conflict
# Simple version of Units_converter

how_much = 0  # is necessary for temperature_K
mass_kg = {"kg": 1, "g": 10 ** 3, "mg": 10 ** 6, "microg": 10 ** 9,
           "t": 10 ** (-3), "lb": 2.20462,
           "help": "kg - kilogramme\ng - gram\nmg - milligramme\n"
                   "microg - microgramme\nt - ton\nlb - pound\n"}

time_sec = {"s": 1, "c": 3.171 * (10 ** (-10)), "yr": 3.171 * (10 ** (-8)),
            "wk": 1.6534 * (10 ** (-6)), "d": 1.1574 * (10 ** (-5)),
            "h": 0.000277778, "min": 0.0166667,
            "help": "s - second\nc - century\nyr - year\nwk - week\n"
                    "d - day\nh - hour\nmin - minute\n"}

pressure_Pa = {"Pa": 1, "bar": 10 ** (-5), "atm": 9.8692 * (10 ** (-6)),
               "help": "Pa - Pascal\nbar - bar\natm - atmosphere\n"}

temperature_K = {"K": how_much, "C": how_much + 273.15, "F": (how_much - 32) * 5/9 + 273.15,
                 "help": "K - Kelvin\nC - Celsius\nF - fahrenheit\n"}


converter = {"mass": mass_kg, "time": time_sec, "pressure": pressure_Pa, "temperature": temperature_K}

while True:
    print("What type of operation do you want?\nmass, time, pressure or temperature?")
    while True:
        conversion = input()
        if conversion not in converter.keys():
            print("There is no such type of conversion :(")
            print("Please, type 'mass', 'time', 'pressure' or 'temperature'")
            continue
        else:
            break

    print("There are possible quantities")
    keys = [i for i in converter[conversion].keys() if i != "help"]
    print(keys)
    print(converter[conversion]["help"])

    while True:
        From = input("What we are converting from\t(Example: {})\n".format(keys[1]))
        how_much = float(input("Enter the quantity\t(Example: 1)\n"))
        To = input("What we are converting in\t(Example: {})\n".format(keys[2]))

        if From not in converter[conversion] or To not in converter[conversion]:
            print("There is no such quantity :(")
            print("Please, type '{}'\n".format("' or '".join(keys)))
            continue
        else:
            break

    if conversion == "temperature":
        if To == "C":
            temp = temperature_K[From] - 273.15
        elif To == "F":
            temp = (temperature_K[From] - 273.15) * 9 / 5 + 32
        elif To == "K":
            temp = temperature_K[From]
        print(From, "=", temp, To)
    else:
        print(From, "=", how_much * converter[conversion][To] / converter[conversion][From], To)

    if input("To start again type y\n") == "y":
        continue
    else:
        break
