import math
#RIAN COSTA FERRERIRA
#120046792

#1a
def calculeN(a_n, a_1 ,r):
  """Retorna o número de termos n"""
  return ((a_n - a_1)/r)+1

#1b
def somaPA(a_n, a_1 ,n):
  """Retorna a soma Sn da progressão aritmética"""
  return ((a_n + a_1)*n)/2

#2
def concatena(sra,srb):
  """Retorna a concatenação modificada entre duas strings"""
  sra = sra [5:]  
  srb = srb [0:-10]  
  z = sra + srb
  return z

#3
def sublista(lista, n):
  """Retorna uma sublista por todos os elementos maiores que N"""
  return [x for x in lista if x > n]

#4
def primo(n): 
  """Retorna se este número é primo ou não."""
  if n > 1:
    for i in range(2,n):
        if (n % i) == 0:
            return False 
            break
    else:
      return True
  else:
    return False

#5a
def numeroEuler(n):
  """Retorna o valor de e por meio de uma série """
  sum1 = 1
  for i in range(1, n + 1):
      sum1 = sum1 + (1/math.factorial(i))
  return round(sum1, 2)

#5b
def precisaoEuler(erro):
  """Retorna a quantidade de termos que devem ser calculados para
o erro absoluto"""
  n = 0
  while True:
    if math.fabs(numeroEuler(n) - math.e) < erro:
      break
    n=n+1
  return n

#5c
def main():
  """Retorna a função main para a finalidade da função de cima"""
  erro = float(input("Qual a precisão desejada? "))
  print (precisaoEuler(erro))
if __name__ == "__main__":
  main()