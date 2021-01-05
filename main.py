from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.ui import Select

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

#clicando em enter
enter = navegador.find_element_by_id('btn_entrar')
enter.click()




def clientes():
    navegador.execute_script("document.getElementsByTagName('a')[0].click()")

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('igorr')

    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()

    pessoa = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_cliente_ctl02_lbl_nome')
    pessoa.click()

def arquitetos():
    navegador.execute_script("document.getElementsByTagName('a')[1].click()")

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('mari')

    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()

    pessoa = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_arquitetos_ctl02_lbl_nome')
    pessoa.click()

def produtos():
    navegador.execute_script("document.getElementsByTagName('a')[2].click()")

    barraBusca = Select(navegador.find_element_by_id('ctl00_ContentPlaceHolder1_drp_fornecedor'))
    barraBusca.select_by_value("39")

    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_pesquisar')
    enter.click()

def fornecedores():
    botao = navegador.execute_script("document.getElementsByTagName('a')[3].click()")

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('FOUR')

    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()

    pessoa = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_fornecedores_ctl02_lbl_nome')
    pessoa.click()


def orcamentos():
    botao = navegador.execute_script("document.getElementsByTagName('a')[4].click()")

def pedidos():
    botao = navegador.execute_script("document.getElementsByTagName('a')[5].click()")

def emissaoOc():
    botao = navegador.execute_script("document.getElementsByTagName('a')[6].click()")

def recebimetoOc():
    botao = navegador.execute_script("document.getElementsByTagName('a')[7].click()")

def representantes():
    botao = navegador.execute_script("document.getElementsByTagName('a')[8].click()")

def assistencia():
    botao = navegador.execute_script("document.getElementsByTagName('a')[9].click()")

def estoque():
    botao = navegador.execute_script("document.getElementsByTagName('a')[10].click()")

def entrega():
    botao = navegador.execute_script("document.getElementsByTagName('a')[11].click()")

####################################
def inicio():
    sleep(2)
    inicio = navegador.find_element_by_id('ctl00_Topo1_btn_inicio').click()
    sleep(2)
####################################

sleep(2)

'''clientes()
inicio()

arquitetos()
inicio()

produtos()
inicio()'''

fornecedores()
inicio()

'''orcamentos()
inicio()

pedidos()
inicio()

emissaoOc()
inicio()

recebimetoOc()
inicio()

representantes()
inicio()

assistencia()
inicio()

estoque()
inicio()

entrega()
inicio()'''
