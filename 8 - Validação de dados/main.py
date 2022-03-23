from validate_docbr import CPF,CNPJ
from cpf_cnpj import CpfCnpj

exemplo_cnpj = "3537983800011"
# cnpj = CNPJ()

# print(cnpj.validate(exemplo_cnpj))

documento = CpfCnpj(exemplo_cnpj,"cnpj")