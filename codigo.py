numero_de_participantes=int(input('quantos iram participar? '))

 

if (numero_de_participantes <=5):
    print('reservada sala pequena de reuniões')
elif (numero_de_participantes <15):
    print('reservada sala média de reuniões')
elif (numero_de_participantes >=15):
    print('reservada sala grande de reuniões')