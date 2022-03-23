from validate_docbr import CPF,CNPJ
from cpf_cnpj import CpfCnpj

exemplo_cnpj = "35379838000112"
# cnpj = CNPJ()

# print(cnpj.validate(exemplo_cnpj))

documento = CpfCnpj(exemplo_cnpj,"cnpj")