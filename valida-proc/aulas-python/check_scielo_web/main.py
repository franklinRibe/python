#!/usr/bin/python3
# coding: utf-8

import requests
from lxml import html
import re

"""
O que iremos fazer?

    Poder ter a capacidade de garantir que os novos conteudos foram inseridos no site do SciELO

Como iremos fazer?
    verificar a cada termino de processamento os novos dados que foram inseridos

Iremos utilizar programação estruturada em python

Temos a scilista.lst como indicação das últimas alterações validadas.

""" 
REGEX_ISSN = r'[\S]{4}\-[\S]{4}'
PROTOCOL = 'http://'
DOMAIN = 'www.scielo.br'
URL_SEGMENT = 'scielo.php?script=%s&pid=%s'
SCRIPT_URL = {
                'grid': 'sci_issues',
                'toc': 'sci_issuetoc',
                'article': 'sci_arttext'
}

if __name__ == "__main__":

    # Ler o arquivo Scilista

    fp = open("/Users/franklin.ribeiro/Documents/Python/valida-proc/aulas-python/check_scielo_web/scilista.lst", 'r')

    issns = []
    j_not_found = []

    for line in fp.readlines():
        acron, issue_label = line.split()
        ret = requests.get("%s%s/%s" % (PROTOCOL, DOMAIN, acron))
        if ret.status_code == 200:
            issn = re.search(REGEX_ISSN, ret.url)
            issns.append(issn.group())
        else:
            j_not_found.append(issn.group())
    for issn in issns:
        url_segment = URL_SEGMENT % (SCRIPT_URL['grid'], issn)
        ret = requests.get("%s%s/%s" % (PROTOCOL, DOMAIN, url_segment))

        tree = html.fromstring(ret.content)
        table = tree.xpath('//table')[3]
        print("Conteúdo da tablela fasciculo: %s \n" % table.text_content)
        


    print("teste")