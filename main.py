import requests
from datetime import datetime
import csv

chave = 'XXXXXXXXXXXXXXXX'

def extrairDados(dicio):
    elementos = dicio['elements'][0]
    distancia = elementos['distance']['value']
    duração = elementos['duration']['value']#segundos
    return (distancia,duração)



def escreve_no_arquivo(nome_arquivo, informacao):
  with open(nome_arquivo, 'a') as arquivo_csv:
    escrever = csv.writer(arquivo_csv, delimiter=',', lineterminator="\n")
    escrever.writerow(informacao)


ref_arquivo = open("coordenadas.txt","r")
i = 0
requisicao = ''
for coordenada in ref_arquivo:
    if(i%2 == 0):
      origem = coordenada.split()[0]
    else:
      destino = coordenada.split()[0]

      requisicao = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+origem+'&destinations='+destino+'&key='+chave

      dados_rota = requests.get(requisicao)
      distancia_tempo= extrairDados(dados_rota.json()['rows'][0])

      data_e_hora = datetime.now()
      escreve_no_arquivo("dados.csv", [str(distancia_tempo[0]), str(distancia_tempo[1]), data_e_hora.strftime('%d/%m/%Y - %H:%M')])

    i+=1
ref_arquivo.close()

