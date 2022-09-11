richterList = [1.0,5.0,9.1,9.2,9.5]


def Joules(richter):
    Joules = 10**((1.5*richter)+4.8)
    return Joules

def TNT(richter):
    Tons = Joules(richter) / (4.184*(10**9))
    return Tons

def run():
    print("Richter             Joules             TNT")
    for i in range (len(richterList)):
      print(f"{richterList[i]}         {Joules(richterList[i])}        {TNT(richterList[i])}")
    richter = float(input("Please enter a Richter scale value: "))
    print(f"Richter Value: {richter}")
    print(f"Equivalence in Joules: {Joules(richter)}")
    print(f"Equivalence in Tons of TNT {TNT(richter)}")

if __name__ == "__main__":
    run()
