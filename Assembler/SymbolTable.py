class SymTable():
    
    predefined_symbols={
        "SP": '0',
        "LCL":'1',
        "ARG":'2',
        "THIS":'3',
        "THAT":'4',
        "R0":'0',
        "R1":'1',
        "R2":'2',
        "R3":'3',
        "R4":'4',
        "R5":'5',
        "R6":'6',
        "R7":'7',
        "R8":'8',
        "R9":'9',
        "R10":'10',
        "R11":'11',
        "R12":'12',
        "R13":'13',
        "R14":'14',
        "R15":'15',
        "SCREEN":'16384',
        "KBD":'24576'
    }
    def __init__(self):
        # Initializes symbol table with all predefined symbols - symbols, labels and variables and their pre-allocated RAM addresses.  
        self.symbol_table=self.predefined_symbols
    
    @staticmethod
    def addEntry(self,symbol,address):
        # Adds a pair (symbol, address) to table.
        self.symbol_table.update({symbol:address})
    
    def contains(self,symbol):
        # Checks if the symbol is in the table or not. Returns boolean. 
        return self.symbol_table.get(symbol)
    
    def GetAddress(self,symbol):
        # Returns address associated with the symbol.
        return self.symbol_table.get(symbol)

