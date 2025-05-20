from enum import Enum

"""
NO RECURSIVE CALLS (unknown length; impossible for compiletime calculation)
variables declared inside a loop or function (aka a block) either need to be defined beforehand (global) or be given an address
    this allows the compiler to know where memory is
alloc and deallc require memory to be specified

push v, let v = pop

// a pointer to the memory (really just for memory areas; this ensures the compiler leaves the whole block alone)
// the user has to remember the size
// alloc only works on memory, not registers
let v = &alloc 0x1A, 0x1F;  // the compiler won't assign memory here ever

// dealloc (*v); idk about this. It doesn't seem like it has any use with how everything is setup as static

+, -, *, |, ~, ^, ~^, &, ~&, ~|, <<, >>
<, >, <=, >=, ==, !=  (no && and || bc/ it would be complicated)

let var = 4;

; endln

let == asignment

&pointer
*dereference

call foo (x, y, z) -> function calls

[0, 0, 0] = slice/array (needs to be pre-filled)
    converts to a pointer with known size (indexing == pointer + index)

@left var = 4;   var goes to bus 2
@right var = 2;  var goes to bus 1
@mem var = 1;    var goes to ram

or @0x1A and @DAX and @IAX for specifics

(the compiler will forcefully move any values if they get stuck in the way; but it'll try to be smart)

var -> @right;
var -> @left;
var -> @mem;
(this just means moving memory; it can also be used if replacing a value after an op)

the compiler does a pass where it places type annotations on everything and
    ... conversions when necessary

labels are done like:
    "label_A"
        goto "label_A"

Passes:
    1. calculating the usage frequency of each var in each block
    2. adding new type annotations & adding conversions to avoid overlaps
    3. when assigning a non-output add/reg, add an extra step of @out o = ...; o -> address of other var
    4. convert items to instructions
    5. conjoin instructions when possible and fix illegal steps
"""

rawFile = open(input("file >> ")).read()

splitters = [
    ["-", "->"], ["*"], ["+"], [">", ">>", ">="], ["<", "<<", "<="], ["=", "=="], ["&"], ["|"], ["!", "!^", "!="],
    ["["], ["]"], ["@"], [" "], ["@"], [";"], [":"], ["\n"], ["|"], ["~", "~^", "~&", "~|"], ["&"], ["^"], [","],
    ["("], [")"], ["\""]
]

# tokenizing the code
token = ""
tokens: list[str] = []
for (i, char) in enumerate(rawFile):
    kill = False
    oneLiner = False
    for split in splitters:
        if char == split[0]:
            oneLiner = True
            kill = True
            break
    for split in splitters:
        i2 = 1
        for s in split:
            if s == token:
                kill = True
                break
            i2 += 1
        if kill and i2 < len(split) and i < len(rawFile) - 1:
            new = token + rawFile[i + 1]
            if new in split:
                kill = False
    
    if oneLiner and char and token:
        tokens.append(token)
        token = ""
    token += char
    if kill:
        tokens.append(token)
        token = ""
tokens.append(token)

# removing comments
inComment = False
nonComments = []
for token in tokens:
    if token == "\n": inComment = False
    if token == "//": inComment = True
    if not inComment: nonComments.append(token)
tokens = nonComments

# combining tokens
totalToken = ""
newTokens = []
for (i, token) in enumerate(tokens):
    if token == '' or token == ' ' or token == '\n':
        if totalToken:
            newTokens.append(totalToken)
            totalToken = ""
        continue
    if i < len(tokens) - 1:
        kill = False
        for split in splitters:
            if token + tokens[i + 1] in split:
                totalToken += token
                kill = True
                break
        if kill: continue

    newTokens.append(totalToken + token)
    totalToken = ""
tokens = newTokens

layer = []
tokenLines = []
for token in tokens:
    if token == ";" or token == ":":
        tokenLines.append(layer)
        layer = []
    else:
        layer.append(token)

tokens = tokenLines

print(tokens)

registers = []
memory = []

# break the code into its blocks
# find all declarations in each block
# figure out what registers are used
# figure out the total memory allocation
# add type annotations and conversions for all variables (such as @right)


