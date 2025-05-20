
instructionTypes = {
    "NOP" : 0b000,
    "move": 0b001,
    "OP"  : 0b010,
    "Stck": 0b011,
    "Dsp" : 0b100,
    "pnt" : 0b101,
    "END" : 0b111
}

operands = {
    "NOP" : 0b000000,

    "0x01": 0b000001,
    "0x02": 0b000010,
    "0x03": 0b000011,
    "0x04": 0b000100,
    "0x05": 0b000101,
    "0x06": 0b000110,
    "0x07": 0b000111,
    "0x08": 0b001000,
    "0x09": 0b001001,
    "0x0A": 0b001010,
    "0x0B": 0b001011,
    "0x0C": 0b001100,
    "0x0D": 0b001101,
    "0x0E": 0b001110,
    "0x0F": 0b001111,
    "0x11": 0b010000,
    "0x12": 0b010001,
    "0x13": 0b010010,
    "0x14": 0b010011,
    "0x15": 0b010100,
    "0x16": 0b010101,
    "0x17": 0b010110,
    "0x18": 0b010111,
    "0x19": 0b011000,
    "0x1A": 0b011001,
    "0x1B": 0b011010,
    "0x1C": 0b011011,
    "0x1D": 0b011100,
    "0x1E": 0b011101,
    "0x1F": 0b011110,
    "0x21": 0b011111,
    "0x22": 0b100000,

    "ABX" : 0b100001,
    "AX"  : 0b100010,
    "DAX" : 0b100011,
    "DBX" : 0b100100,
    "DCX" : 0b100101,
    "IAX" : 0b100110,
    "IBX" : 0b100111,
    "OAX" : 0b101000,
    "OBX" : 0b101001,
    "OCX" : 0b101010,
    "PAX" : 0b101011,

    "NOP"  : 0b101100,
    "ADD"  : 0b101101,
    "SUB"  : 0b101110,
    "SUBR" : 0b110110,
    "LEFT" : 0b101111,
    "RGHT" : 0b110000,
    "NOT"  : 0b110001,
    "XOR"  : 0b110010,
    "XNOR" : 0b110011,
    "AND"  : 0b110100,
    "MULT" : 0b110101,
    "EQ"   : 0b110111,
    "LESS" : 0b111000,
    "GRTR" : 0b111001,
    "LSEQ" : 0b111010,
    "GREQ" : 0b111011,
    "NEQ"  : 0b111100,
    "NAND" : 0b111101,
    
    "OX"   : 0b111110,
    "IX"   : 0b111111,
}

stackOps = {
    "NOP" : 0b000000,

    "0x01": 0b000001,
    "0x02": 0b000010,
    "0x03": 0b000011,
    "0x04": 0b000100,
    "0x05": 0b000101,
    "0x06": 0b000110,
    "0x07": 0b000111,
    "0x08": 0b001000,
    "0x09": 0b001001,
    "0x0A": 0b001010,
    "0x0B": 0b001011,
    "0x0C": 0b001100,
    "0x0D": 0b001101,
    "0x0E": 0b001110,
    "0x0F": 0b001111,
    "0x11": 0b010000,
    "0x12": 0b010001,
    "0x13": 0b010010,
    "0x14": 0b010011,
    "0x15": 0b010100,
    "0x16": 0b010101,
    "0x17": 0b010110,
    "0x18": 0b010111,
    "0x19": 0b011000,
    "0x1A": 0b011001,
    "0x1B": 0b011010,
    "0x1C": 0b011011,
    "0x1D": 0b011100,
    "0x1E": 0b011101,
    "0x1F": 0b011110,
    "0x21": 0b011111,
    "0x22": 0b100000,

    "AX"  : 0b100010,
    "DAX" : 0b100011,
    "DBX" : 0b100100,
    "DCX" : 0b100101,
    "IAX" : 0b100110,
    "IBX" : 0b100111,
    "OAX" : 0b101000,
    "OBX" : 0b101001,
    "OCX" : 0b101010,
    "PAX" : 0b101011,

    "psh" : 0b101101,
    "pop" : 0b101110,
    "flsh": 0b101111,
    "size": 0b110000,
    "last": 0b110001,
}

pointerOps = {
    "NOP" : 0b000000,

    "0x01": 0b000001,
    "0x02": 0b000010,
    "0x03": 0b000011,
    "0x04": 0b000100,
    "0x05": 0b000101,
    "0x06": 0b000110,
    "0x07": 0b000111,
    "0x08": 0b001000,
    "0x09": 0b001001,
    "0x0A": 0b001010,
    "0x0B": 0b001011,
    "0x0C": 0b001100,
    "0x0D": 0b001101,
    "0x0E": 0b001110,
    "0x0F": 0b001111,
    "0x11": 0b010000,
    "0x12": 0b010001,
    "0x13": 0b010010,
    "0x14": 0b010011,
    "0x15": 0b010100,
    "0x16": 0b010101,
    "0x17": 0b010110,
    "0x18": 0b010111,
    "0x19": 0b011000,
    "0x1A": 0b011001,
    "0x1B": 0b011010,
    "0x1C": 0b011011,
    "0x1D": 0b011100,
    "0x1E": 0b011101,
    "0x1F": 0b011110,
    "0x21": 0b011111,
    "0x22": 0b100000,

    "AX"  : 0b100010,
    "DAX" : 0b100011,
    "DBX" : 0b100100,
    "DCX" : 0b100101,
    "IAX" : 0b100110,
    "IBX" : 0b100111,
    "OAX" : 0b101000,
    "OBX" : 0b101001,
    "OCX" : 0b101010,
    "PAX" : 0b101011,

    "WRT" : 0b101101,
    "MOVE": 0b101110,
}

codeFile = input("File >> ")
code = open(codeFile).read()
code = code.replace(' ', '')
code = code.split('\n')

binary = []
for badLine in code:
    instruction = ""

    line = ""
    for char in badLine:
        if char == '#':
            break
        line += char

    ops = line.split(",")
    #print(ops, "|", line, "|", code)
    try:
        instType = instructionTypes[ops[0]]
        #print(instType)
        instruction += '{0:03b}'.format(instType)  # str(bin(instType)[2:])
        instruction += "_"
        #print(instType)

        for op in ops[1:]:
            if instType == 0b011 and op in stackOps:
                decoded = stackOps[op]
                instruction += '{0:06b}'.format(decoded)
                instruction += "_"
            elif instType == 0b101 and op in pointerOps:
                decoded = pointerOps[op]
                instruction += '{0:06b}'.format(decoded)
                instruction += "_"
            else:
                if op not in operands:
                    instruction += '{0:08b}'.format(int(op))  # str(bin(int(op))[2:])  # it should be a number
                    instruction += "_"
                else:
                    decoded = operands[op]
                    instruction += '{0:06b}'.format(decoded)  # str(bin(decoded)[2:])
                    instruction += "_"

        binary.append(instruction[:-1])
    except KeyError:
        pass  # incase the instruction is null or something

print(binary)
with open(input("output >> "), "w") as file:
    text = ""
    for line in binary:
        text += line
        text += '\n'
    file.write(text[:-1])
