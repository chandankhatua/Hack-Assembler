import re

#  Accepts file.asm, reads assembly language command, parses it and provides convenient access 
#  to command's components (fields and symbols). It also removes all white space and comments.

class Parser():
    dest0 = []
    jump0 = []
    comp0 = []
    val = []
    asm = []

    def __init__(self, file):
        self.file = file
        
        # os.chdir(r"C:\Users\lenovo\Desktop\New folder\Tests\rect")

    def rf(self):
        
        with open(self.file, 'r') as rf:
            for line in rf.readlines():
                # removes all comments and whitespace
                if(not line.startswith("//")):
                    if line.strip() != (""):
                        self.asm.append(line.strip().split()[0])

        return(self.asm)

    @staticmethod
    def load_val(line):
        val = line.split("@")[1]
        return '{:015b}'.format(int(val))

    @staticmethod
    def dest(line):
        if len(line.split("=")) == 2:
            dest0 = re.split("=", line)[0]
        else:
            dest0 = "null"
        return dest0

    @staticmethod
    def comp(line):
        if len(re.split("=|;",line)) == 3:
            comp0 = re.split("=|;", line)[1]
        elif len(re.split("=",line)) == 2:
            comp0 = re.split("=", line)[1]
        else:
            comp0 = re.split(";", line)[0]
        return comp0

    @staticmethod
    def jump(line):
        if len(line.split(";")) == 2:
            jump0 = re.split(";", line)[1]
        else:
            jump0 = "null"
        return jump0

    @staticmethod
    def label(line):
        if line.startswith("("):
            return line
