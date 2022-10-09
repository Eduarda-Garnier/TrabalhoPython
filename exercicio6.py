arquivo = float(input(' Informe o tamanho do arquivo para download (em MB): '))
link = float(input("Informe a velocidade do link de Internet (em Mbps) "))
tempo = ((arquivo * 8) / link) / 60
print ("Tempo aproximado de download é %.2f minutos" %tempo)



