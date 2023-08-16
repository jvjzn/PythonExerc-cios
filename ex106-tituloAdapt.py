def titulo(msg):
    tam = len(msg) + 4
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)

titulo(str(input("Insira o título: ")))