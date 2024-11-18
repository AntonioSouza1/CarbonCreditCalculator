# CarbonCreditCalculator
Documentação da Calculadora de Emissões e Reduções
Introdução
A Calculadora de Emissões e Reduções é uma aplicação web desenvolvida em Flask que permite a usuários, tanto pessoas físicas quanto jurídicas, calcular suas emissões de gases de efeito estufa e as reduções que podem ser alcançadas através de práticas sustentáveis. A aplicação coleta dados sobre consumo de combustíveis, produção industrial, uso de ar condicionado, resíduos, e outros fatores que impactam as emissões.
Requisitos
•	Python 3.x
•	Flask
•	Bibliotecas necessárias (instaláveis via pip)
Como Usar
1. Instalação
Para instalar a aplicação, você precisa ter o Python e o Flask instalados. Execute os seguintes comandos:
bash
VerifyOpen In EditorEditCopy code
1pip install Flask
2. Executando a Aplicação
Para iniciar a aplicação, navegue até o diretório onde o app.py está localizado e execute:
bash
VerifyOpen In EditorEditCopy code
1python app.py
A aplicação estará disponível em http://127.0.0.1:5000/.
3. Navegação
•	Página Inicial: Acesse a página inicial para escolher entre calcular as emissões como pessoa ou empresa.
•	Cadastro: Preencha os formulários com as informações necessárias. Dependendo da escolha, você será direcionado para a página de cadastro de pessoa ou empresa.
•	Cálculo: Após inserir os dados, clique no botão para calcular. O aplicativo processará as informações e apresentará os resultados de emissões, reduções e créditos.
•	Resultados: Os resultados serão apresentados em uma nova página, e também serão salvos em um arquivo de texto na pasta Resultados/.
4. Estrutura dos Dados
Os dados necessários para o cálculo incluem, mas não se limitam a:
•	Para Pessoas:
•	Nome
•	Endereço
•	Telefone
•	Ano inventariado
•	Consumo de combustíveis (gasolina, etanol, diesel, biodiesel)
•	Uso de ar condicionado
•	Resíduos gerados
•	Efluentes
•	Para Empresas:
•	Nome da empresa
•	Endereço
•	Nome do responsável
•	Telefone do responsável
•	Ano inventariado
•	Ramo da empresa
•	Produção de diversos produtos (aço, cimento, papel, etc.)
•	Consumo de energia elétrica
5. Resultados
Os resultados incluem:
•	Total de emissões calculadas
•	Total de reduções alcançadas
•	Total de créditos obtidos
Os resultados são salvos em um arquivo de texto que inclui todas as informações inseridas e os cálculos realizados.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório.
Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.
