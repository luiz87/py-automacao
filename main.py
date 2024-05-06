import pyautogui
import time
import random

def calhora(minutos):
    h = minutos//60
    m = minutos%60
    return f"{h:02}{m:02}"

lsNum = ["24","26","29","30"]
i = 0
proximo = input("Next?")
while i < len(lsNum): #(proximo != "x"):
    try:
        
        entrada = random.randint(0,20)+(480-10)
        hm1 = calhora(entrada)
        saida = random.randint(0,20)+(720-10)
        hm2 = calhora(saida)
        entrada = (480-entrada)+810
        hm3 = calhora(entrada)
        saida = (720-saida)+1050
        hm4 = calhora(saida)

        img = pyautogui.locateCenterOnScreen(lsNum[i]+".png")
        pyautogui.click(img.x, img.y)

        time.sleep(2)
        pyautogui.typewrite(hm1)
        pyautogui.press("tab")
        pyautogui.typewrite(hm2)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.typewrite(hm3)
        pyautogui.press("tab")
        pyautogui.typewrite(hm4)

        img = pyautogui.locateCenterOnScreen('bt-salvar.png')
        pyautogui.click(img.x, img.y)
        i += 1
    except:
        try:
            img = pyautogui.locateCenterOnScreen('bt-down.png')
            pyautogui.click(img.x, img.y)
        except:
            print("erros")

    #proximo = input("Next?")