# Hex to decimal
hex = "38006F45291200"
bin = bin(int(hex, 16)).zfill(8)[2:]

# Read version
version = int(bin[:3], 2)
bin = bin[3:]
type = int(bin[:3], 2)
bin = bin[3:]


def get_literal_value(bin):
    literal_value = bin[:5]
    bin = bin[5:]
    number = ""
    while literal_value[0] == "1":
        number += literal_value[1:]
        literal_value = bin[:5]
        if literal_value[0] == "0":
            number += literal_value[1:]
        bin = bin[5:]
    bin = bin[3:]
    return int(number, 2)


def get_operator(bin):
    length_type = bin[0]
    bin = bin[1:]
    if length_type == "0":
        bit_number = 15
    else:
        bit_number = 11
    subpackets_lenght = int(bin[:bit_number], 2)
    bin = bin[bit_number:]
    print(subpackets_lenght)


print(get_operator(bin))
