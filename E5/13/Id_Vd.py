import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'E5/13/Id_Vd.txt'

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

Vg_low = df['Vd2']
Id_low = df['Id(Low2)']
Id_low_mA = Id_low*1000

plt.figure(1, figsize=(10,6))

plt.plot(
    Vd_high,
    Id_high_mA,
    linewidth=2,
    label = 'VSAT = 2e7 cm/s'
)
plt.plot(
    Vd_def,
    Id_def_mA,
    linewidth=2,
    label = 'VSAT = 1.24e7 cm/s'
)
plt.plot(
    Vg_low,
    Id_low_mA,
    linewidth=2,
    label = 'VSAT = 0.8e7 cm/s'
)
plt.title('IdVd Charateristics')
plt.xlabel('Drain Voltage, $V_D$V')
plt.ylabel('Drain Current, $I_D$mA')
plt.legend(title='Values of VSAT', loc ='upper left', title_fontsize='11', fontsize='10')
plt.grid(True, linestyle='--', alpha =0.6)
plt.tight_layout()
plt.savefig('E5/13/Id_Vd.png', dpi =300)
plt.show()