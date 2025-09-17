import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

time.sleep(15)

# Entrar no link de registro dos dados
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(20)

# Login no sistema
pyautogui.click(x=670, y=461)
pyautogui.write("dias@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=1000, y=664)

time.sleep(5)

# importar a base de dados
table = pd.read_csv('produtos.csv')

# Cadastrar dos produtos
for row in table.index:

    pyautogui.click(x=686, y=316)
    # Pegar na tabela o valor do campo usando .loc acessando pelos rótulos
    pyautogui.write(str(table.loc[row, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[row, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[row, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[row, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[row, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[row, "custo"]))
    pyautogui.press("tab")
    obs = table.loc[row, "obs"]

    if not pd.isna(obs):
        pyautogui.write(str(table.loc[row, "obs"]))
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)




