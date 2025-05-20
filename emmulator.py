#binary: list[str] = ['001_101100_100011_00000001', '001_101100_000001_00000000', '001_000001_100100', '010_101101_100011_100100_101000', '010_101100_100011_100011_101001', '001_101001_000001', '001_101000_100011', '001_101100_100101_11101001', '010_111011_100011_100101_101010', '001_101010_100101', '010_101101_101011_100101_101010', '001_101010_101011', '001_101100_101011_00000001', '111']
#['001_101100_100011_00100010', '010_101100_100011_100011_101000', '011_101101_101000', '011_110000_100011', '001_101100_100100_00000011', '010_101101_100011_100100_101000', '000']
#['001_101100_100011_00000101', '001_101100_000001_00001000', '001_101100_100110_00000001', '001_100110_100100', '010_110100_100011_100100_101000', '001_101000_100011', '001_101100_100100_00000001', '010_101101_100011_100100_101000', '001_101000_100011', '001_101100_100100_00000001', '010_110111_100011_100100_101000', '001_101000_100011', '010_101101_100011_101011_101000', '001_101000_101011', '001_101100_101011_00001111', '001_101100_001010_00011011', '000']
#['001_101100_100011_00000101', '001_101100_000001_00001000', '001_101100_100110_00000001', '001_100110_100100', '010_110100_100011_100100_101000', '001_101000_100011', '001_101100_100100_00000001', '010_101101_100011_100100_101000', '001_101000_100011', '001_101100_100100_00000011', '010_110111_100011_100100_101000', '001_101000_100011', '010_101101_100011_101011_101000', '001_101000_101011', '001_101100_101011_00001111', '001_101100_001010_00011011', '000']
#['001_101100_100011_00000101', '001_101100_000001_00001000', '001_101100_100110_00000001', '001_100110_100100', '010_110100_100011_100100_101000', '001_101000_100011', '001_101100_100100_00000001', '010_101101_100011_100100_101000']
#['001_101100_100011_00000101', '001_101100_000001_00001000', '001_101100_100110_00000001', '001_100110_100100', '010_110100_100011_100100_101000']
#['001_101100_100101_00000101', '001_101100_000001_00001000', '001_101100_100110_00000001', '001_100110_100100', '010_101100_100101_100100_101000']
#['001_101100_100101_00000101', '001_101100_000001_00001000', '001_101100_100110_00000001', '001_100110_100100', '010_101101_100101_100100_101000']
#['001_101100_100011_00000101', '001_101100_000001_00001000', '001_101100_100110_00000001', '001_100110_100100', '010_101101_100011_100100_101000']
#['001_101100_100011_00000101', '001_101100_000001_00000001', '001_000001_100100', '010_101101_100011_100100_101000']

with open(input("file >> ")) as file:
    binary = file.read().split("\n")

registers = {
    "100001": 0,
    "100010": 0,
    "100011": 0,
    "100100": 0,
    "100101": 0,
    "100110": 0,
    "100111": 0,
    "101000": 0,
    "101001": 0,
    "101010": 0,
    "101011": 0,
    "111110": 0,  # OX/IX
    "111111": 0,
}

regNames = {
    "100001": "ABX",
    "100010": "AX",
    "100011": "DAX",
    "100100": "DBX",
    "100101": "DCX",
    "100110": "IAX",
    "100111": "IBX",
    "101000": "OAX",
    "101001": "OBX",
    "101010": "OCX",
    "101011": "PAX",
    "111110": "OX",
    "111111": "IX"
}

ram = {
    "000001": 0,
    "000010": 0,
    "000011": 0,
    "000100": 0,
    "000101": 0,
    "000110": 0,
    "000111": 0,
    "001000": 0,
    "001001": 0,
    "001010": 0,
    "001011": 0,
    "001100": 0,
    "001101": 0,
    "001110": 0,
    "001111": 0,
    "010000": 0,
    "010001": 0,
    "010010": 0,
    "010011": 0,
    "010100": 0,
    "010101": 0,
    "010110": 0,
    "010111": 0,
    "011000": 0,
    "011001": 0,
    "011010": 0,
    "011011": 0,
    "011100": 0,
    "011101": 0,
    "011110": 0,
    "011111": 0,
    "100000": 0,
}

opCodes = {
    "101100": lambda bus1, bus2: bus1 | bus2,  # "NOP"  :
    "101101": lambda bus1, bus2: bus1 + bus2,  # "ADD"  :
    "101110": lambda bus1, bus2: bus1 - bus2,  # "SUB"  :
    "110110": lambda bus1, bus2: bus2 - bus1,  # "SUBR"  :
    "101111": lambda bus1, bus2: bus1 << bus2,  # "LEFT" :
    "110000": lambda bus1, bus2: bus1 >> bus2,  # "RIGHT":
    "110001": lambda bus1, bus2: ~bus1,  # "NOT"  :
    "110010": lambda bus1, bus2: bus1 ^ bus2,  # "XOR"  :
    "110011": lambda bus1, bus2: ~(bus1 ^ bus2),  # "XNOR" :
    "110100": lambda bus1, bus2: bus1 & bus2,  # "AND"  :
    "110101": lambda bus1, bus2: bus1 * bus2,  # "MULT" :
    "110111": lambda bus1, bus2: int(bus1==bus2) + 1,  # "EQ"   :
    "111000": lambda bus1, bus2: int(bus1<bus2) + 1,  # "LESS" :
    "111001": lambda bus1, bus2: int(bus1>bus2) + 1,  # "GRTR" :
    "111010": lambda bus1, bus2: int(bus1<=bus2) + 1,  # "LSEQ" :
    "111011": lambda bus1, bus2: int(bus1>=bus2) + 1,  # "GREQ" :
    "111100": lambda bus1, bus2: int(bus1!=bus2) + 1,  # "NEQ"  :
    "111101": lambda bus1, bus2: ~(bus1 & bus2),  # "NAND" :
}

# 16 values
stackCounter = 0
stack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

stackCodes = {
    "101100": lambda    : (),
    "101101": lambda add: Push(GetAdd(add)),
    "101110": lambda add: SetAdd(add, Pop()),
    "101111": lambda    : ClearStack(),
    "110000": lambda add: SetAdd(add, stackCounter),
    "110001": lambda add: SetAdd(add, stack[stackCounter-1]),
}

pointerCodes = {
    "101101": lambda add, add2: SetAdd('{0:06b}'.format(GetAdd(add)), GetAdd(add2)),
    "101110": lambda add, add2: Move(add, add2),
}

def Move (add, add2):
    #print(f"{add}, {add2}, moving; {GetAdd(add)}")
    return SetAdd(add2, GetAdd(add))

def Pop () -> int:
    global stack, stackCounter
    stackCounter -= 1
    return stack[stackCounter]

def ClearStack ():
    global stackCounter
    stackCounter = 0

def Push (value) -> None:
    global stack, stackCounter
    stack[stackCounter] = value
    stackCounter += 1

def GetAdd (add) -> int:
    if add in registers:
        return registers[add]
    return ram[add]

def SetAdd (add, value) -> None:
    if add in registers:
        registers[add] = value
    else:
        ram[add] = value


import time

while True:
    time.sleep(0.05)  # 20 hrtz....
    lineNumber = registers["101011"]
    print(f"\n\n\nLine: {lineNumber}")
    if lineNumber >= len(binary):
        break
    print(f"Code: {binary[lineNumber]}")
    
    # interpreting the code
    line = binary[lineNumber].split('_')
    opCode = line[0]
    ops = line[1:]

    if opCode == "001":
        if len(ops) > 2:
            mem = int(ops[2], 2)
        elif ops[0] in registers:
            if ops[0] in ["100110", "100111"]:
                mem = ram['{0:06b}'.format(registers[ops[0]])]
                #mem = ram[str(registers[ops[0]])]
            else:
                mem = registers[ops[0]]
        else: # ops[0] != "101100":
            mem = ram[ops[0]]
        
        if ops[1] in registers:
            registers[ops[1]] = mem
        else:
            ram[ops[1]] = mem
    elif opCode == "010":
        # getting the two registers being read
        bus1 = 0b00000000
        bus2 = 0b00000000
        if ops[1] in ["100010", "100011", "101011", "100001"]:
            bus1 |= registers[ops[1]]
        else:
            bus2 |= registers[ops[1]]
        
        if ops[2] in ["100010", "100011", "101011", "100001"]:
            bus1 |= registers[ops[2]]
        else:
            bus2 |= registers[ops[2]]

        # getting and calling the lambda function
        output = opCodes[ops[0]](bus1, bus2)
        registers[ops[3]] = output
        print(f"Bus1: {bus1}, Bus2: {bus2}; {ops[1]}, {ops[2]}; {output}")
    elif opCode == "011":
        if len(ops) > 1:
            stackCodes[ops[0]](ops[1])
        else:
            stackCodes[ops[0]]()
    elif opCode == "101":
        pointerCodes[ops[0]](ops[1], ops[2])
    
    print("\nRam:")
    for key in ram:
        if ram[key]:
            print(f"{key}: {ram[key]}")
    print("\nRegisters:")
    for reg in registers:
        if registers[reg]:
            print(f"{regNames[reg]}: {registers[reg]}")
    
    print(f"\nStack: {stack[:stackCounter]}\n")
    
    #if lineNumber in [51, 46]:
    #    input(">> ")

    # incrementing the line count
    registers["101011"] += 1

