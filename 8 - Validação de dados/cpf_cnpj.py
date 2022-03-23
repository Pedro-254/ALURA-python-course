from validate_docbr import CPF,CNPJ


class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if tipo_documento == "cpf":
            if self.cpf_eh_Valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!!")
        elif tipo_documento == "cnpj":
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!!")
        else:
            raise ValueError("Documento inválido!!")
    
    
    def cpf_e_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de digitos inválida!!")
        
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
    def __str__(self) -> str:
        return self.format_cpf()
    
    def cnpj_e_valido(self,cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return(validate_cnpj.validate(cnpj))
        else:
            ValueError("Quantidade de digitos inválida!!")