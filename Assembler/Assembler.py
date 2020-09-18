import os, sys
from SymbolTable import SymTable
from Parser import Parser
from code_ import Code

variable_addr = 16

# _____________________________C-INSTRUCTION____________________________________________________________
def C_intstruction(parserObj, intstruction):

    d0 = parserObj.dest(intstruction)  # parsed destination
    c0 = parserObj.comp(intstruction)  # parsed computation
    j0 = parserObj.jump(intstruction)  # parsed jump

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
def A_instruction(parserObj, SymTableObj, intstruction=''):
    global variable_addr
    var = intstruction.split("@")[1]
    if intstruction[1].isdigit() == True:  # integer
        value = parserObj.load_val(intstruction)
    elif SymTable.contains(SymTableObj, var) != None:
        value_dec = SymTable.GetAddress(SymTableObj, var)
        value = parserObj.load_val("@{}".format(value_dec))
    else:
        # adding variable to symboltable
        SymTable.addEntry(SymTableObj, var, str(variable_addr))
        variable_addr += 1
        value_dec = SymTable.GetAddress(SymTableObj, var)
        value = parserObj.load_val("@{}".format(value_dec))

    return "0{}".format(value)
#________________________________________________________________________________________________________

###====================FIRST PASS(Checking and storing 'Labels' in SymbolTable)=======================###
def firstPass(SymTableObj, pars_file):
    addr=0
    for i in pars_file:
        if i[0] == "(":  # some unbound method problem
            SymTable.addEntry(SymTableObj, i.strip(r"(|)"), addr)  # ...solved by passing the instance
        else:
            addr+=1

    print("Symbol Table\n",SymTableObj.symbol_table)   # Printing the symbol table
    print()

###=================SECOND PASS(Storing variable with add and translating each line)==================###
    
# - A_INSTRUCTION : @Xxx, Xxx is either a symbol or a decimal
# - C_INSTRUCTION : dest=comp;jump
def secondPass(parserObj, SymTableObj, pars_file, output_filename):
    for i in pars_file:

        if i[0] == "@":  # A-instruction
            out = A_instruction(parserObj, SymTableObj,i)
        elif i[0] == "(":  # Label
            # out = Label(i)
            continue
        else:  # C-instruction
            out = C_intstruction(parserObj,i)

        # Writing the output to file
        with open(output_filename,"a") as mcode:
            mcode.write(f"{out}\n")

    print("....Completed....") # Completion message

def main():

    if len(sys.argv) == 2:
        for root, dirs, files in os.walk('.\\data\\input_output\\'):
            for file in files:
                if file == sys.argv[1]:
                    path = os.path.join(root, file)
    else:
        sys.exit(1)

    outfilename = path.replace("asm","hack")

    # initialising the symbol table
    s = SymTable()
    # Initialising the Parser
    p = Parser(path)
    # Storing the parsed file
    pars_file = p.rf()
    
    print(f"Parsed file\n{pars_file}\n")    

    firstPass(s, pars_file)
    secondPass(p, s, pars_file, outfilename)

if __name__ == "__main__":
    main()
