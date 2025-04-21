def main():
    qtd_total = int(input())
    array = []
    contador = 1
    for i in range(qtd_total):
        var = int(input())
        array.append(var)
    for i in range(1, len(array)):
        if array[i] == array[i-1]:
            continue
        contador+=1
    print(contador)
main()