def main():
    qtd = int(input())
    var_control = 1

    array_01 = []
    array_02 = []
    array_03 = []

    for i in range(1, qtd+1):
        array_01.append(i)
        array_01.append(i)

        array_02.append(i**2)
        array_02.append(i**2 + 1)

        array_03.append(i**2*var_control)
        array_03.append(i**2*var_control+1)

        var_control+=1
    
    for i in range(len(array_03)):
        print(array_01[i], array_02[i],array_03[i])
        

main()