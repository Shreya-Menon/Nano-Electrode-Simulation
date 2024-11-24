import numpy as np

def simulate_energy_density(material, coating_thickness, surface_area):
    """
    Simulate the energy density of a battery based on material properties.
    
    Parameters:
    - material: str, type of nanomaterial (e.g., graphene, CNT)
    - coating_thickness: float, thickness of the nano-coating in micrometers
    - surface_area: float, electrode surface area in cm^2

    Returns:
    - energy_density: float, calculated energy density in Wh/kg
    """
    # Material properties (in hypothetical units)
    properties = {
        "graphene": {"conductivity": 5.9, "efficiency_factor": 0.8},
        "carbon_nanotube": {"conductivity": 4.8, "efficiency_factor": 0.75},
        "metal_oxide": {"conductivity": 3.2, "efficiency_factor": 0.65}
    }
    
    if material not in properties:
        raise ValueError("Material not supported! Choose from graphene, carbon_nanotube, metal_oxide.")
    
    # Extract properties
    conductivity = properties[material]["conductivity"]
    efficiency_factor = properties[material]["efficiency_factor"]
    
    # Formula to calculate energy density (hypothetical)
    energy_density = conductivity * surface_area * efficiency_factor / coating_thickness
    return energy_density

def simulate_degradation(material, cycles):
    """
    Simulate electrode degradation over charging cycles.
    
    Parameters:
    - material: str, type of nanomaterial
    - cycles: int, number of charge/discharge cycles

    Returns:
    - degradation: list of performance over cycles
    """
    degradation_rates = {
        "graphene": 0.001,  # degradation rate per cycle
        "carbon_nanotube": 0.002,
        "metal_oxide": 0.003
    }
    
    if material not in degradation_rates:
        raise ValueError("Material not supported!")
    
    degradation_rate = degradation_rates[material]
    performance = [100 - degradation_rate * i for i in range(cycles)]
    return performance
