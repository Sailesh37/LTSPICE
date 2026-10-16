import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'E3/S3.txt'
try:
    df = pd.read_csv(file_path, sep='\t')
    print("CSV file successfully loaded!")
    print(df.columns) # ALWAYS check the exact column names
except FileNotFoundError:
    print(f"Error: Could not find ’{file_path}’. Check the path and try again.")
    exit()

Vd_03 = df['Vd']
Id_03 = df['Id(M1)']
Id_03_mA = Id_03 * 1e3

Vd_06 = df['Vd']
Id_06 = df['Id(M2)']
Id_06_mA = Id_06 * 1e3

Vd_09 = df['Vd']
Id_09 = df['Id(M3)']
Id_09_mA = Id_09 * 1e3

Vd_15 = df['Vd']
Id_15 = df['Id(M4)']
Id_15_mA = Id_15 * 1e3

plt.figure(1, figsize= (10 ,6))

plt.plot(
    Vd_03,
    Id_03_mA,
    linewidth=2,
    label= '$V_G$ = 0.3V'
)
plt.plot(
    Vd_06,
    Id_06_mA,
    linewidth=2,
    label= '$V_G$ = 0.6V'
)
plt.plot(
    Vd_09,
    Id_09_mA,
    linewidth=2,
    label= '$V_G$ = 0.9V'
)
plt.plot(
    Vd_15,
    Id_15_mA,
    linewidth=2,
    label= '$V_G$ = 1.5V'
)
plt.title('IdVd characteristics')
plt.xlabel('Drain Voltage,$V_D$V')
plt.ylabel('Drain Current,$I_D(mA$')
plt.legend(title = 'Gate Voltage',title_fontsize='11', loc='upper left', fontsize='10')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('IdVd.png', dpi=300)
plt.show()

# Output resistance at VGS = 1.5 V

# Output resistance at VGS = 1.5 V

mask = (Vd_15 >= 1.0) & (Vd_15 <= 1.5)

Vd_15_sat = Vd_15[mask].to_numpy()
Id_15_sat = Id_15[mask].to_numpy()

# Calculate output conductance
gds = np.gradient(Id_15_sat, Vd_15_sat)

# Calculate output resistance
ro = 1 / gds

# Plot output resistance
plt.figure(2, figsize=(10, 6))

plt.plot(
    Vd_15_sat,
    ro / 1e3,
    linewidth=2,
    label='$V_{GS} = 1.5V$'
)

plt.title('Output Resistance at $V_{GS} = 1.5V$')
plt.xlabel('Drain Voltage, $V_D$ (V)')
plt.ylabel('Output Resistance, $r_o$ (k$\\Omega$)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig('Output Resistance.png', dpi=300)
plt.show()

print("Output conductance (S):", gds)
print("Output resistance (kOhm):", ro / 1e3)

# Report output conductance and resistance
print("Output conductance (S):", gds)
print("Output resistance (kohms):", ro / 1e3)