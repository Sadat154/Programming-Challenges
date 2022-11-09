

def rTm(rods):
    rodsToMeters = rods * 5.0292
    return rodsToMeters


def rTf(rodsToMeters):
    rodsToFeet = rodsToMeters / 0.3048
    return rodsToFeet

def rTmi(rodsToMeters):
    rodsToMiles = rodsToMeters / 1609.34
    return rodsToMiles

def rTfu(rods):
    rodsToFurlongs = rods / 40
    return rodsToFurlongs

def minutes(rodsToMiles):
    rodMinutes = (rodsToMiles / 3.1) * 60
    return rodMinutes


def run():
    rods = float(input("Input Rods: "))
    print(f"Meters: {rTm(rods)}")
    print(f"Feet: {rTf(rTm(rods))}")
    print(f"Miles: {rTmi(rTm(rods))}")
    print(f"Furlongs: {rTfu(rods)}")
    print(f"Minutes to walk {rods}: {minutes(rTmi(rTm(rods)))}")

if __name__ == "__main__":
    run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Skeleton Program for the AQA AS1 Summer 2020 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS1 Programmer Team
# developed in a Python 3 environment

# Version number: 0.0.0

EMPTY_STRING = ""
MAX_WIDTH = 100
MAX_HEIGHT = 100

class FileHeader:
  def __init__(self):
    self.Title = EMPTY_STRING
    self.Width = MAX_WIDTH
    self.Height = MAX_HEIGHT
    self.FileType = EMPTY_STRING 

def DisplayError(ErrorMessage):
  """

  :parameters: String
  :Description: Takes in a string and prints it as an error message
  """
  print("Error: ", ErrorMessage)

def PrintHeading(Heading):
  """

  :parameters: String
  :Description: Takes in the title of the file and prints it as well as "=" with length equal to the title on the next line
  """
  print(Heading)
  HeadingLength = len(Heading)
  for Position in range(1, HeadingLength + 1):
    print('=', end='')
  print()

def DisplayImage(Grid, Header):
  """

  :parameters: list, object
  :description: Displays the image
  """
  print()
  PrintHeading(Header.Title)
  for ThisRow in range(Header.Height):
    for ThisColumn in range(Header.Width):
      print(Grid[ThisRow][ThisColumn], end='')
    print()

def SaveImage(Grid, Header):
  """

  :parameters:  List, Object
  :description: Allows user to save changes theyve made to the file

  """
  print("The current title of your image is: " + Header.Title)
  Answer = input("Do you want to use this as your filename? (Y/N) ")
  if Answer == "N" or Answer == "n":
    FileName = input("Enter a new filename: ")
  else:
    FileName = Header.Title
  FileOut = open(FileName + ".txt", 'w')
  FileOut.write(Header.Title + '\n')
  for Row in range(Header.Height):
    for Column in range(Header.Width):
      FileOut.write(Grid[Row][Column])
    FileOut.write('\n')
  FileOut.close()

def EditImage(Grid, Header):
  """

  :parameters: List, Object
  :description: Allows user to choose if they want to edit an image or not, if they do, they can replace symbols with their own choice
  :return type: List
  """
  DisplayImage(Grid, Header)
  Answer = EMPTY_STRING
  while Answer != "N":
    Symbol = EMPTY_STRING
    NewSymbol = EMPTY_STRING
    while len(Symbol) != 1:
      Symbol = input("Enter the symbol you want to replace: ")
    while len(NewSymbol) != 1:
      NewSymbol = input("Enter the new symbol: ")
    for ThisRow in range(Header.Height):
      for ThisColumn in range(Header.Width):
        if Grid[ThisRow][ThisColumn] == Symbol:
          Grid[ThisRow][ThisColumn] = NewSymbol
    DisplayImage(Grid, Header)
    Answer = input("Do you want to make any further changes? (Y/N) ")
  return Grid

def ConvertChar(PixelValue):
  """

  :parameter: Integer
  :description: Depending on the pixelvalue (shade level) in the file it returns an ascii character
  :return type: String
  """
  if PixelValue <= 32:
    AsciiChar = '#'
  elif PixelValue <= 64:
    AsciiChar = '&'
  elif PixelValue <= 96:
    AsciiChar = '+'
  elif PixelValue <= 128:
    AsciiChar = ';'
  elif PixelValue <= 160:
    AsciiChar = ':'
  elif PixelValue <= 192:
    AsciiChar = ','
  elif PixelValue <= 224:
    AsciiChar = '.'
  else:
    AsciiChar = ' '
  return AsciiChar

def LoadGreyScaleImage(FileIn, Grid, Header):
  """

  :parameters: String, List, Object
  :description: returns the shade of each row and column
  :return Type: List

  """
  try:
    for Row in range(Header.Height):
      for Column in range(Header.Width):
        NextPixel = FileIn.readline()
        PixelValue = int(NextPixel)
        Grid[Row][Column] = ConvertChar(PixelValue)
  except:
    DisplayError("Image data error")    
  return Grid
  
def LoadAsciiImage(FileIn, Grid, Header):
  """

  :parameters: String, List, Object
  :description: If there is no error returns Grid which stores the actual image in rows and columns
  :return type: List
  """
  try:
    ImageData = FileIn.readline()
    NextChar = 0
    for Row in range(Header.Height):
      for Column in range(Header.Width):
        Grid[Row][Column] = ImageData[NextChar]
        NextChar += 1
  except:
    DisplayError("Image data error")
  return Grid

def LoadFile(Grid, Header):
  """

  :parameters:  List, Object
  :description: Opens a file, determines if the file stores an Ascii image or a Grey Scale image and stores the image in the variable grid which is then returned along ith the header
  :return type:  List, Object
  """
  FileFound = False
  FileTypeOK = False
  FileName = input("Enter filename to load: ")
  try:
    FileIn = open(FileName + ".txt", 'r')
    FileFound = True
    HeaderLine = FileIn.readline()
    Fields = HeaderLine.split(',')
    Header.Title = Fields[0]
    Header.Width = int(Fields[1])
    Header.Height = int(Fields[2])
    Header.FileType = Fields[3]
    Header.FileType = Header.FileType[0]
    if Header.FileType == 'A':  
      Grid = LoadAsciiImage(FileIn, Grid, Header)
      FileTypeOK = True
    elif Header.FileType == 'G': 
      Grid = LoadGreyScaleImage(FileIn, Grid, Header)
      FileTypeOK = True
    FileIn.close()
    if not FileTypeOK:
      DisplayError("Unknown file type")
    else:
      DisplayImage(Grid, Header)
  except:
    if not FileFound:
      DisplayError("File not found")
    else:
      DisplayError("Unknown error")
  return Grid, Header

def SaveFile(Grid, Header):
  """

  :parameters: List, Object
  :description: Opens the file and overwrites it with changes made by the user then saves the file

  """
  FileName = input("Enter filename: ")
  FileOut = open(FileName + ".txt", 'w')
  FileOut.write(Header.Title + ',' + str(Header.Width) + ',' + str(Header.Height) + ',' + 'A' + '\n')
  for Row in range(Header.Height):
    for Column in range(Header.Width):
      FileOut.write(Grid[Row][Column])
  FileOut.close()

def ClearGrid(Grid):
  """

  :parameters: List
  :Description: Clears the grid
  :return Type: List

  """
  for Row in range(MAX_HEIGHT):
    for Column in range(MAX_WIDTH):
      Grid[Row][Column] = '.'
  return Grid
   
def DisplayMenu():
  """

  :Description: Outputs all the options the user has

  """
  print()
  print("Main Menu")
  print("=========")
  print("L - Load graphics file") 
  print("D - Display image")
  print("E - Edit image")
  print("S - Save image")
  print("X - Exit program") 
  print()

def GetMenuOption():
  """

  :description: Takes in a user input and returns it
  :return Type: String

  """
  MenuOption = EMPTY_STRING
  while len(MenuOption) != 1:
    MenuOption = input("Enter your choice: ")
  return MenuOption
  
def Graphics():
  """

  :description: Based on the user choice from GetMenuOption, it carries out the task then asks if they want to save the image or not, following through with their choice.

  """
  Grid = [['' for Column in range(MAX_WIDTH)] for Row in range(MAX_HEIGHT)]
  Grid = ClearGrid(Grid)
  Header = FileHeader()
  ProgramEnd = False
  while not ProgramEnd:
    DisplayMenu()
    MenuOption = GetMenuOption()
    if MenuOption == 'L':
      Grid, Header = LoadFile(Grid, Header)
    elif MenuOption == 'D':
      DisplayImage(Grid, Header) 
    elif MenuOption == 'E':
      Grid = EditImage(Grid, Header) 
    elif MenuOption == 'S':    
      SaveImage(Grid, Header)
    elif MenuOption == 'X':
      ProgramEnd = True
    else:
      print("You did not choose a valid menu option. Try again")
  print("You have chosen to exit the program")
  Answer = input("Do you want to save the image as a graphics file? (Y/N) ")
  if Answer == "Y" or Answer == "y":
    SaveFile(Grid, Header)
      
if __name__ == "__main__":
  Graphics()         
