#Rian Costa Ferreira
#dre:120046792

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
            
    def dados(self):
        """Retorna uma descrição de um objeto da classe"""
        return "{}\t{}\tmatricula {}".format(self.nome, str(self.DRE), self.matricula)
    
#=======================================

class Disciplina:
    """Classe representa o conceito de uma disciplina na UFRJ"""
    def __init__(self, nome, vagas = 0):
        """Cria um objeto da classe com atributos nome, vagas, alunos"""
        self.nome = nome
        self.vagas = vagas
        self.alunos = [] # self.alunos é um atributo global criado automaticamente

    def __add__(self, other):
        """Junta duas disciplinas se o nome delas for idêntico"""
        if self.nome == other.nome:
            return Disciplina(self.nome, self.vagas + other.vagas)
        else:
            print("Não foi possível juntar as turmas")
    
    def inscreverAluno(self, aluno):
        """Inscreve um objeto da classe Aluno na disciplina se tiver
        vagas livres ou o Aluno não for ainda inscrito na disciplina"""
        if len(self.alunos) < self.vagas and aluno not in self.alunos:
            self.alunos.append(aluno)
        elif aluno in self.alunos:
            print("aluno {} já está inscrito na disciplina".format(aluno.nome))
        else:
            print("Vagas esgotadas")
    
#1b    
    def _str_(self):
        """Retorna uma descrição de um objeto da  classe"""
        info = self.nome + ', alunos inscritos:'
        for aluno in self.alunos:
            info += '\n' + aluno.dados
        info += self.consultarVagas()
        return info
###1a
    def consultarVagas(self):
        """ Retorna vagas totais e livres"""
        return("Vagas Totais: {}. Vagas Livres: {}".format(self.vagas, self.vagas - len(self.alunos)))


##################################
#2a
class Pessoa:
    def __init__(self, nome, dataNascimento, nomeDeMae=None, nomeDoPai=None):
      """"Cria um objeto da classe Pessoa com atributos nome, Data de Nascimento, Nome da mãe , Nome do Pai"""
      self.nome = nome
      self.dataNascimento = dataNascimento
      self.nomeDeMae = nomeDeMae
      self.nomeDoPai = nomeDoPai
#2b
    from datetime import date
    def idade(self, data = date.today().strftime("%d/%m/%Y")):
        """Retorna um inteiro que é a idade em anos no dia da data"""
        diax = int(self.dataNascimento[:2])
        mesx = int(self.dataNascimento[3:5])
        anox = int(self.dataNascimento[6:])
        dia = int(data[:2])
        mes = int(data[3:5])
        ano = int(data[6:])
        if (mesx == mes and diax > dia) or mesx > mes:
            return ano - anox - 1
        else:
            return ano - anox   
#2c     
    def __str__(self):
        """Retorna uma string com os dados de um objeto da classe"""
        return  ("nome: %s , idade: %d , mãe: %s , pai:%s" % (self.nome,self.idade(),self.nomeDeMae.nome,self.nomeDoPai.nome))
        return None
      