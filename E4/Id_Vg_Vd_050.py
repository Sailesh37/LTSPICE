import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'E4/S4_Id_Vg_Vd_50m.txt'

df = pd.read_csv(file_path, sep='\t')

print(df.head())
print(df.columns)
print(df.shape)
print(df.describe())

Vg_mob = df['Vg']
Id_mob = df['Id(UA_UB_0)']
Id_mob_mA = Id_mob*1000

# Select the approximately linear region

# ------------------------------------------------------------

# Example: choose the region manually

mask = (Vg_mob >= 0.4) & (Vg_mob <= 0.6)

Vg_mob_fit = Vg_mob[mask]

Id_mob_fit = Id_mob[mask]

# ------------------------------------------------------------

# Linear fit: ID = m*VGS + c

# ------------------------------------------------------------

m, c = np.polyfit(Vg_mob_fit, Id_mob_fit, 1)

# Threshold voltage = x-intercept

Vth_mob = -c / m

Vg_vsat = df['Vg']
Id_vsat = df['Id(VSAT_multiplied_by_100)']
Id_vsat_mA = Id_vsat*1000

mask = (Vg_vsat >= 0.4) & (Vg_vsat <= 0.6)

Vg_vsat_fit = Vg_vsat[mask]

Id_vsat_fit = Id_vsat[mask]
m, c = np.polyfit(Vg_vsat_fit, Id_vsat_fit, 1)
Vth_vsat = -c / m


Vg_def = df['Vg']
Id_def = df['Id(default)']
Id_def_mA = Id_def*1000

mask = (Vg_def >= 0.4) & (Vg_def <= 0.6)

Vg_def_fit = Vg_def[mask]

Id_def_fit = Id_def[mask]
m, c = np.polyfit(Vg_def_fit, Id_def_fit, 1)
Vth_def = -c / m

print(f"Threshold Voltage(UA = UB = 0) = {Vth_mob:.4f} V")
print(f"Threshold Voltage(VVSAT multiplied by 100) = {Vth_vsat:.4f} V")
print(f"Threshold Voltage(Default) = {Vth_def:.4f} V")


# Calculate I_ON and I_OFF at VDS = 1.1 V
# I_ON  : VGS = 1.1 V, VDS = 1.1 V
# I_OFF : VGS = 0 V,   VDS = 1.1 V

# UA = UB = 0
Ion_mob = df.loc[df['Vg'] == 1.1, 'Id(UA_UB_0)'].iloc[0]
Ioff_mob = df.loc[df['Vg'] == 0.0, 'Id(UA_UB_0)'].iloc[0]

# VSAT multiplied by 100
Ion_vsat = df.loc[df['Vg'] == 1.1, 'Id(VSAT_multiplied_by_100)'].iloc[0]
Ioff_vsat = df.loc[df['Vg'] == 0.0, 'Id(VSAT_multiplied_by_100)'].iloc[0]

# Default
Ion_def = df.loc[df['Vg'] == 1.1, 'Id(default)'].iloc[0]
Ioff_def = df.loc[df['Vg'] == 0.0, 'Id(default)'].iloc[0]

# Print results in microamperes
print("\n--- I_ON and I_OFF ---")

print(f"UA = UB = 0:")
print(f"I_ON  = {Ion_mob * 1e6:.6f} µA")
print(f"I_OFF = {Ioff_mob * 1e6:.6f} µA")

print(f"\nVSAT multiplied by 100:")
print(f"I_ON  = {Ion_vsat * 1e6:.6f} µA")
print(f"I_OFF = {Ioff_vsat * 1e6:.6f} µA")

print(f"\nDefault:")
print(f"I_ON  = {Ion_def * 1e6:.6f} µA")
print(f"I_OFF = {Ioff_def * 1e6:.6f} µA")



plt.figure(1, figsize=(10,6))

plt.plot(
    Vg_mob,
    Id_mob_mA,
    linewidth=2,
    label = 'UA = UB = 0'
)
plt.plot(
    Vg_vsat,
    Id_vsat_mA,
    linewidth=2,
    label = 'VSAT multiplied by 100'
)
plt.plot(
    Vg_def,
    Id_def_mA,
    linewidth=2,
    label = 'Default'
)
plt.title('IdVg Charateristics at Vd = 50mV')
plt.xlabel('Gate Voltage, $V_G$V')
plt.ylabel('Drain Current, $I_G$mA')
plt.legend(title='Conditions', loc ='upper left', title_fontsize='11', fontsize='10')
plt.grid(True, linestyle='--', alpha =0.6)
plt.tight_layout()
plt.savefig('Id_Vg_Vd_50mV.png', dpi =300)
plt.show()



