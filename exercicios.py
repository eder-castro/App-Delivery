#---------- Usando lista de dicionarios

#pessoas = [
#           {'nome': 'Eder', 'idade': 46, 'cidade': 'Santo André'},
#           {'nome': 'Rita', 'idade': 41, 'cidade': 'Recife'}, 
#           {'nome': 'Elena', 'idade': 8, 'cidade': 'São Paulo'}]

#---------- Para cada item da lista, extrai os dados do dicionario e imprime
# for pessoa in pessoas:
#    nome = pessoa['nome']
#    idade = pessoa['idade']
#    cidade = pessoa['cidade']
#    print (f'- {nome}  |  {idade}  |  {'cidade'}')
#    print (f'- {pessoa}')

#---------- Usando Dicionario de dicionarios

#pessoas = {'Eder': {'idade': '46', 'cidade': 'Santo André', 'cor': 'Preto'},
#            'Rita': {'idade': '41', 'cidade': 'Recife', 'cor': 'Verde'},
#            'Elena': {'idade': '8', 'cidade': 'São Paulo', 'cor': 'Vermelho'}}

#---------- Imprime o nome para cada pessoa no dicionario
#for pessoa in pessoas:
#    print(f'-{pessoa}')


#---------- Imprime a idade para cada item do dicionario 
#for pessoa in pessoas.items():
#    print (pessoa[1]['idade'])


#---------- Imprime nome | idade para cada item do dicionario
#for pessoa in pessoas:
#    print(f'- {pessoa} | {pessoas[pessoa]['idade']}')

#for pessoa in pessoas:
#    print(f'- {pessoa} | {pessoas[pessoa]['idade']} | {pessoas[pessoa]['cidade']} | {pessoas[pessoa]['cor']}')

pessoa = {'nome': 'Eder', 'idade': 46}
print(pessoa)
pessoa['cor'] = 'Preto'
print(pessoa)
pessoa['cidade'] = 'São Paulo'
print(pessoa)
pessoa.update({'cor': 'Azul'})
print(pessoa)
del pessoa['cor']
print(pessoa)
pessoa.update({'cidade': 'Santo André'})
print(pessoa)