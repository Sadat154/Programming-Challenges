# Skeleton Program for the AQA AS Summer 2023 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in a Python 3 environment

# Version number: 0.0.0


EMPTY_STRING = ""
HI_MEM = 20
MAX_INT = 127  # 8 bits available for operand (two's complement integer)
PC = 0
ACC = 1
STATUS = 2
TOS = 3
ERR = 4


class AssemblerInstruction:
    def __init__(self):
        self.OpCode = EMPTY_STRING
        self.OperandString = EMPTY_STRING
        self.OperandValue = 0


def DisplayMenu():
    """
    Description: Displays the menu options

    """
    print()
    print("Main Menu")
    print("=========")
    print("L - Load a program file")
    print("D - Display source code")
    print("E - Edit source code")
    print("A - Assemble program")
    print("R - Run the program")
    print("X - Exit simulator")
    print()


def GetMenuOption():
    Choice = EMPTY_STRING
    while len(Choice) != 1:
        Choice = input("Enter your choice: ")
    return Choice[0]


def ResetSourceCode(SourceCode):
    for LineNumber in range(HI_MEM):
        SourceCode[LineNumber] = EMPTY_STRING
    return SourceCode


def ResetMemory(Memory):
    for LineNumber in range(HI_MEM):
        Memory[LineNumber].OpCode = EMPTY_STRING
        Memory[LineNumber].OperandString = EMPTY_STRING
        Memory[LineNumber].OperandValue = 0
    return Memory


def DisplaySourceCode(SourceCode):
    print()
    NumberOfLines = int(SourceCode[0])
    for LineNumber in range(0, NumberOfLines + 1):
        print("{:>2d} {:<40s}".format(LineNumber, SourceCode[LineNumber]))
    print()


def LoadFile(SourceCode):
    """

    :parameters: String
    :description: Loads the file and stores it in source code before displaying it
    :return type: String
    """
    FileExists = False
    SourceCode = ResetSourceCode(SourceCode)
    LineNumber = 0
    FileName = input("Enter filename to load: ")
    try:
        FileIn = open(FileName + ".txt", 'r')
        FileExists = True
        Instruction = FileIn.readline()
        while Instruction != EMPTY_STRING:
            LineNumber += 1
            SourceCode[LineNumber] = Instruction[:-1]
            Instruction = FileIn.readline()
        FileIn.close()
        SourceCode[0] = str(LineNumber)
    except:
        if not FileExists:
            print("Error Code 1")
        else:
            print("Error Code 2")
            SourceCode[0] = str(LineNumber - 1)
    if LineNumber > 0:
        DisplaySourceCode(SourceCode)
    return SourceCode


def EditSourceCode(SourceCode):
    """

    :parameters: String
    :description: Allows user to edit a certain line and then adjusts source code in accordance to the users inputs before displaying the source code to the user
    :return type: String
    """
    LineNumber = int(input("Enter line number of code to edit: "))
    print(SourceCode[LineNumber])
    Choice = EMPTY_STRING
    while Choice != "C":
        Choice = EMPTY_STRING
        while Choice != "E" and Choice != "C":
            print("E - Edit this line")
            print("C - Cancel edit")
            Choice = input("Enter your choice: ")
        if Choice == "E":
            SourceCode[LineNumber] = input("Enter the new line: ")
        DisplaySourceCode(SourceCode)
    return SourceCode


def UpdateSymbolTable(SymbolTable, ThisLabel, LineNumber):
    """

    :parameters: Dict, Str, Int
    :description:Updates Symboltable dict with the label of the current instruction
    :return type: Dict
    """
    if ThisLabel in SymbolTable:
        print("Error Code 3")
    else:
        SymbolTable[ThisLabel] = LineNumber
    return SymbolTable


def ExtractLabel(Instruction, LineNumber, Memory, SymbolTable):
    """

    :parameters: String, Int, List, Dict
    :description: Obtains the Lablel and stores it in memory
    :return type: Dict, List
    """
    if len(Instruction) > 0:
        ThisLabel = Instruction[0:5]
        ThisLabel = ThisLabel.strip()
        if ThisLabel != EMPTY_STRING:
            if Instruction[5] != ':':
                print("Error Code 4")
                Memory[0].OpCode = "ERR"
            else:
                SymbolTable = UpdateSymbolTable(SymbolTable, ThisLabel, LineNumber)


    return SymbolTable, Memory


def ExtractOpCode(Instruction, LineNumber, Memory):
    """

    :parameters: String, Int, List
    :description: Obtains the opcode and stores it in memory and returns an error if the opcode is invalid
    :return type: List
    """
    if len(Instruction) > 9:
        OpCodeValues = ["LDA", "STA", "LDA#", "HLT", "ADD", "JMP", "SUB", "CMP#", "BEQ", "SKP", "JSR", "RTN", "   "]
        Operation = Instruction[7:10]
        if len(Instruction) > 10:
            AddressMode = Instruction[10:11]
            if AddressMode == '#':
                Operation += AddressMode
        if Operation in OpCodeValues:
            Memory[LineNumber].OpCode = Operation
        else:
            if Operation != EMPTY_STRING:
                print("Error Code 5")
                Memory[0].OpCode = "ERR"
    return Memory


def ExtractOperand(Instruction, LineNumber, Memory):
    """

    :parameters: String, Int, List
    :description: Obtains the operand and stores it in memory
    :return type: List
    """
    if len(Instruction) >= 13:
        Operand = Instruction[12:]
        ThisPosition = -1
        for Position in range(len(Operand)):
            if Operand[Position] == '*':
                ThisPosition = Position
        if ThisPosition >= 0:
            Operand = Operand[:ThisPosition]
        Operand = Operand.strip()
        Memory[LineNumber].OperandString = Operand
    return Memory


def PassOne(SourceCode, Memory, SymbolTable):
    """

    :parameters: String, List, Dict
    :description: Obtains the necessary details from the first pass
    :return type: List, Dict
    """
    NumberOfLines = int(SourceCode[0])
    for LineNumber in range(1, NumberOfLines + 1):
        Instruction = SourceCode[LineNumber]
        SymbolTable, Memory = ExtractLabel(Instruction, LineNumber, Memory, SymbolTable)
        Memory = ExtractOpCode(Instruction, LineNumber, Memory)
        Memory = ExtractOperand(Instruction, LineNumber, Memory)
    return Memory, SymbolTable


def PassTwo(Memory, SymbolTable, NumberOfLines):
    """

    :parameters: List, String, Int
    :description: Obtains the necessary details from the second pass
    :return type: List
    """
    for LineNumber in range(1, NumberOfLines + 1):
        Operand = Memory[LineNumber].OperandString
        if Operand != EMPTY_STRING:
            if Operand in SymbolTable:
                OperandValue = SymbolTable[Operand]
                Memory[LineNumber].OperandValue = OperandValue
            else:
                try:
                    OperandValue = int(Operand)
                    Memory[LineNumber].OperandValue = OperandValue
                except:
                    print("Error Code 6")
                    Memory[0].OpCode = "ERR"
    return Memory


def DisplayMemoryLocation(Memory, Location):
    print("*  {:<5s}{:<5d} |".format(Memory[Location].OpCode, Memory[Location].OperandValue), end='')


def DisplaySourceCodeLine(SourceCode, Location):
    print(" {:>3d}  |  {:<40s}".format(Location, SourceCode[Location]))


def DisplayCode(SourceCode, Memory):
    """

    :parameters: String, List
    :description: Displays the source code in a nice format

    """
    print("*  Memory     Location  Label  Op   Operand Comment")
    print("*  Contents                    Code")
    NumberOfLines = int(SourceCode[0])
    DisplayMemoryLocation(Memory, 0)
    print("   0  |")
    for Location in range(1, NumberOfLines + 1):
        DisplayMemoryLocation(Memory, Location)
        DisplaySourceCodeLine(SourceCode, Location)


def Assemble(SourceCode, Memory):
    """

    :parameters: String, List
    :description: Assembles source code into memory
    :return type: List
    """
    Memory = ResetMemory(Memory)
    NumberOfLines = int(SourceCode[0])
    SymbolTable = {}
    Memory, SymbolTable = PassOne(SourceCode, Memory, SymbolTable)
    if Memory[0].OpCode != "ERR":
        Memory[0].OpCode = "JMP"
        if "START" in SymbolTable:
            Memory[0].OperandValue = SymbolTable["START"]
        else:
            Memory[0].OperandValue = 1
        Memory = PassTwo(Memory, SymbolTable, NumberOfLines)
    return Memory


def ConvertToBinary(DecimalNumber):
    """

    :parameters: Int
    :description: Converts Decimal to Binary string
    :return type: String
    """
    BinaryString = EMPTY_STRING
    while DecimalNumber > 0:
        Remainder = DecimalNumber % 2
        Bit = str(Remainder)
        BinaryString = Bit + BinaryString
        DecimalNumber = DecimalNumber // 2
    while len(BinaryString) < 4:
        BinaryString = '0' + BinaryString
    return BinaryString


def ConvertToDecimal(BinaryString):
    """

    :parameters: String
    :description: Converts binary string value to decimal
    :return type: Int
    """
    DecimalNumber = 0
    for Bit in BinaryString:
        BitValue = int(Bit)
        DecimalNumber = DecimalNumber * 2 + BitValue
    return DecimalNumber


def DisplayFrameDelimiter(FrameNumber):
    """

    :parameters: Int
    :description: Displays the Frame number

    """
    if FrameNumber == -1:
        print("***************************************************************")
    else:
        print("****** Frame", FrameNumber, "************************************************")


def DisplayCurrentState(SourceCode, Memory, Registers):
    """

    :parameters: String, List, List
    :description: Displays the status

    """
    print("*")
    DisplayCode(SourceCode, Memory)
    print("*")
    print("*  PC: ", Registers[PC], " ACC: ", Registers[ACC], " TOS: ", Registers[TOS])
    print("*  Status Register: ZNVC")
    print("*                  ", ConvertToBinary(Registers[STATUS]))
    DisplayFrameDelimiter(-1)


def SetFlags(Value, Registers):
    """

    :parameters: Int, List
    :description: Assigns a flag to an operation
    :return type: List
    """
    if Value == 0:
        Registers[STATUS] = ConvertToDecimal("1000")
    elif Value < 0:
        Registers[STATUS] = ConvertToDecimal("0100")
    elif Value > MAX_INT or Value < -(MAX_INT + 1):
        Registers[STATUS] = ConvertToDecimal("0011")
    else:
        Registers[STATUS] = ConvertToDecimal("0000")
    return Registers


def ReportRunTimeError(ErrorMessage, Registers):
    """

    :parameters: String, List
    :description:Outputs the error code of a run time error
    :return type: List
    """
    print("Run time error:", ErrorMessage)
    Registers[ERR] = 1
    return Registers


def ExecuteLDA(Memory, Registers, Address):
    """

    :parameters: List, List, Int
    :description: Loads data in the location specified by the operand into the accumulator
    :return type: List
    """
    Registers[ACC] = Memory[Address].OperandValue
    Registers = SetFlags(Registers[ACC], Registers)
    return Registers


def ExecuteSTA(Memory, Registers, Address):
    """

    :parameters: List, List, Int
    :description: Stores the contents of the accumulator in the memory location specified by the address in the operand
    :return type: List
    """
    Memory[Address].OperandValue = Registers[ACC]
    return Memory


def ExecuteLDAimm(Registers, Operand):
    """

    :parameters: List, Int
    :description: Loads the operand into the accumulator and checks the flags
    :return type: List
    """
    Registers[ACC] = Operand
    Registers = SetFlags(Registers[ACC], Registers)
    return Registers


def ExecuteADD(Memory, Registers, Address):
    """

    :parameters: List, List, Int
    :description: Addition takes place and flags are set again as well as errors being sent if there are any
    :return type: List
    """
    Registers[ACC] = Registers[ACC] + Memory[Address].OperandValue
    Registers = SetFlags(Registers[ACC], Registers)
    if Registers[STATUS] == ConvertToDecimal("001"):
        ReportRunTimeError("Overflow", Registers)
    return Registers


def ExecuteSUB(Memory, Registers, Address):
    """

    :parameters: List, List, Int
    :description: Subtraction takes place and flags are set again as well as errors being sent if there are any
    :return type: List
    """
    Registers[ACC] = Registers[ACC] - Memory[Address].OperandValue
    Registers = SetFlags(Registers[ACC], Registers)
    if Registers[STATUS] == ConvertToDecimal("001"):
        ReportRunTimeError("Overflow", Registers)
    return Registers


def ExecuteCMPimm(Registers, Operand):
    """

    :parameters: List, Int
    :description: This subroutine is called when immediate addressing is used, the operand is set
    :return type: List
    """
    Value = Registers[ACC] - Operand
    Registers = SetFlags(Value, Registers)
    return Registers


def ExecuteBEQ(Registers, Address):
    """

    :parameters: List, Integer
    :description: Checks if the Z flag is set to 1 which would mean the value at ACC is equal to the operand then jumps to the branch if conditions are met
    :return type: List
    """
    StatusRegister = ConvertToBinary(Registers[STATUS]) # Status stores the flags
    FlagZ = StatusRegister[0]
    if FlagZ == "1":
        Registers[PC] = Address
    return Registers


def ExecuteJMP(Registers, Address):
    """

    :parameters: List, Int
    :description: Jumps to the location specified by the address/opcode thus PC is set to that location
    :return type: List
    """
    Registers[PC] = Address
    return Registers


def ExecuteSKP():
    return


def DisplayStack(Memory, Registers):
    """

    :parameters: List, List
    :description: Displays the contents of the stack

    """
    print("Stack contents:")
    print(" ----")
    for Index in range(Registers[TOS], HI_MEM):
        print("|{:>3d} |".format(Memory[Index].OperandValue))


    print(" ----")


def ExecuteJSR(Memory, Registers, Address):

    """
    Parameters: List, List, Int
    Description: Executes Jump to Subroutine, thus TOS is decremented since one space is being used now,
    Return Type: List, List
    """
    StackPointer = Registers[TOS] - 1
    Memory[StackPointer].OperandValue = Registers[PC]
    print(Registers)
    print(Registers[PC])
    Registers[PC] = Address
    Registers[TOS] = StackPointer
    DisplayStack(Memory, Registers)
    return Memory, Registers


def ExecuteRTN(Memory, Registers):

    """
    Parameters: List, List
    Description: Returns from the current subroutine, TOS is updated to point to the next item in the stack since one item has now been removed, hence there is now one more space available on the stack
    Return Type: List
    """
    StackPointer = Registers[TOS]
    Registers[TOS] += 1
    Registers[PC] = Memory[StackPointer].OperandValue
    return Registers


def Execute(SourceCode, Memory):

    """
    Parameters: String, String
    Description: Calls the necessary routines for each line in the source code

    """

    Registers = [0, 0, 0, 0, 0]
    Registers = SetFlags(Registers[ACC], Registers)
    Registers[PC] = 0
    Registers[TOS] = HI_MEM
    FrameNumber = 0
    DisplayFrameDelimiter(FrameNumber)
    DisplayCurrentState(SourceCode, Memory, Registers)
    OpCode = Memory[Registers[PC]].OpCode
    while OpCode != "HLT":
        FrameNumber += 1
        print()
        DisplayFrameDelimiter(FrameNumber)
        Operand = Memory[Registers[PC]].OperandValue

        print("*  Current Instruction Register: ", OpCode, Operand)
        Registers[PC] = Registers[PC] + 1
        if OpCode == "LDA":
            Registers = ExecuteLDA(Memory, Registers, Operand)
        elif OpCode == "STA":
            Memory = ExecuteSTA(Memory, Registers, Operand)
        elif OpCode == "LDA#":
            Registers = ExecuteLDAimm(Registers, Operand)
        elif OpCode == "ADD":
            Registers = ExecuteADD(Memory, Registers, Operand)
        elif OpCode == "JMP":
            Registers = ExecuteJMP(Registers, Operand)
        elif OpCode == "JSR":
            Memory, Registers = ExecuteJSR(Memory, Registers, Operand)
        elif OpCode == "CMP#":
            Registers = ExecuteCMPimm(Registers, Operand)
        elif OpCode == "BEQ":
            Registers = ExecuteBEQ(Registers, Operand)
        elif OpCode == "SUB":
            Registers = ExecuteSUB(Memory, Registers, Operand)
        elif OpCode == "SKP":
            ExecuteSKP()
        elif OpCode == "RTN":
            Registers = ExecuteRTN(Memory, Registers)
        if Registers[ERR] == 0:
            OpCode = Memory[Registers[PC]].OpCode
            DisplayCurrentState(SourceCode, Memory, Registers)
        else:
            OpCode = "HLT"
    print("Execution terminated")


def AssemblerSimulator():
    """

    Description:

    """
    SourceCode = [EMPTY_STRING for Lines in range(HI_MEM)]
    Memory = [AssemblerInstruction() for Lines in range(HI_MEM)]
    SourceCode = ResetSourceCode(SourceCode)
    Memory = ResetMemory(Memory)
    Finished = False
    while not Finished:
        DisplayMenu()
        MenuOption = GetMenuOption()
        if MenuOption == 'L':
            SourceCode = LoadFile(SourceCode)
            Memory = ResetMemory(Memory)
        elif MenuOption == 'D':
            if SourceCode[0] == EMPTY_STRING:
                print("Error Code 7")
            else:
                DisplaySourceCode(SourceCode)
        elif MenuOption == 'E':
            if SourceCode[0] == EMPTY_STRING:
                print("Error Code 8")
            else:
                SourceCode = EditSourceCode(SourceCode)
                Memory = ResetMemory(Memory)
        elif MenuOption == 'A':
            if SourceCode[0] == EMPTY_STRING:
                print("Error Code 9")
            else:
                Memory = Assemble(SourceCode, Memory)
        elif MenuOption == 'R':
            if Memory[0].OperandValue == 0:
                print("Error Code 10")
            elif Memory[0].OpCode == "ERR":
                print("Error Code 11")
            else:
                Execute(SourceCode, Memory)
        elif MenuOption == 'X':
            Finished = True
        else:
            print("You did not choose a valid menu option. Try again")
    print("You have chosen to exit the program")


if __name__ == "__main__":
    AssemblerSimulator()
