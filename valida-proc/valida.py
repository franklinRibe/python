import requests

''' revista gaucha de enfermagem código 1983-1447
 página http://homolog.revenf.bvs.br/scielo.php?script=sci_issues&pid=1983-1447
'''

#Primeiro cria objeto para armazenar página inicial do Revenf

r = requests.get('http://homolog.revenf.bvs.br/scielo.php?script=sci_issues&pid=1983-1447')

URL = 'http://homolog.revenf.bvs.br/scielo.php?script=sci_issues&pid=%s'

##criando lista das revistas do Revenf

revistas = {'ape':'0103-2100', 'ccs':'1677-3861', 'ce':'1414-8536', 'ean':'1414-8145', 'reme':'1415-276', 'rene':'1517-3852', 'rbaen':'2178-8650', 'reben':'0034-7167', 'cuid':'2216-0973', 'reeusp':'0080-6234', 'reuerj':'0104-3552', 'rgenf':'1983-1447', 'rlae':'0104-1169', 'tce':'0104-0707', 'objn':'1676-4285', 'ree':'1518-1944', 'rpe':'0100-8889', 'smad':'1806-6976'}

#verificar o código HTTP e armazena em variável

cod_http = r.status_code

# Testa se o site foi encontrado, caso contrário. encerra
if cod_http == 200:
    print('Site acessível, continuando...')
else:
    print('Site Inacessível, verificar...')


fyle = open('/Users/franklin.ribeiro/Documents/Python/valida-proc/scilista.txt', 'r')

lines = fyle.readlines()

# issns = [revistas[line.split()[0]] for line in lines]

issns = []

for line in lines:
    issns.append(revistas[line.split()[0]])

print(issns)

for issn in issns:
    print(requests.get(URL % issn))
