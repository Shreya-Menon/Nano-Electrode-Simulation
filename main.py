from simulation import simulate_energy_density, simulate_degradation
from visualization import plot_energy_density, plot_degradation

def main():
    # Input parameters
    materials = ["graphene", "carbon_nanotube", "metal_oxide"]
    coating_thickness = 0.5  # in micrometers
    surface_area = 10.0  # in cm^2
    cycles = 100

    # Simulate energy densities
    energy_densities = []
    for material in materials:
        energy_density = simulate_energy_density(material, coating_thickness, surface_area)
        energy_densities.append(energy_density)

    # Plot energy density comparison
    plot_energy_density(materials, energy_densities)

    # Simulate degradation for each material and plot
    for material in materials:
        performances = simulate_degradation(material, cycles)
        plot_degradation(range(cycles), performances, material)

if __name__ == "__main__":
    main()
