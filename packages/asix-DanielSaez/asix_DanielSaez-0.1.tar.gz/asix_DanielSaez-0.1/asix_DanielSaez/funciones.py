def Calcular_Segundos(h,m,s):
    totalsegundos=(h*60*60)+(m*60)+s
    return totalsegundos

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def EsPrimo (numero):
    numero=abs(numero)
    primo=True
    if numero==0 or numero==1 or numero == 2:
        #print (f"El numero {numero} es primo")
        return True
    elif numero%2==0:
        return False
    for i in range (3,round (numero/2),2):
        if numero%i==0:
            primo=False

    return primo