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


    for i in range (0,2):
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
    atualizar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormArquiteto1_btn_cadastrar')
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
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormArquiteto1_txt_nome').clear()
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormArquiteto1_txt_nome')
    inputNome.send_keys('teste arquiteto')

    # clica em atualizar
    atualizar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormArquiteto1_btn_cadastrar')
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

    navegador.execute_script("document.getElementsByTagName('a')[1].click()")

    fornecedor = Select(navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormProdutoADM1_drp_fornecedor'))
    fornecedor.select_by_value("39") # matek

    linha = Select(navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormProdutoADM1_drp_linha'))
    linha.select_by_value("28")  # mesa de jantar

    descricao = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormProdutoADM1_txt_nome')
    descricao.send_keys('teste automacao')

    medida = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormProdutoADM1_txt_medida')
    medida.send_keys('7,00X2,00X0,50')

    precoCusto = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormProdutoADM1_txt_custo').clear()
    precoCusto = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormProdutoADM1_txt_custo')
    precoCusto.send_keys('5,00')

    
    configurarProduto = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormProdutoADM1_btn_cadastrar')
    configurarProduto.click()

    configuracao1 = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_configuracao1')
    configuracao2 = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_configuracao2')
    configuracao3 = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_configuracao3')
    configuracao4 = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_configuracao4')

    configuracao1.send_keys('ACABAMENTO')
    configuracao2.send_keys('TECIDO')
    configuracao3.send_keys('COR')
    configuracao4.send_keys('BASE')

    ok = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    ok.click()

    acabamento = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_acabamento_txt_acabamento')
    acabamento.send_keys('cola branca')
    acrescimo = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_acabamento_txt_acrescimoValorAcabamento').clear()
    acrescimo = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_acabamento_txt_acrescimoValorAcabamento')
    acrescimo.send_keys('1,00')
    aplicar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_acabamento_btn_acabamento')
    aplicar.click()

    tecido = navegador.find_element_by_id('__tab_ctl00_ContentPlaceHolder1_tab_containerTudo_tab_tecido')
    tecido.click()
    tecido = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_tecido_txt_tecido')
    tecido.send_keys('camurça')
    acrescimo = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_tecido_txt_AcrescimoValorTecido').clear()
    acrescimo = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_tecido_txt_AcrescimoValorTecido')
    acrescimo.send_keys('2,00')
    aplicar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_tecido_btn_Tecido')
    aplicar.click()

    cor = navegador.find_element_by_id('__tab_ctl00_ContentPlaceHolder1_tab_containerTudo_tab_cor')
    cor.click()
    cor = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_cor_txt_cor')
    cor.send_keys('cor')
    acrescimo = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_cor_txt_acrescimoPorcentagemCor').clear()
    acrescimo = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_cor_txt_acrescimoPorcentagemCor')
    acrescimo.send_keys('3,00')
    aplicar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_cor_btn_cor')
    aplicar.click()

    base = navegador.find_element_by_id('__tab_ctl00_ContentPlaceHolder1_tab_containerTudo_tab_configuracao4')
    base.click()
    base = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_configuracao4_txt_configuracao4_')
    base.send_keys('MADEIRA SOLIDA')
    acrescimo = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_configuracao4_txt_AcrescimoPorcentagemConfiguracao4').clear()
    acrescimo = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_configuracao4_txt_AcrescimoPorcentagemConfiguracao4')
    acrescimo.send_keys('4,00')
    aplicar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_tab_containerTudo_tab_configuracao4_btn_configuracao4')
    aplicar.click()

    # voltando para o inicio
    inicio()
    navegador.execute_script("document.getElementsByTagName('a')[2].click()")
    barraBusca = Select(navegador.find_element_by_id('ctl00_ContentPlaceHolder1_drp_fornecedor'))
    barraBusca.select_by_value("39")
    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_pesquisar')
    enter.click()

    # excluir produto criado
    navegador.execute_script("document.getElementsByTagName('a')[9].click()")
    excluir = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_tirar')
    excluir.click()

    alert = navegador.switch_to_alert()
    alert.accept()
    #sleep(1)
    alert = navegador.switch_to_alert()
    alert.accept()



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

    navegador.execute_script("document.getElementsByTagName('a')[2].click()") #clica na pessoa

    adcionaProduto = navegador.find_element_by_id('FormOrcamento1_btn_adicionar')
    adcionaProduto.click()


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
    #TECIDO CAMURÇA

    ajusteEstoque = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ajusteEstoque')
    ajusteEstoque.click()

    pesquisaCodigo = Select(navegador.find_element_by_id('ctl00_ContentPlaceHolder1_drp_tipoPesquisa'))
    pesquisaCodigo.select_by_value("1") #descrição

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_pesquisa').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_pesquisa')
    inputBusca.send_keys('POLTRONA RECLINAVEL')

    ok = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_pesquisarPorDesc')
    ok.click()

    valor = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txtQtde')
    valor = valor.get_attribute('value')

    if(valor == '1'):
        quantidade = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_itens_ctl02_txt_quantidade').clear()
        quantidade = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_itens_ctl02_txt_quantidade')
        quantidade.send_keys('2')
    else:
        quantidade = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_itens_ctl02_txt_quantidade').clear()
        quantidade = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_itens_ctl02_txt_quantidade')
        quantidade.send_keys('1')    

    atualizar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_itens_ctl02_LinkButton1')
    atualizar.click()

    alert = navegador.switch_to_alert()
    alert.accept()

    ################################
    pesquisaCodigo = Select(navegador.find_element_by_id('ctl00_ContentPlaceHolder1_drp_tipoPesquisa'))
    pesquisaCodigo.select_by_value("0") #codigo

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_pesquisa').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_pesquisa')
    inputBusca.send_keys('38129117')

    ok = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_pesquisarPorDesc')
    ok.click()

    valor = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txtQtde')
    valor = valor.get_attribute('value')

    if(valor == '1'):
        quantidade = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_itens_ctl02_txt_quantidade').clear()
        quantidade = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_itens_ctl02_txt_quantidade')
        quantidade.send_keys('2')
    else:
        quantidade = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_itens_ctl02_txt_quantidade').clear()
        quantidade = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_itens_ctl02_txt_quantidade')
        quantidade.send_keys('1')    

    atualizar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_itens_ctl02_LinkButton1')
    atualizar.click()

    alert = navegador.switch_to_alert()
    alert.accept()


def entrega():
    navegador.execute_script("document.getElementsByTagName('a')[11].click()")

def funcionarios():
    navegador.execute_script("document.getElementsByTagName('a')[12].click()")

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('teste funcionario')


    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()


    # clica na pessoa
    pessoa = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_funcionario_ctl02_lbl_nome')
    pessoa.click()


    # clica para editar
    editar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_editar')
    editar.click()


    # coloca novo nome
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormFuncionario1_txt_nome').clear()

    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormFuncionario1_txt_nome')
    inputNome.send_keys('teste funcionario mudado')


    # clica em atualizar
    atualizar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormFuncionario1_btn_cadastrar')
    atualizar.click()


    ###################
    # busca com novo nome
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('teste funcionario mudado')


    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()

    # clica na pessoa
    pessoa = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_grid_funcionario_ctl02_lbl_nome')
    pessoa.click()

    # clica em editar
    editar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_editar')
    editar.click()

    # coloca o antigo nome
    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormFuncionario1_txt_nome').clear()

    inputNome = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormFuncionario1_txt_nome')
    inputNome.send_keys('teste funcionario')

    # clica em atualizar
    atualizar = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_FormFuncionario1_btn_cadastrar')
    atualizar.click()

    alert = navegador.switch_to_alert()
    alert.accept()

    sleep(1)

    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar').clear()
    inputBusca = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_txt_buscar')
    inputBusca.send_keys('teste funcionario')
    
    enter = navegador.find_element_by_id('ctl00_ContentPlaceHolder1_btn_ok')
    enter.click()

def usuarios():
    navegador.execute_script("document.getElementsByTagName('a')[13].click()")

def financeiro():
    navegador.execute_script("document.getElementsByTagName('a')[14].click()")

    navegador.execute_script("document.getElementsByTagName('a')[9].click()") # integração

def marketing():
    navegador.execute_script("document.getElementsByTagName('a')[15].click()")

def relatorio():
    navegador.execute_script("document.getElementsByTagName('a')[16].click()")

def configuracao():
    navegador.execute_script("document.getElementsByTagName('a')[17].click()")


####################################
def inicio():
    sleep(2)
    navegador.find_element_by_id('ctl00_Topo1_btn_inicio').click()
    sleep(2)
####################################

sleep(2)

clientes()  #ok
inicio()

arquitetos()  #ok 
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
inicio()

representantes() # ok
inicio()

assistencia()
inicio()

estoque()  # ok
inicio()

entrega()
inicio()

funcionarios()  # ok
inicio()

usuarios()
inicio()

financeiro()
inicio()

marketing()
inicio()

relatorio()
inicio()

configuracao()
inicio()