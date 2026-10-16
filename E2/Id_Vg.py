import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'E2/S2.txt'

df = pd.read_csv(file_path, sep='\t')

print(df.head())
print(df.columns)
print(df.shape)
print(df.describe())

Vg_050 = df['Vg']
Id_050 = df['Id(M1)']
Id_050_mA = Id_050*1000

Vg_11 = df['Vg']
Id_11 = df['Id(M2)']
Id_11_mA = Id_11*1000

# Select the approximately linear region

# ------------------------------------------------------------

# Example: choose the region manually

mask = (Vg_050 >= 0.4) & (Vg_050 <= 0.6)

Vg_050_fit = Vg_050[mask]

Id_050_fit = Id_050[mask]

# ------------------------------------------------------------

# Linear fit: ID = m*VGS + c

# ------------------------------------------------------------

m, c = np.polyfit(Vg_050_fit, Id_050_fit, 1)

# Threshold voltage = x-intercept

Vth_050 = -c / m

mask = (Vg_11 >= 0.4) & (Vg_11 <= 1)

Vg_11_fit = Vg_11[mask]

Id_11_fit = Id_11[mask]
m, c = np.polyfit(Vg_11_fit, Id_11_fit, 1)
Vth_11 = -c / m

print(f"Threshold Voltage(Vd=0.05V) = {Vth_050:.4f} V")
print(f"Threshold Voltage(Vd=1.1V) = {Vth_11:.4f} V")

plt.figure(1, figsize=(10,6))

plt.plot(
    Vg_050,
    Id_050_mA,
    linewidth=2,
    label = '$V_D$ = 50 mV'
)
plt.plot(
    Vg_11,
    Id_11_mA,
    linewidth=2,
    label = '$V_D$ = 1.1 V'
)
plt.title('IdVg Charateristics')
plt.xlabel('Gate Voltage, $V_G$V')
plt.ylabel('Drain Current, $I_G$mA')
plt.legend(title='Drain Voltage', loc ='upper left', title_fontsize='11', fontsize='10')
plt.grid(True, linestyle='--', alpha =0.6)
plt.tight_layout()
plt.savefig('Id_Vg.png', dpi =300)
plt.show()



