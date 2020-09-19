from SymbolTable import SymTable
from Parser import Parser
from code_ import Code
import os

variable_addr = 16
addr=0

#   initialising the symbol table
s = SymTable()
#   Initialising the Parser
p = Parser("C:\\Users\\lenovo\\Desktop\\New folder\\data\\input_output\\Add.asm")
#   Storing the parsed file
pars_file = p.rf()

print(f"Parsed File\n{pars_file}\n")    #printing parsed file

# _____________________________C-INSTRUCTION____________________________________________________________
def C_intstruction(intstruction):

    d0 = p.dest(intstruction)  # parsed destination
    c0 = p.comp(intstruction)  # parsed computation
    j0 = p.jump(intstruction)  # parsed jump

    # Translation C-instruction-----------------------------------------------
    d = Code.dest(d0)  # Destination in binary

    if Code.comp("0", c0) != None:  # Comp in binary
        c = Code.comp("0", c0)
        a = 0
    else:
        c = Code.comp("1", c0)
        a = 1

    j = Code.jump(j0)  # Jump in binary

    # final output of c-instruction
    return "111{0}{1}{2}{3}".format(a, c, d, j)
#________________________________________________________________________________________________________


#_______________________________A-INSTRUCTION____________________________________________________________
def A_instruction(intstruction=''):
    global variable_addr
    var = intstruction.split("@")[1]
    if intstruction[1].isdigit() == True:  # integer
        value = p.load_val(intstruction)
    elif SymTable.contains(s, var) != None:
        value_dec = SymTable.GetAddress(s, var)
        value = p.load_val("@{}".format(value_dec))
    else:
        # adding variable to symboltable
        SymTable.addEntry(s, var, str(variable_addr))
        variable_addr += 1
        value_dec = SymTable.GetAddress(s, var)
        value = p.load_val("@{}".format(value_dec))

    return "0{}".format(value)
#________________________________________________________________________________________________________


###====================FIRST PASS(Checking and storing 'Labels' in SymbolTable)=======================###
for i in pars_file:
    if i[0] == "(":  # some unbound method problem
        SymTable.addEntry(s, i.strip(r"(|)"), addr)  # ...solved by passing the instance
    else:
        addr+=1

print("Symbol Table\n",s.symbol_table)   # Printing the symbol table
print()

###=================SECOND PASS(Storing variable with add and translating each line)==================###
    
# - A_INSTRUCTION : @Xxx, Xxx is either a symbol or a decimal
# - C_INSTRUCTION : dest=comp;jump

print("Machine Code\n")
for i in pars_file:

    if i[0] == "@":  # A-instruction
        out = A_instruction(i)
    elif i[0] == "(":  # Label
        # out = Label(i)
        continue
    else:  # C-instruction
        out = C_intstruction(i)

    print(f"{out}\n")
    # Writing the output to file
    # with open("RectL.hack","a") as mcode:
    #     mcode.write(f"{out}\n")

print("done") # Completion message
