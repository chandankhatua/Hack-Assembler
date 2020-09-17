# Hack-Assembler

An assembler that translates a symbolic machine language, also known as assembly, into into binary 0s and 1s. The resultig binary code executes as-is on the Hack platform. Translation techniques include parsing, a symbol table, and macro-assembly(labels).

This is a program, written in Python 3, that translates symbolic assembly code commands into 16-bit binary code.

# Usage
Hack Assembler reads an assembly program - such as Add.asm - located in data/input and produces a translated file - Add.hack - in the same location(data/input).
Additional a compare file is also given in the data/compare folder for each program(like Add_cmpr.hack).

Examples:
To translate Add.asm, use this command-line argument from the root folder: Assembler.py Add.asm
