import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

plt.plot(df['dia'], df['venda'])

plt.xlabel('Dia')
plt.ylabel('Venda')
plt.title('Vendas por dia de gasolina:')

plt.savefig('gasolina.png', dpi=300, bbox_inches='tight')

plt.show