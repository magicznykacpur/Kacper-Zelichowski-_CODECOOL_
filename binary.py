input_list = input()
number, conversion = input_list.split(" ")

while conversion not in ["2", "10"] or number.isalpha() or number == " ":
    print("Wrong input. Try entering a number, and conversion system (2/10).")
    input_list = input()
    number, conversion = input_list.split(" ")
else:
    number = int(number)
    conversion = int(conversion)



def bintodec(number):
    res = []
    decimal = number

    while decimal > 0:
        result = decimal % 2
        decimal = int(decimal / 2)
        res.insert(0, result)
    print("".join(str(x) for x in res))

def dectobin(number):
    binary = str(number)
    binary = list(binary)
    binary = [int(x) for x in binary]

    decim = 0
    y = len(binary) - 1

    for x in binary:
        dec = x * 2**y
        decim = decim + dec
        y = y - 1
    print(decim)


if conversion == 2:
    dectobin(number)
elif conversion == 10:
    bintodec(number)
