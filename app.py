from flask import *
from dados import *
from datetime import datetime
import time
import os

dadosPessoa = {}
dadosEmpresa = {}

totalEmissao = []
totalReducao = []

def tratar_entrada(valor, tipo, valor_padrao):
    if valor.strip() == "":
        return int(valor_padrao)
        
    try:
        if tipo == 'float':
            return float(valor)
        elif tipo == 'int':
            return int(valor)
            
    except ValueError:
        return int(valor_padrao)
 

def salvar_dados(tipoCalculo, Remissao, Rcredito, Rreducao):
    pasta = "Resultados"
    os.makedirs(pasta, exist_ok=True)
    if tipoCalculo == 1:
        nome = dadosPessoa["nome"]
    else:
        nome = dadosEmpresa["nome"]
    data = dadosPessoa["data"] 
    nome_arquivo = (f"{nome}_{data}.txt") 
    caminho = os.path.join(pasta, nome_arquivo)
    with open(caminho, 'w') as arquivo:
        arquivo.write(f"Dados\n")
        if tipoCalculo == 1:
            arquivo.write(f"Nome: {dadosPessoa['nome']}\n") 
            arquivo.write(f"Endereço: {dadosPessoa['endereco']}\n") 
            arquivo.write(f"telefone: {dadosPessoa['telefone']}\n")
            arquivo.write(f"Ano Inventariado: {dadosPessoa['anoInventariado']}\n")
            arquivo.write("\n")
        else:
            arquivo.write(f"Empresa: {dadosEmpresa['nome']}\n")
            arquivo.write(f"Endereço: {dadosEmpresa['endereco']}\n")
            arquivo.write(f"Nome do responsável: {dadosEmpresa['nomeResponsavel']}\n")
            arquivo.write(f"Telefone do Responsável: {dadosEmpresa['telefoneResponsavel']}\n")
            arquivo.write(f"Ano Inventariado: {dadosEmpresa['anoInventariado']}\n")
            arquivo.write(f"Ramo Empresa: {dadosEmpresa['ramoEmpresa']}\n")
            arquivo.write("\n")
                          
        arquivo.write(f'Total de emissão {Remissao}\n')
        arquivo.write(f'Total de redução {Rreducao}\n')
        arquivo.write(f'Total de credito {Rcredito}\n')
        arquivo.write("\n")
        arquivo.write(f'Data: {dadosPessoa['data']}') 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/empresa')
def empresa_index():
    return render_template('/empresa/index.html')
@app.route('/pessoa')
def pessoa_index():
    return render_template('/pessoa/index.html')

@app.route('/calculo', methods=['POST'])
def empresa():

    tipoCalculo = int(request.form['tipo'])
    print(tipoCalculo) #teste
    if tipoCalculo == 1:
        print('Cadastrando pessoa')
        dadosPessoa['nome'] = request.form['nome']
        dadosPessoa['endereco'] = request.form['endereco']
        dadosPessoa['telefone'] = request.form['telefone']
        anoInventario = int(request.form['ano_inventariado'])
        dadosPessoa['data'] = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        if anoInventario == 0:
            dadosPessoa['anoInventariado'] = 'Ano não selecionado'
        else:
            dadosPessoa['anoInventariado'] = anoInventario
        print()
    else:
        # cadastro empresa
        print('Cadastrando empresa')
        dadosEmpresa['nome'] = request.form['nome_empresa'] # Entrada do nome da empresa via formulário
        dadosEmpresa['endereco'] = request.form["endereco_empresa"] # Entrada do endereço da empresa via formulário
        dadosEmpresa['nomeResponsavel'] = request.form['nomeResponsavel_empresa'] # Entrada do nome do responsável pela empresa via formulário
        dadosEmpresa['telefoneResponsavel'] = request.form['telefoneResponsavel_empresa'] # Entrada do telefone do responsável pela empresa via formulário
        anoInventario = int(request.form['ano_inventariado'])
        if anoInventario == 0:
            dadosEmpresa['anoInventariado'] = 'Ano não selecionado'
        else:
            dadosEmpresa['anoInventariado'] = anoInventario
        ramoEmpresa = int(request.form['ramo_empresa'])
        if ramoEmpresa == 0:
            dadosEmpresa['ramoEmpresa'] = 'Ramo não selecionado'
        elif ramoEmpresa == 1:
            dadosEmpresa['ramoEmpresa'] = 'Agro'
        elif ramoEmpresa == 2:
            dadosEmpresa['ramoEmpresa'] = 'Industrial'
        else:
            dadosEmpresa['ramoEmpresa'] = 'Outros'

    print('Puxando dados do formulário. Aguarde....')
    # Entrada combustivel via formulário
    gasolina = tratar_entrada(request.form.get('gasolina'), 'float', 0.0)  # Consumo médio de gasolina
    qtGasolina = tratar_entrada(request.form.get('qtGasolina'), 'int', 1)  # Quantidade de veículos a gasolina
    etanol = tratar_entrada(request.form.get('etanol'), 'float', 0.0)  # Consumo médio de etanol
    qtEtanol = tratar_entrada(request.form.get('qtEtanol'), 'int', 1)  # Quantidade de veículos a etanol
    diesel = tratar_entrada(request.form.get('diesel'), 'float', 0.0)  # Consumo médio de diesel
    qtDiesel = tratar_entrada(request.form.get('qtDiesel'), 'int', 1)  # Quantidade de veículos a diesel
    biodiesel = tratar_entrada(request.form.get('biodiesel'), 'float', 0.0)  # Consumo médio de biodiesel
    qtBiodiesel = tratar_entrada(request.form.get('qtBiodiesel'), 'int', 1)  # Quantidade de veículos a biodiesel

    if tipoCalculo == 2:
        # Entrada produção via formulário
        ramo_empresa = request.form['ramo_empresa']
        prodAco = tratar_entrada(request.form.get('ProdAco'), 'float', 0.0)  # Produção de aço
        prodCimento = tratar_entrada(request.form.get('ProdCimento'), 'float', 0.0)  # Produção de cimento
        prodPapel = tratar_entrada(request.form.get('ProdPapel'), 'float', 0.0)  # Produção de papel
        prodVidro = tratar_entrada(request.form.get('ProdVidro', ''), 'float', 0.0)  # Produção de vidro
        prodAluminio = tratar_entrada(request.form.get('ProdAluminio', ''), 'float', 0.0)  # Produção de alumínio
        prodEtanol = tratar_entrada(request.form.get('ProdEtanol', ''), 'float', 0.0)  # Produção de etanol
        prodAmonia = tratar_entrada(request.form.get('ProdAmonia', ''), 'float', 0.0)  # Produção de amônia
        prodEletricidade_Carvao = tratar_entrada(request.form.get('ProdEletricidade_Carvao', ''), 'float',0.0)  # Produção de eletricidade a carvão
        prodEletricidade_GasNat = tratar_entrada(request.form.get('ProdEletricidade_GasNat', ''), 'float',0.0)  # Produção de eletricidade a gás natural
        prodEletricidade_Petroleo = tratar_entrada(request.form.get('ProdEletricidade_Petroleo', ''), 'float',0.0)  # Produção de eletricidade a petróleo

        # Entrada Atividade agrícola
        solo_mineral = tratar_entrada(request.form.get('solo_mineral', ''), 'float', 0.0)
        desmatamento = tratar_entrada(request.form.get('desmatamento', ''), 'float', 0.0)
        cult_solo = tratar_entrada(request.form.get('cult_solo', ''), 'float', 0.0)

    #entrada ar condicionado via terminal
    arP = tratar_entrada(request.form.get('arP', ''), 'float', 0.0)  # entrada do uso do ar condicionado em hr/dia
    qtarP = tratar_entrada(request.form.get('qtarP', ''), 'int', 1)  # quantidade de ar condicionado
    arM = tratar_entrada(request.form.get('arM', ''), 'float', 0.0)  # entrada do uso do ar condicionado em hr/dia
    qtarM = tratar_entrada(request.form.get('qtarM', ''), 'int', 1)  # quantidade de ar condicionado
    arG = tratar_entrada(request.form.get('arG', ''), 'float', 0.0)  # entrada do uso do ar condicionado em hr/dia
    qtarG = tratar_entrada(request.form.get('qtarG', ''), 'int', 1)  # quantidade de ar condicionado
    arI = tratar_entrada(request.form.get('arI', ''), 'float', 0.0)  # entrada do uso do ar condicionado em hr/dia
    qtarI = tratar_entrada(request.form.get('qtarI', ''), 'int', 1)  # quantidade de ar condicionado

    #entrada de resíduos
    solidos = tratar_entrada(request.form.get('RsSolidos', ''), 'float', 0.0)
    organicos = tratar_entrada(request.form.get('RsOrganicos', ''), 'float', 0.0)
    industriais = tratar_entrada(request.form.get('RsIndustriais', ''), 'float', 0.0)
    eletronicos = tratar_entrada(request.form.get('RsEletronicos', ''), 'float', 0.0)

    #entrada de efluentes
    EfIndustriais = tratar_entrada(request.form.get('EfIndustriais', ''), 'float', 0.0)
    domesticos = tratar_entrada(request.form.get('EfDomestico', ''), 'float', 0.0)
    agricolas = tratar_entrada(request.form.get('EfAgricola', ''), 'float', 0.0)

    #entrada consumo de energia eletrica
    carvao = tratar_entrada(request.form.get('enCarvao', ''), 'float', 0.0)
    gasNat = tratar_entrada(request.form.get('enGasnatural', ''), 'float', 0.0)
    petroleo = tratar_entrada(request.form.get('enPetroleo', ''), 'float', 0.0)
    nuclear = tratar_entrada(request.form.get('enNuclear', ''), 'float', 0.0)
    renovavel = tratar_entrada(request.form.get('enRenovavel', ''), 'float', 0.0)
    tpFornecimento = int(request.form['tpFornecimento'])
    print('Processo concluido')

    #Eficiencia energetica
    equipamento = tratar_entrada(request.form.get('equipamento', ''), 'float', 0.0)
    iluminacao = tratar_entrada(request.form.get('iluminacao', ''), 'float', 0.0)
    #fontes renovaveis
    Psolar = tratar_entrada(request.form.get('Psolar', ''), 'float', 0.0)
    Hsolar = tratar_entrada(request.form.get('Hsolar', ''), 'float', 0.0)
    Peolica = tratar_entrada(request.form.get('Peolica', ''), 'float', 0.0)
    Ceolica = tratar_entrada(request.form.get('Ceolica', ''), 'float', 0.0)
    Heolica = tratar_entrada(request.form.get('Heolica', ''), 'float', 0.0)
    Csolar = tratar_entrada(request.form.get('Csolar', ''), 'float', 0.0)
    EaqSolar = tratar_entrada(request.form.get('Esolar', ''), 'float', 0.0)
    #transporte sustentavel
    CarEletrico = tratar_entrada(request.form.get('CarEletrico', ''), 'float', 0.0)
    TpPublico = tratar_entrada(request.form.get('TpPublico', ''), 'float', 0.0)
    Caminhada = tratar_entrada(request.form.get('Caminha', ''), 'float', 0.0)
    #redução de residuos
    ReciclagemPapel = tratar_entrada(request.form.get('ReciclagemPapel', ''), 'float', 0.0)
    Comp = tratar_entrada(request.form.get('Comp', ''), 'float', 0.0)
    Plast = tratar_entrada(request.form.get('Plast', ''), 'float', 0.0)
    Agricultura = tratar_entrada(request.form.get('Agricultura', ''), 'float', 0.0)
    Carne = tratar_entrada(request.form.get('Carne', ''), 'float', 0.0)
    Reflorestamento = tratar_entrada(request.form.get('Reflorestamento', ''), 'float', 0.0)

    #Processamento dos dados
    #cálculo combustível
    print('Calculando emissão por queima de combustível')
    totalEmissao.append(((((gasolina * qtGasolina) * 12) * comb['gasolina'])/1000)) # calculo de emissão por queima de gasolina em t/ano
    totalEmissao.append(((((etanol * qtEtanol) * 12) * comb['etanol'])/1000)) # calculo de emissão por queima de etanol em t/ano
    totalEmissao.append(((((diesel * qtDiesel) * 12) * comb['diesel'])/1000)) # calculo de emissão por queima de diesel em t/ano
    totalEmissao.append(((((biodiesel * qtBiodiesel) * 12) * comb['biodiesel'])/1000)) # calculo de emissão por queima de biodiesel em t/ano
    print('Concluido')

    if tipoCalculo == 2:
        # cálculo produção
        if ramoEmpresa == 2:
            print('Calculando emissão por tipo de produção')
            totalEmissao.append(((((prodAco * 30)*12) * prodIndustrial['prodAco'])/1000)) # Calculo de produção de aço em t/ano
            totalEmissao.append(((((prodCimento * 30)*12) * prodIndustrial['prodCimento'])/1000)) # Calculo de produção de cimento em t/ano
            totalEmissao.append(((((prodPapel * 30)*12) * prodIndustrial['prodPapel'])/1000)) # Calculo de produção de papel em t/ano
            totalEmissao.append(((((prodVidro * 30)*12) * prodIndustrial['prodVidro'])/1000)) # Calculo de produção de vidro em t/ano
            totalEmissao.append(((((prodAluminio * 30)*12) * prodIndustrial['prodAluminio'])/1000)) # Calculo de produção de alumínio em t/ano
            totalEmissao.append(((((prodAmonia * 30)*12) * prodIndustrial['prodAmonia'])/1000)) # Calculo de produção de amônia em t/ano
            totalEmissao.append(((((prodEtanol * 30)*12) * prodIndustrial['prodEtanol'])/1000)) # Calculo de produção de etanol em t/ano
            totalEmissao.append(((((prodEletricidade_Carvao * 30)*12) * prodIndustrial['prodEletricidade_Carvao'])/1000)) # Calculo de produção de eletricidade por queima de carvão em t/ano
            totalEmissao.append(((((prodEletricidade_GasNat * 30)*12) * prodIndustrial['prodEletricidade_GasNat'])/1000)) # Calculo de produção de eletricidade por queima de gás natural em t/ano
            totalEmissao.append(((((prodEletricidade_Petroleo * 30)*12) * prodIndustrial['prodEletricidade_Petroleo'])/1000)) # Calculo de produção de eletricidade por queima de petrólio em t/ano
            print('concluido')
        elif ramoEmpresa == 2:
            # cálculo Atividade Agricola
            print('Calculando emissão por mudança no solo')
            totalEmissao.append((((solo_mineral * 30) * 12) * atAgricola['solo_mineral']) / 1000)
            totalEmissao.append((((desmatamento * 30) * 12) * atAgricola['desmatamento']) / 1000)
            totalEmissao.append((((cult_solo * 30) * 12) * atAgricola['cult_solo']) / 1000)
            print('concluido')

    # cálculo Ar Condicionado
    print('Calculando emissão por uso de Ar condicionado')
    totalEmissao.append((((((qtarP * arP) * 30) * 12) * arCond['arPequeno']) / 1000)) # Calculo de emissão para ar cond.pequeno em t/ano
    totalEmissao.append((((((qtarM * arM) * 30) * 12) * arCond['arMedio']) / 1000)) # Calculo de emissão para ar cond.pequeno em t/ano
    totalEmissao.append((((((qtarG * arG) * 30) * 12) * arCond['arGrande']) / 1000)) # Calculo de emissão para ar cond.grande em t/ano
    totalEmissao.append((((((qtarI * arI) * 30) * 12) * arCond['arIndustrial']) / 1000)) # Calculo de emissão para ar cond.industrial em t/ano
    print('Concluido')


    # calculo resíduos
    print('Calculando emissão por resíduos')
    totalEmissao.append((((solidos * 30) * 12) * residuos['solidos']) / 1000)
    totalEmissao.append((((organicos * 30) * 12) * residuos['organicos']) / 1000)
    totalEmissao.append((((industriais * 30) * 12) * residuos['industriais']) / 1000)
    totalEmissao.append((((eletronicos * 30) * 12) * residuos['eletronicos']) / 1000)
    print('Concluido')

    # calculo efluentes
    print('Calculando emissão por Efluentes')
    totalEmissao.append((((EfIndustriais * 30) * 12) * efluentes['industriais']) / 1000)
    totalEmissao.append((((domesticos * 30) * 12) * efluentes['domesticos']) / 1000)
    totalEmissao.append((((agricolas * 30) * 12) * efluentes['agricolas']) / 1000)
    print('Concluido')

    # Calculo consumo energetico
    print('Calculando emissão por consumo de energia eletrica')
    if tpFornecimento == 1:
        totalEmissao.append(((carvao * 12) * energia['carvao']) / 1000)
        print('Calculando: Carvão')
    elif tpFornecimento == 2:
        totalEmissao.append(((gasNat * 12) * energia['gasNat']) / 1000)
        print('Calculando: Gás Natural')
    elif tpFornecimento == 3:
        totalEmissao.append(((petroleo * 12) * energia['petroleo']) / 1000)
        print('Calculando: Petróleo')
    elif tpFornecimento == 4:
        totalEmissao.append(((nuclear * 12) * energia['nuclear']) / 1000)
        print('Calculando: Nuclear')
    elif tpFornecimento == 5:
        totalEmissao.append(((renovavel * 12) * energia['renovavel']) / 1000)
        print('Calculando: Renovavel')

    #calculo da redeução
    totalReducao.append((equipamento * reducao['equipamento']) / 1000)
    totalReducao.append((iluminacao * reducao['iluminacao']) / 1000)
    Esolar = Psolar * Hsolar
    totalReducao.append((((Esolar * 30) * 12) * reducao['solar']) / 1000)
    Eeolica = Peolica * (Ceolica/100) * Heolica
    totalReducao.append((((Eeolica * 30) * 12 ) * reducao['eolica']) / 1000)
    Eaqsolar = (Csolar) * (EaqSolar/100)
    totalReducao.append((Eaqsolar * reducao['AqSolar']) * 12 / 1000)
    totalReducao.append((CarEletrico * reducao['CarEletrico']) / 1000)
    totalReducao.append((TpPublico * reducao['TpPublico']) / 1000)
    totalReducao.append((Caminhada * reducao['Caminhada']) / 1000)
    totalReducao.append((ReciclagemPapel * reducao['ReciclagemPapel']) / 1000)
    totalReducao.append((Comp * reducao['Comp']) / 1000)
    totalReducao.append((Plast * reducao['Plast']) / 1000)
    totalReducao.append((Agricultura * reducao['Agricultura']) / 1000)
    totalReducao.append((Carne * reducao['Carne']) / 1000)
    totalReducao.append((Reflorestamento * reducao['Reflorestamento']) / 1000)

    #retorno
    print('Salvando dados aguarde...')
    Remissao = (f'{sum(totalEmissao):.2f}')
    Rcredito = (f'{sum(totalReducao):.2f}')
    Rreducao = (f'{sum(totalEmissao) - sum(totalReducao):.2f}')
    salvar_dados(tipoCalculo, Remissao, Rcredito, Rreducao)
    if tipoCalculo == 1:
        return render_template('/pessoa/result/index.html',
                               nome=dadosPessoa['nome'],
                               endereco_empresa=dadosPessoa['endereco'],
                               telefone=dadosPessoa['telefone'],
                               ano_inventariado=dadosPessoa['anoInventariado'],
                               Remissao=Remissao, Reducao=Rreducao, Rcredito=Rcredito)

    elif tipoCalculo == 2:
        return render_template('/empresa/result/index.html',
                               nome_empresa=dadosEmpresa['nome'],
                               endereco_empresa=dadosEmpresa['endereco'],
                               nomeResponsavel_empresa=dadosEmpresa['nomeResponsavel'],
                               telefoneResponsavel_empresa=dadosEmpresa['telefoneResponsavel'],
                               ano_inventariado=dadosEmpresa['anoInventariado'],
                               ramo_empresa=dadosEmpresa['ramoEmpresa'],
                               Remissao=Remissao, Reducao=(f'{Rreducao:.2f}'), Rcredito=Rcredito)

if __name__ == '__main__':
    app.run(debug=True)


