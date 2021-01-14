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
    navegador.execute_script("document.getElementsByTagName('a')[0].click()") #entra em clientes
    sleep(1)

    '''navegador.execute_script("document.getElementsByTagName('a')[1].click()") # clica em novo

    
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_txt_nome')
    inputNome.send_keys('teste automação')

    inputEmail = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_txt_email')
    inputEmail.send_keys('123@EMAIL.COM')

    inputCelular = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_txt_celular')
    inputCelular.send_keys('(43) 99999-9999')

    cadastrar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_btn_cadastrar')
    cadastrar.click()'''

    # busca cliente
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('teste automação')


    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()


    # clica na pessoa
    pessoa = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_cliente_ctl02_lbl_nome')
    pessoa.click()


    # clica para editar
    editar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_editar')
    editar.click()


    # coloca novo nome
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_txt_nome').clear()

    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_txt_nome')
    inputNome.send_keys('teste automação mudado')


    # clica em atualizar
    atualizar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_btn_cadastrar')
    atualizar.click()


    ###################
    # busca com novo nome
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('teste automação mudado')


    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()

    # clica na pessoa
    pessoa = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_cliente_ctl02_lbl_nome')
    pessoa.click()

    # clica em editar
    editar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_editar')
    editar.click()

    # coloca o antigo nome
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_txt_nome').clear()

    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_txt_nome')
    inputNome.send_keys('teste automação')

    # clica em atualizar
    atualizar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_btn_cadastrar')
    atualizar.click()

    alert = navegador.switch_to_alert()
    alert.accept()

    sleep(1)

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('teste automação')
    
    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()
    


def arquitetos():
    navegador.execute_script("document.getElementsByTagName('a')[1].click()")

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('teste arquiteto')


    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()


    # clica na pessoa
    pessoa = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_arquitetos_ctl02_lbl_nome')
    pessoa.click()


    # clica para editar
    editar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_editar')  # erro ao clicar aki
    editar.click()


    # coloca novo nome
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormArquiteto1_txt_nome').clear()
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormArquiteto1_txt_nome')
    inputNome.send_keys('teste arquiteto mudado')


    # clica em atualizar
    atualizar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_btn_cadastrar')
    atualizar.click()


    ###################
    # busca com novo nome
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('teste arquiteto mudado')


    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()

    # clica na pessoa
    pessoa = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_arquitetos_ctl02_lbl_nome')
    pessoa.click()

    # clica em editar
    editar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_editar')
    editar.click()

    # coloca o antigo nome
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_txt_nome').clear()
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_txt_nome')
    inputNome.send_keys('teste arquiteto')

    # clica em atualizar
    atualizar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormCliente1_btn_cadastrar')
    atualizar.click()

    alert = navegador.switch_to_alert()
    alert.accept()

    sleep(1)

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('teste arquiteto')
    
    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()

def produtos():
    navegador.execute_script("document.getElementsByTagName('a')[2].click()")

    barraBusca = Select(navegador.find_element_by_id('ctl00_ContentPlaceHolder1_drp_fornecedor'))
    barraBusca.select_by_value("39")

    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_pesquisar')
    enter.click()

def fornecedores():
    navegador.execute_script("document.getElementsByTagName('a')[3].click()")

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('FOUR')

    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()

    pessoa = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_fornecedores_ctl02_lbl_nome')
    pessoa.click()


def orcamentos():
    navegador.execute_script("document.getElementsByTagName('a')[4].click()")

    novo = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_novo')
    novo.click()

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_nome')
    inputBusca.send_keys('igorr')

    ok = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    ok.click()

    #continuar
    
def pedidos():
    navegador.execute_script("document.getElementsByTagName('a')[5].click()")

    novo = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_novo')
    novo.click()

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_nome')
    inputBusca.send_keys('igorr')

    ok = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    ok.click()

    #continuar

def emissaoOc():
    navegador.execute_script("document.getElementsByTagName('a')[6].click()")

    ocEstoque = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_emitirEstoque')
    ocEstoque.click()

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_nome')
    inputBusca.send_keys('matek')

    ok = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    ok.click()

    #continuar

def recebimetoOc():
    navegador.execute_script("document.getElementsByTagName('a')[7].click()")

def representantes():
    navegador.execute_script("document.getElementsByTagName('a')[8].click()")

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('teste representante')


    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()


    # clica na pessoa
    pessoa = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_representantes_ctl02_lbl_nome')
    pessoa.click()


    # clica para editar
    editar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_editar')
    editar.click()


    # coloca novo nome
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormRepresentante1_txt_nome').clear()
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormRepresentante1_txt_nome')
    inputNome.send_keys('teste representante mudado')


    # clica em atualizar
    atualizar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormRepresentante1_btn_cadastrar')
    atualizar.click()


    ###################
    # busca com novo nome
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('teste representante mudado')


    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()

    # clica na pessoa
    pessoa = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_representantes_ctl02_lbl_nome')
    pessoa.click()

    # clica em editar
    editar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_editar')
    editar.click()

    # coloca o antigo nome
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormRepresentante1_txt_nome').clear()
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormRepresentante1_txt_nome')
    inputNome.send_keys('teste representante')

    # clica em atualizar
    atualizar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormRepresentante1_btn_cadastrar')
    atualizar.click()

    alert = navegador.switch_to_alert()
    alert.accept()

    sleep(1)

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('teste representante')
    
    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()

def assistencia():
    navegador.execute_script("document.getElementsByTagName('a')[9].click()")

def estoque():
    navegador.execute_script("document.getElementsByTagName('a')[10].click()")

def entrega():
    navegador.execute_script("document.getElementsByTagName('a')[11].click()")

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
inicio()

fornecedores()
inicio()

orcamentos()
inicio()

pedidos()
inicio()

emissaoOc()
inicio()

recebimetoOc()
inicio()'''

representantes()
inicio()

'''assistencia()
inicio()

estoque()
inicio()

entrega()
inicio()'''