# Base de dados "Fator de conversão"
comb = {
    'etanol': 1.94,  # CO2/litro
    'gasolina': 2.31,  # CO2/litro
    'diesel': 2.68,  # CO2/litro
    'biodiesel': 2.46,  # CO2/litro
    'glp': 2.50  # CO2/litro
}
arCond = {
    'arPequeno': 0.5,  # kg por hora
    'arMedio': 1.5,  # kg por hora
    'arGrande': 3,  # kg por hora
    'arIndustrial': 4  # kg por hora
}

prodIndustrial = {
    'prodAco': 1.8,  # kg de co2 por kg produzido
    'prodCimento': 0.9,  # kg de co2 por kg produzido
    'prodPapel': 0.5,  # kg de co2 por kg produzido
    'prodVidro': 0.6,  # kg de co2 por kg produzido
    'prodAluminio': 12,  # kg de co2 por kg produzido
    'prodAmonia': 1.8,  # kg de co2 por kg produzido
    'prodEtanol': 1.6,  # kg de co2 por kg produzido
    'prodEletricidade_Carvao': 0.9,  # kg de co2 por kg produzido
    'prodEletricidade_GasNat': 0.4,  # kg de co2 por kg produzido
    'prodEletricidade_Petroleo': 0.7  # kg de co2 por kg produzido
}

atAgricola = {
    'solo_mineral': 44, #Kg de CO2 por m2
    'desmatamento': 110, #Kg de CO2 por m2
    'cult_solo': 108 #Kg de CO2 por m2
}

residuos = {
    'solidos': 0.5, # kg de co2 por kg de resíduos
    'organicos': 0.25, # kg de co2 por kg de resíduos
    'industriais': 1.5, # kg de co2 por kg de resíduos
    'eletronicos': 2 # kg de co2 por kg de resíduos
}

efluentes = {
    'industriais': 0.5, # kg de co2 por kg efluentes tratados
    'domesticos': 0.3, # kg de co2 por kg efluentes tratados
    'agricolas': 0.2 # kg de co2 por kg efluentes tratados
}

energia = {
    'carvao': 0.9,
    'gasNat': 0.4,
    'petroleo': 0.6,
    'nuclear': 0.010,
    'renovavel': 0.005
}
reducao = {
    'equipamento': 1.500,
    'iluminacao': 100,
    'solar': 0.5, #kg de co2/kw
    'eolica': 0.5, #kg de co2/kw
    'AqSolar': 0.5, #kg de co2/kw
    'CarEletrico': 2.500,
    'TpPublico': 1.250,
    'Caminhada': 1.000,
    'ReciclagemPapel': 1.200,
    'Comp': 0.500,
    'Plast': 0.500,
    'Agricultura': 1.500,
    'Carne':2.500,
    'Reflorestamento': 7.500,
}