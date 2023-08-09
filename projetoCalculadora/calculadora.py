import time
import pyautogui
import tkinter

tk = tkinter.Tk()
tk.withdraw()

def CopiarColar():
        time.sleep(.01)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(.01)
        return tk.clipboard_get()


pyautogui.press("win")
time.sleep(0.1)
pyautogui.write("calculator")
pyautogui.press("enter")
time.sleep(0.1)

class Tecla:
    
    tecla1 = "1"
    pyautogui.moveTo(x=723, y=925)
    tecla2 = "2"
    pyautogui.moveTo(x=829, y=919)
    tecla3 = "3"
    pyautogui.moveTo(x=963, y=922)
    tecla4 = "4"
    pyautogui.moveTo(x=704, y=872)
    tecla5 = "5"
    pyautogui.moveTo(x=830, y=876)
    tecla6 = "6"
    pyautogui.moveTo(x=960, y=876)
    tecla7 = "7"
    pyautogui.moveTo(x=700, y=825)
    tecla8 = "8"
    pyautogui.moveTo(x=829, y=815)
    tecla9 = "9"
    pyautogui.moveTo(x=959, y=827)
    tecla0 = "0"
    pyautogui.moveTo(x=699, y=973)
    teclaapagar = ""
    pyautogui.moveTo(x=699, y=780)
    teclasoma= "+"
    pyautogui.moveTo(x=1093, y=973)
    teclamultiplicacao = "*"
    pyautogui.moveTo(x=1091, y=877)
    teclasubtracao = "-"
    pyautogui.moveTo(x=1088, y=922)
    tecladivisao = "/"
    pyautogui.moveTo(x=1094, y=822)
    teclaigual = "="
    pyautogui.moveTo(x=1219, y=944)
    time.sleep(0.1)

    pyautogui.moveTo(x=829, y=919)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(x=1091, y=877)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(x=704, y=872)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(x=1219, y=944)
    pyautogui.click()
    pyautogui.moveTo(x=658, y=703)
    pyautogui.doubleClick()

    
    def obterResultado(int):
        return CopiarColar()
    resultado = CopiarColar()
    print (resultado)
    

class Tecla:
     def __init__(self, x, y):
        self.x = x
        self.y = y

class Calculadora:
    def __init__(self):
          self.teclas = {}
    
    def AdicionarTecla(self, nome, x, y):
        self.teclas[nome] = Tecla(x,y)
         

calc = Calculadora()
calc.AdicionarTecla("1", 723, 925)


# Tecla = {}
# Tecla ["1"] = (723, 925)
# Tecla ["2"] = (829, 919)
# Tecla ["3"] = (963, 922)
# Tecla ["4"] = (704, 872)
# Tecla ["5"] = (830, 876)
# Tecla ["6"] = (960, 876)
# Tecla ["7"] = (700, 825)
# Tecla ["8"] = (829, 815)
# Tecla ["9"] = (959, 827)
# Tecla ["0"] = (699, 973)
# Tecla [""] = (699, 780)
# Tecla ["+"] = (1093, 973)
# Tecla ["*"] = (1091, 877)
# Tecla ["-"] = (1088, 922)
# Tecla ["/"] = (1094, 822)
# Tecla ["="] = (1219, 944)

print(Tecla)

