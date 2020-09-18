## Overall logic
- Initialization
  - Of Parser
  - Of Symbol Table
- First Pass: Read all commands, only paying attention to labels and
  updating the symbol table
- Restart reading and translating commands

- Main Loop:
  - Get the parse file and start translation
  - For A-commands: Translate symbols to binary addresses
  - For C-commands: get code for each part and put them together
  - Output the resulting machine language command into a file
