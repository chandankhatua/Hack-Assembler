##Overall logic
- Initialization
  - Of Parser
  - Of Symbol Table
• First Pass: Read all commands, only paying attention to labels and
updating the symbol table
• Restart reading and translating commands
• Main Loop:
q Get the next Assembly Language Command and parse it
q For A-commands: Translate symbols to binary addresses
q For C-commands: get code for each part and put them together
q Output the resulting machine language command
