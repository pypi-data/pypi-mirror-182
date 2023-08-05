# Python standard libraries
import json
import numpy as np
import os

def calculate_heat_flux_round_wire(power, wire_radius, wire_distance):
    """
    :param power: losses in Watts
    :param radius: wire thickness in m
    """
    # Power density for volumes W/m^3
    #volume = 2 * np.pi**2 * wire_radius**2 * wire_position_x
    volume = 2 * np.pi**2 * wire_radius**2 * wire_distance

    return power/volume

def read_results_log(results_log_file_path):
    losses = {}
    if not os.path.exists(results_log_file_path):
        raise Exception(f"Losses file not found {results_log_file_path}.")
    with open(results_log_file_path, "r") as fd:
        content = json.loads(fd.read())
        losses = content["total_losses"]

    return losses