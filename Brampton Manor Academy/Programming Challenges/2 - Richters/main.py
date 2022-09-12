richterList = [1.0,5.0,9.1,9.2,9.5]


def Joules(richter):
    return 10**((1.5*richter)+4.8)

def TNT(richter):
    Tons = Joules(richter) / (4.184*(10**9))
    return Tons

def run():
    print(f"Richter        Joules                     TNT")
    for i in range (len(richterList)):
      print(f"{richterList[i]:>2}{Joules(richterList[i]):>30} {TNT(richterList[i]):>30}")
    richter = float(input("Please enter a Richter scale value: "))
    print(f"Richter Value: {richter}")
    print(f"Equivalence in Joules: {Joules(richter)}")
    print(f"Equivalence in Tons of TNT {TNT(richter)}")

if __name__ == "__main__":
    run()
