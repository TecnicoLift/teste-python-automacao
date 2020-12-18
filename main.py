from selenium.webdriver import Chrome
from time import sleep
#from selenium.webdriver.common.keys import Keys

url = 'https://sistemalift1.com/lifthomolog/Inicio.aspx'

navegador = Chrome()
navegador.get(url)
sleep(3)

# Inserindo no campo login
inputLogin = navegador.find_element_by_id('txt_login')
inputLogin.send_keys('igor')

# Inserindo no campo senha
inputSenha = navegador.find_element_by_id('txt_senha')
inputSenha.send_keys('abc123')

enter = navegador.find_element_by_id('btn_entrar')
enter.click()

def clientes():
    botao = driver.execute_script("document.getElementsByTagName('a')[0].click()")

def arquitetos():
    botao = navegador.execute_script("document.getElementsByTagName('a')[1].click()")

def produtos():
    botao = navegador.execute_script("document.getElementsByTagName('a')[2].click()")

def fornecedores():
    botao = navegador.execute_script("document.getElementsByTagName('a')[3].click()")

sleep(2)

clientes()
sleep(2)
inicio = navegador.find_element_by_id('ctl00_Topo1_btn_inicio').click()
sleep(2)

arquitetos()
sleep(2)
inicio = navegador.find_element_by_id('ctl00_Topo1_btn_inicio').click()
sleep(2)

produtos()
sleep(2)
inicio = navegador.find_element_by_id('ctl00_Topo1_btn_inicio').click()
sleep(2)

fornecedores()
sleep(2)
inicio = navegador.find_element_by_id('ctl00_Topo1_btn_inicio').click()
sleep(2)