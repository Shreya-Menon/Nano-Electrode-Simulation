import matplotlib.pyplot as plt

def plot_energy_density(materials, energy_densities):
    plt.figure(figsize=(8, 5))
    plt.bar(materials, energy_densities, color=['blue', 'green', 'red'])
    plt.title("Energy Density Comparison of Nano-Coatings")
    plt.xlabel("Material")
    plt.ylabel("Energy Density (Wh/kg)")
    plt.show()

def plot_degradation(cycles, performances, material):
    plt.figure(figsize=(8, 5))
    plt.plot(cycles, performances, label=f"{material} Performance")
    plt.title(f"Electrode Degradation for {material}")
    plt.xlabel("Charge/Discharge Cycles")
    plt.ylabel("Performance (%)")
    plt.legend()
    plt.grid()
    plt.show()
