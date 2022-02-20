import re

class Funcionario:
    # Criando as caracteristicas da classe
    def __init__(self,nome,cpf,rg,telefone):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        
        self.valida_nome()
        self.valida_cpf()
        self.valida_rg()
        self.valida_telefone()
        
        self.formaliza_nome()
        self.formaliza_cpf()
        self.formaliza_telefone()
    
    # Validando informações
    def valida_nome(self):
        nome = self.nome.strip()
        
        if not nome:
            raise ValueError("O nome está vazio")
        
    def valida_cpf(self):
        if not self.cpf:
            raise ValueError("O CPF está vazio.")    
        
        padrao_cpf = re.compile("[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}")
        match = padrao_cpf.match(self.cpf)
        
        if not match:
            raise ValueError("O CPF é invalido.")
        else:
            print("A CPF é válido.")
            
        
    
    def valida_rg(self):
        if not self.rg:
            raise ValueError("O RG está vazio.")    
        
        padrao_rg = re.compile("[0-9]{7}")
        match = padrao_rg.match(self.rg)
        
        if not match:
            raise ValueError("O RG é invalido.")
        else:
            print("A RG é válido.")
            
    def valida_telefone(self):
        if not self.telefone:
            raise ValueError("O telefone está vazio.")    
        
        padrao_telefone = re.compile("[+]?[0-9]{2}[(]?[0-9]{2}[)]?9[0-9]{8}")
        match = padrao_telefone.match(self.telefone)
        
        if not match:
            raise ValueError("O telefone é invalido.")
        else:
            print("O telefone é válido.")
    
    #Formaliza dados
    def formaliza_nome(self):
        self.nome = self.nome.lower().title()
        
    def formaliza_cpf(self):
        cpf = self.cpf
        cpf = cpf.strip(".-")
        
        self.cpf = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
    
    def formaliza_telefone(self):
        telefone = self.telefone
        telefone = telefone.strip("+")
        telefone = telefone.replace("(", "").replace(")","")
        
        self.telefone = f"+{telefone[0:2]}({telefone[2:4]}){telefone[4:13]}"
          
    # Print do objeto
    def __str__(self):
        return (f"Nome: {self.nome}\nCpf: {self.cpf}\nRG: {self.rg}\nTelefone: {self.telefone}" )
    
    # Comparação do objeto
    def __eq__(self, other):
        return self.nome == other.nome and self.cpf == other.cpf and self.rg == other.rg and self.telefone == other.telefone
    
            
f1 = Funcionario("pedro lucas adorno","12345678910","6288868","+5562985249317")
f2 = Funcionario("pedro lucas adorno","12345678910","6288868","5562985249317")
print(f1)
print(f1 == f2)