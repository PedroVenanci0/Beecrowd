def main():
    espaco = " "
    procedimento_01(espaco)
    procedimento_02(espaco)
    procedimento_03(espaco)
    procedimento_04(espaco)
    procedimento_05(espaco)
    procedimento_04(espaco)
    procedimento_03(espaco)
    procedimento_02(espaco)
    procedimento_01(espaco)
    
def procedimento_01(espaco):
    print(f'{espaco * 7}A')
def procedimento_02(espaco):
    print(f'{espaco * 6}B{espaco * 1}B')
def procedimento_03(espaco):
    print(f'{espaco * 5}C{espaco * 3}C')
def procedimento_04(espaco):
    print(f'{espaco * 4}D{espaco * 5}D')
def procedimento_05(espaco):
    print(f'{espaco * 3}E{espaco * 7}E')
main()

