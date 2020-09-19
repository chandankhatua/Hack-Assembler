## Overall logic
- Initialization
  - Of Parser
  - Of Symbol Table
- First Pass: Read all commands, only paying attention to labels and
  updating the symbol table
- Second Pass: Restart reading and translating commands
  - Get the parse file and start translation
  - For A-commands(@value/variable_name) : Translate symbols to binary addresses
  - For C-commands(dest=comp;jump): get code for each part and put them together
  - Output the resulting machine language command into a file

- Assembler.py is the main program that can be run from terminal(add Assembler to path).
- main.py is the same as Assembler.py but it  is executed from top to down.(path of the file has to be passed explicitly)
