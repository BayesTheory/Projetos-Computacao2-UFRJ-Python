#Lista 3
# Rian Costa Ferreira
#120046792
class Aluno:
    def __init__(self, nome, DRE, matricula = "ativa"):
        """Cria um objeto da classe Aluno com atributos nome, DRE, matricula"""
        self.nome = nome
        self.DRE = DRE       
        self.matricula = matricula

    def trancarMatricula(self):
        """Tranca a matricula"""
        self.matricula = "trancada"
        
    def cancelarMatricula(self):
        """Cancela a matricula"""
        self.matricula = "cancelada"
        
    def reativarMatricula(self):
        """Reativa a matricula se a matricula não for cancelada"""
        if self.matricula == "cancelada":
            print("Matrícula cancelada, solicite reabertura de matrícula")
        else:
            self.matricula = "ativa"
            
    def __str__(self): # método novo
        """Retorna uma descrição de um objeto da classe"""
        return "{}, DRE {}, matricula {}\n".format(self.nome, str(self.DRE), self.matricula)
#
# 2
#
class Bolsista(Aluno): #2A & 2B
    """Define a classe Bolsista com a superclasse Aluno"""
    def __init__(self, nome, DRE, bolsa,matricula = 'ativa'):
        """Atribui a classe para os atributos com o método trancarMatricula implementado"""
        super().__init__(nome, DRE,matricula)
        self.bolsa = bolsa

class Disciplina:
    """Classe representa o conceito de uma disciplina na UFRJ"""
    def __init__(self, nome, carga, vagas = 40):
        self.nome = nome
        self.carga = carga
        self.vagas = vagas
    
    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        return self.nome
#
# 1
#
class Turma(Disciplina): #1A
    """Cria a classe turma para usar o construtor da superclasse Disciplina."""
    def __init__(self, nome, carga, vagas, horario, alunos = []):
        """Atribui 5 atrbutos sendo 3 herdados da superclasse"""
        super().__init__(nome, carga, vagas)
        self.horario = horario
        self.alunos = alunos
    
    def __add__(self,other): #1B
         """Junta dois objetos, se diferir imprime uma mensagem """
         if(self.nome == other.nome and self.carga == other.carga and self.horario == other.horario):
            return Turma(self.nome, self.carga, self.vagas + other.vagas,self.horario, self.alunos + other.alunos)
         else:
            erro = "Não foi possível juntar as turmas."
            if(self.nome != other.nome):
               erro += " Nomes têm que ser iguais"
            if(self.carga != other.carga):
               erro += " Cargas têm que ser iguais."
            if(self.horario != other.horario):
               erro += "Horários têm que ser iguais."
            print(erro)
  
    def __str__(self): #1C
        """Retorna uma string com os dados de um objeto de uma classe"""
        return "{}, carga: {} , Horario: {} , Vagas Totais {} ,Vagas Livres {} \n".format(self.nome, self.carga, self.horario ,self.vagas,self.vagas - len(self.alunos) )

    
#  Herança ================================

class Monitor(Aluno):
    """Representa o conceito de um monitor"""
    def __init__(self, nome, DRE, historico = []):
        """O parametro historico deve ser uma lista de listas, onde o primeiro
        elemento da sublista é uma disciplina e o segundo elemento é o período."""
        super().__init__(nome, DRE)
        self.historico = historico

    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        string =  Aluno.__str__(self) + "HISTÓRICO DE MONITORIA\n"
        string += "Nome da Disciplina\tCarga horária\tPeríodo de monitoria\n"
        for entrada in self.historico:
            turma = entrada[0]
            periodo = entrada[1]
            string += "{}\t\t{}\t\t{}\n".format(turma.nome, turma.carga, periodo)
        return string
            
#fulano = Aluno("Adam", 123)
#fulana = Aluno("Eva", 111)
#mab241 = Disciplina("Computação II", 60)
#mab200 = Disciplina("Algebra I", 60)
#monitor1 = Monitor("Adam", 123, [[mab241, "2020-2"],[mab200, "2021-1"]])
#mab241 = Turma("Algebra I", 60, 30, "Ter 8-10")
#mab200 = Turma("Algebra I", 80, 100, "Qua 10-12", [fulano, fulana])
#bolsista1 = Bolsista("Adam", 456, 1200)
#o = mab200 + mab241
#bolsista1.trancarMatricula()
#print(bolsista1)