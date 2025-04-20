def main():
    a = int(input())
    resultado = 1
    while True:
        resultado *= a
        a -= 1
        if a == 0:
            break
    print(resultado)
main()