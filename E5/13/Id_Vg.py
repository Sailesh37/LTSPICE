import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'E5/13/Id_Vg.txt'

df = pd.read_csv(file_path, sep='\t')

print(df.head())
print(df.columns)
print(df.shape)
print(df.describe())

Vg_def = df['Vg1']
Id_def = df['Id(Default1)']
Id_def_mA = Id_def*1000

Vg_high = df['Vg1']
Id_high = df['Id(High1)']
Id_high_mA = Id_high*1000

Vg_low = df['Vg1']
Id_low = df['Id(Low1)']
Id_low_mA = Id_low*1000

# Select the approximately linear region

# ------------------------------------------------------------

# Example: choose the region manually

mask = (Vg_high >= 0.5) & (Vg_high <= 0.9)

Vg_high_fit = Vg_high[mask]

Id_high_fit = Id_high[mask]

# ------------------------------------------------------------

# Linear fit: ID = m*VGS + c

# ------------------------------------------------------------

m, c = np.polyfit(Vg_high_fit, Id_high_fit, 1)

# Threshold voltage = x-intercept

Vth_high = -c / m

mask = (Vg_def >= 0.5) & (Vg_def <= 0.9)

Vg_def_fit = Vg_def[mask]

Id_def_fit = Id_def[mask]
m, c = np.polyfit(Vg_def_fit, Id_def_fit, 1)
Vth_def = -c / m

mask = (Vg_low >= 0.5) & (Vg_low <= 0.9)

Vg_low_fit = Vg_low[mask]

Id_low_fit = Id_low[mask]
m, c = np.polyfit(Vg_low_fit, Id_low_fit, 1)
Vth_low = -c / m

print(f"Threshold Voltage(VSAT = 2e7 cm/s) = {Vth_high:.4f} V")
print(f"Threshold Voltage(VSAT = 1.24e7 cm/s) = {Vth_def:.4f} V")
print(f"Threshold Voltage(VSAT = 0.8e7 cm/s) = {Vth_low:.4f} V")


Ion_high = df.loc[df['Vg1'] == 1.1, 'Id(High1)'].iloc[0]
Ioff_high = df.loc[df['Vg1'] == 0.0, 'Id(High1)'].iloc[0]

Ion_def = df.loc[df['Vg1'] == 1.1, 'Id(Default1)'].iloc[0]
Ioff_def = df.loc[df['Vg1'] == 0.0, 'Id(Default1)'].iloc[0]

# Default
Ion_low = df.loc[df['Vg1'] == 1.1, 'Id(Low1)'].iloc[0]
Ioff_low = df.loc[df['Vg1'] == 0.0, 'Id(Low1)'].iloc[0]

# Print results in microamperes
print("\n--- I_ON and I_OFF ---")

print(f"VSAT = 2e7 cm/s")
print(f"I_ON  = {Ion_high * 1e6:.6f} µA")
print(f"I_OFF = {Ioff_high * 1e6:.6f} µA")

print(f"\nVSAT = 1.24e7 cm/s")
print(f"I_ON  = {Ion_def * 1e6:.6f} µA")
print(f"I_OFF = {Ioff_def * 1e6:.6f} µA")

print(f"\nVSAT = 0.8e7 cm/s")
print(f"I_ON  = {Ion_low * 1e6:.6f} µA")
print(f"I_OFF = {Ioff_low * 1e6:.6f} µA")

plt.figure(1, figsize=(10,6))

plt.plot(
    Vg_high,
    Id_high_mA,
    linewidth=2,
    label = 'VSAT = 2e7 cm/s'
)
plt.plot(
    Vg_def,
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
plt.title('IdVg Charateristics')
plt.xlabel('Gate Voltage, $V_G$V')
plt.ylabel('Drain Current, $I_G$mA')
plt.legend(title='Values of VSAT', loc ='upper left', title_fontsize='11', fontsize='10')
plt.grid(True, linestyle='--', alpha =0.6)
plt.tight_layout()
plt.savefig('E5/13/Id_Vg.png', dpi =300)
plt.show()