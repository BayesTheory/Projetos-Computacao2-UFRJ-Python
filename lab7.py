#Rian Costa Ferreira
import numpy as np
import math

#1

def calcularAngulo(x,y):
  """Calcula e retorna ângulo em graus ou None"""
  j = math.pow(x, 2)
  k = math.pow(y, 2)
  s =j+k
  if s!=1:
    return None
  else:
    if x<0 :
        x = math.asin(x)
        return math.degrees(x)
    else:
        y = math.acos(y)
        return math.degrees(y)


#2
def analisarIsometria(Ab):
   """A funçãodeve analisar a transformação representada pela Ab e retornar uma string com a conclusão da análise"""
   b=(Ab[:,2])
   a=(Ab[0:2,0:2])
   if np.allclose((np.transpose(a)@a),(np.eye(2))):  
      if np.linalg.det(a) <= 0 :       
          R = np.array([[1,0],[0,-1]])
          a = a@np.transpose(R)
          return("A transformacao é uma isometria composta de reflexão pelo eixo x, rotação pelo ángulo {}".format(a))
      else:
          x = Ab[0,0]
          y = Ab[1,0]
          s = (calcularAngulo(x,y))
      if s!= 0:
              return ("A transformacao é uma isometria composta de rotação pelo ângulo {} graus".format(calcularAngulo(x,y)))
      zero = (np.array([0,0]))
      if np.allclose((zero) ,(b)):
              return("A transformacao é uma isometria composta de translação pelo vetor {}".format(b))
   else:
        return ("A transformacao não é uma isometria.")




