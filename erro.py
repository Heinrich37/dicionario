try: #try reconhece se o usuario digitar nesse caso alguma letra, junto ao except que é tipo um else
    a =int(input("Digite um numero: "))
except:
    print("Digite apenas numero")









try:
    a =int(input("Digite um numero: "))
except ValueError:
    print("Digite apenas numero")
except:
    print("Erro desconhecido")
    










try:
    a =int(input("Digite um numero: "))
except ValueError:
    print("Digite apenas numero")

except: 
    print("Erro desconhecido")

finally: #ele segue o programa normalmente mesmo se houver erro
    print("Programa finalizado")



    