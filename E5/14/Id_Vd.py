import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'E5/14/Id_Vd.txt'

df = pd.read_csv(file_path, sep='\t')

print(df.head())
print(df.columns)
print(df.shape)
print(df.describe())

Vd_def = df['Vd2']
Id_def = df['Id(Default2)']
Id_def_mA = Id_def*1000

Vd_high = df['Vd2']
Id_high = df['Id(High2)']
Id_high_mA = Id_high*1000

Vd_low = df['Vd2']
Id_low = df['Id(Low2)']
Id_low_mA = Id_low*1000

plt.figure(1, figsize=(10,6))

plt.plot(
    Vd_high,
    Id_high_mA,
    linewidth=2,
    label = 'RDSW = 400 Ω·μm'
)
plt.plot(
    Vd_def,
    Id_def_mA,
    linewidth=2,
    label = 'RDSW = 165 Ω·μm'
)
plt.plot(
    Vd_low,
    Id_low_mA,
    linewidth=2,
    label = 'RDSW = 50 Ω·μm'
)
plt.title('IdVd Charateristics')
plt.xlabel('Drain Voltage, $V_D$V')
plt.ylabel('Drain Current, $I_D$mA')
plt.legend(title='Values of RDSW ', loc ='upper left', title_fontsize='11', fontsize='10')
plt.grid(True, linestyle='--', alpha =0.6)
plt.tight_layout()
plt.savefig('E5/14/Id_Vd.png', dpi =300)
plt.show()