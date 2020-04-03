import requests
chave = 'APY-KEY'
requisicoes = []
#---------ROTA 01 -------------
#Av. Nossa Sra. de Nazaré, 1271-1261 - Nazaré, Belém - PA, 66035-445
#-1.452206,-48.481416
#Tv. Padre Eutíquio, 984-1154 - Campina, Belém - PA, 66025-230
#-1.457468,-48.494745
requisicoes.append('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=-1.452206,-48.481416&destinations=-1.457468,-48.494745&key='+chave)

#--------- ROTA 02 -------------
#Av. Gov. José Malcher, 2648-2790 - Nazaré, Belém - PA, 66090-100
#-1.448348, -48.469195
#Av. Blvd. Castilhos França, 229-1 - Campina, Belém - PA, 66010-070
#-1.449444, -48.500284
requisicoes.append('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=-1.448348,-48.469195&destinations=-1.449444,-48.500284&key='+chave)

#--------- ROTA 03 -------------
#Av. Visc. de Souza Franco, 459-383 - Reduto, Belém - PA, 66053-020
#-1.445592, -48.488804
#Passagem Onze Bandeirinhas II, 94 - Guamá, Belém - PA, 66075-245
#-1.468513, -48.467681
requisicoes.append('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=-1.445592,-48.488804&destinations=-1.468513,-48.467681&key='+chave)

#--------- ROTA 04 -------------
#Av. Nossa Sra. de Nazaré, 1271-1261 - Nazaré, Belém - PA, 66035-445
#-1.452206, -48.481416
#Av. Sen. Lemos, 1638-1850 - Sacramenta, Belém - PA
#-1.429142, -48.485157
requisicoes.append('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=-1.452206,-48.481416&destinations=-1.429142,-48.485157&key='+chave)

#--------- ROTA 05 -------------
#Passagem Onze Bandeirinhas II, 94 - Guamá, Belém - PA, 66075-245
#-1.468513, -48.467681
#Av. Blvd. Castilhos França, 229-1 - Campina, Belém - PA, 66010-070
#-1.449444, -48.500284
requisicoes.append('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=-1.468513,-48.467681&destinations=-1.449444,-48.500284&key='+chave)


def extrairDados(dicio):
    elementos = dicio['elements'][0]
    distancia = elementos['distance']['value']
    duração = elementos['duration']['value']#segundos
    return (distancia,duração)
     

for i in requisicoes:
    rota = requests.get(i)
    print(extrairDados(rota.json()['rows'][0]))
    print()
    
#print(extrairDados(rota01.json()['rows'][0]))

