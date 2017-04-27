#Introdução _Camila_ESOF (Sprint 1)
# Foram utilizados comandos/funções descritas no capítulo 8.
#Tais como:
#Especificação e identificação de caminhos de arquivo; escrita e fechamento de arquivo;
#o comando random utilizado no exemplo prático;

import os
os.chdir('C:\\Users\\camil_000')#Insira um caminho válido e em seguida crie um arquivo txt com a nomeação abaixo.
os.getcwd()

escreveArquivo = open('QuizzA.txt','w')
           
print('Seja bem vindo!')
escreveArquivo.write('Seja bem vindo!')
print(' ')
escreveArquivo.write('\n\n')

print('Insira seu nome, em seguida precione "Enter".')
escreveArquivo.write('Insira seu nome')
name = input('Insira seu nome: ')
escreveArquivo.write('Nome: '+str(name))
escreveArquivo.write('\n\n')

print(' ')
escreveArquivo.write('\n\n')
print('Olá,' ,name+'!')
escreveArquivo.write('Olá, '+ str(name)+' !')
print(' ')
escreveArquivo.write('\n\n')
print(name,': Pratique um pouco o raciocínio com as questões abaixo!')
escreveArquivo.write(str(name)+' : Pratique um pouco o raciocínio com as questões abaixo!')
print(' ')
escreveArquivo.write('\n\n')

pont=0
qtd=1
import random

while qtd <= 5:
      num1 = random.randint(1,10)
      num2 = random.randint(1,10)
      num3 = random.randint(1,10)
      quest = num1+num2*num3
      print('Questão número',qtd)
      escreveArquivo.write('Questão número'+ str(qtd))
      escreveArquivo.write('\n\n')
      print('Quanto é ', str(num1)+ ' + ', str(num2),' x ',str(num3),' ? ')
      escreveArquivo.write('Quanto é ' + str(num1)+ ' + '+ str(num2)+' x '+str(num3)+' ? ')
      print(' ')
      escreveArquivo.write('\n\n')
      resp=int(input('escreva sua resposta: '))
      escreveArquivo.write('escreva sua resposta: '+str(resp))
      if resp==quest:
                 print(' ')
                 escreveArquivo.write('\n\n')
                 print ('Correto')
                 escreveArquivo.write('Correto!')
                 pont=pont+1
               
      else:
                 print(' ')
                 escreveArquivo.write('\n\n')
                 print('Incorreto')
                 escreveArquivo.write('Incorreto!')
      qtd=qtd+1
      print(' ')
      escreveArquivo.write('\n\n')
print('Terminou o questionário, sua pontução final é',pont,'de 5')
escreveArquivo.write('Terminou o questionário, sua pontução final é '+str(pont)+' de 5')
escreveArquivo.close()             
