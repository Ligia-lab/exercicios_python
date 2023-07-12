# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.


def aumentar(preço=0, taxa=0, formato=False):
    """
    Aumento do valor
    Args:
        preço: valor
        taxa: porcentagem de aumento
        formato: formato de exibição, como dinheiro ou não, padrão False

    Returns: valor com aumento

    """
    res = (preço * (taxa / 100)) + preço
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    """
    desconto no valor
    Args:
        preço: valor original
        taxa: porcentagem de desconto
        formato: normal ou em forma de moeda, padrão flase

    Returns:valor com desconto

    """
    res = preço - (preço * (taxa / 100))
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    """
    dobro do valor
    Args:
        preço: valor
        formato: formatado ou não. padrão false

    Returns: dobro do valor

    """
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    """
    metade do valor
    Args:
        preço: valor
        formato: formatado ou não, padrão false

    Returns:metade do valor

    """
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    """
    formatação do valor, com subtituição do ponto por virgula
    Args:
        preço: valor
        moeda: moeda desejada (não converte), padrão R$

    Returns: valor formatado

    """
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxad=5):
    """
    Resumo das operações
    Args:
        preço: valor
        taxaa: taxa de aumento, padrão 10%
        taxad: taxa de desconto, padrão 5%

    Returns: tabela com todas as informações

    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxad}% de desconto: \t{diminuir(preço, taxad, True)}')
    print('-' * 30)

