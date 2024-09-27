from dataclasses import dataclass 
import sys

verbiage = {
  "messageS": "Введіть ціле число s: ",
  "messageF": "Введіть ціле число f: ",
  "messageD": "Введіть ціле число d: ",
  "messageProceed": "Бажаєте повторити операцію над новоми числами? y / n \n",
  "messageFactorial": "Введіть ціле число: ",
  "errorMessage": "Було введено недопустиме значення"
}

@dataclass
class DivisorParams():
    s: int
    f: int
    d: int

class Program:
  @staticmethod
  def __factorial(n: int):
    if n == 0 or n == 1:
      return 1
    
    return n * Program.__factorial(n - 1)

  @staticmethod
  def __getDivisors(params: DivisorParams) -> list[float]:
    if params.s >= params.f:
      raise ValueError(f"Unexpected value: {params.f}. F should be greater than S")
    
    if params.d == 0:
      raise ValueError("Zero division is not defined")

    if not params.s.is_integer() or not params.f.is_integer() or params.s <= 0 or params.f <= 0:
      raise ValueError(f"Enter valid argument. Composition s={params.s} and f={params.f} can not be handled")

    result = []

    for i in range(params.s, params.f + 1):
      if i % params.d == 0:
        result.append(i)
    
    return result
  
  @staticmethod
  def __logDivisors(params: DivisorParams):
    for i in Program.__getDivisors(params):
      print(i)
  
  @staticmethod
  def executeDivisors():
    s = input(verbiage["messageS"])
    f = input(verbiage["messageF"])
    d = input(verbiage["messageD"])

    paramsObj = DivisorParams(int(s), int(f), int(d))

    Program.__logDivisors(paramsObj)
      
  @staticmethod
  def executeFactorial():
    n = int(input(verbiage["messageFactorial"]))

    print(Program.__factorial(n))

  @staticmethod
  def executeLoop(fn):
    while True: 
      fn()

      response = input(verbiage["messageProceed"])

      if (response == "y"):
        continue
      elif (response == "n"):
        break
      else:
        raise ValueError(verbiage["errorMessage"])

if (sys.argv[1] == "factorial"):
    Program.executeLoop(Program.executeFactorial)
elif (sys.argv[1] == "divisors"):
    Program.executeLoop(Program.executeDivisors)
else: 
    raise ValueError("App has been run with wrong args")