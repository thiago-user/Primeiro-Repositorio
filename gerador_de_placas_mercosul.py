from random import shuffle, sample
from string import ascii_uppercase, digits

alpha = sample(ascii_uppercase, 4)
numeric = sample(digits, 3)
placa = alpha + numeric
shuffle(placa)
placa = ''.join(placa)
print(f'Sua Nova Placa Mercosul: {placa}')

# https://portalespigao.com.br/wp-content/uploads/2018/12/Placas-mercosul_detran_ro.jpg
