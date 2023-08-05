import femmt as fmt
import numpy as np
import itertools



# prepare reluctance matrix combinations
def reluctance_matrix_goal_calculation(l_s_min_max_count_list, l_p_min_max_count_list, n_min_max_count_list,
                                       n_p_top_min_max_list, n_p_bot_min_max_list, n_s_top_min_max_list,
                                       n_s_bot_min_max_list):
    # inductance value and turns ratio
    l_s_list = np.linspace(l_s_min_max_count_list[0], l_s_min_max_count_list[1], l_s_min_max_count_list[2])
    l_p_list = np.linspace(l_p_min_max_count_list[0], l_p_min_max_count_list[1], l_p_min_max_count_list[2])
    n_list = np.linspace(n_min_max_count_list[0], n_min_max_count_list[1], n_min_max_count_list[2])

    # total turns
    n_p_top_list = np.arange(n_p_top_min_max_list[0], n_p_top_min_max_list[1] + 1)
    n_p_bot_list = np.arange(n_p_bot_min_max_list[0], n_p_bot_min_max_list[1] + 1)
    n_s_top_list = np.arange(n_s_top_min_max_list[0], n_s_top_min_max_list[1] + 1)
    n_s_bot_list = np.arange(n_s_bot_min_max_list[0], n_s_bot_min_max_list[1] + 1)

    reluctance_matrix_list = np.array([])
    results_dict_list = []

    for l_s, l_p, n, n_p_top, n_p_bot, n_s_top, n_s_bot in itertools.product(l_s_list, l_p_list, n_list, n_p_top_list, n_p_bot_list, n_s_top_list, n_s_bot_list):

        inductance_matrix = np.array([ [l_s + l_p, l_p / n], [l_p / n, l_p / n / n] ])
        winding_matrix = np.array([ [n_p_top, n_s_top], [n_p_bot, n_s_bot] ])
        reluctance_matrix = fmt.calculate_reluctances(winding_matrix, inductance_matrix)

        results_dict = {
            "l_s": l_s,
            "l_p": l_p,
            "n_p_top": n_p_top,
            "n_p_bot": n_p_bot,
            "n_s_top": n_s_top,
            "n_s_bot": n_s_bot,
            "inductance_matrix": inductance_matrix,
            "winding_matrix": winding_matrix,
            "reluctance_matrix": reluctance_matrix
        }

        results_dict_list.append(results_dict)
        reluctance_matrix_list = np.append(reluctance_matrix_list, reluctance_matrix)
    return results_dict_list, reluctance_matrix_list

def air_gap_placement_generator(air_gap_middle_leg_list, tablet_hight, window_h, sweep_distance_percent = 5):
    """
    This function places the air gap at different positions in the middle leg

    Note: this function is currently limited to two air gaps!!
    """
    if len(air_gap_middle_leg_list) != 2:
        raise NotImplementedError("air gap placement function only valid for two air gaps!")

    position_air_gap_percent_list_list = []
    lower_air_gap_percent_position_vector = np.arange(sweep_distance_percent, 100, sweep_distance_percent)
    for lower_air_gap_percent_position in lower_air_gap_percent_position_vector:
        upper_air_gap_position = lower_air_gap_percent_position * window_h + air_gap_middle_leg_list[0] / 2 + tablet_hight + air_gap_middle_leg_list[1] / 2
        upper_air_gap_percent_position = upper_air_gap_position / window_h

        position_air_gap_percent_list_list.append([lower_air_gap_percent_position, upper_air_gap_percent_position])
    return position_air_gap_percent_list_list

def core_geometry_generation(core_inner_diameter_min_max_count_list, window_w_min_max_count_list,
                             window_h_min_max_count_list, stray_path_air_gap_length_min_max_count_list,
                             mu_r_min_max_count_list, tablet_hight_min_max_count_list, air_gap_middle_leg_list_list,
                             n_p_top_min_max_list, n_p_bot_min_max_list, n_s_top_min_max_list, n_s_bot_min_max_list):

    core_inner_diameter_list = np.linspace(core_inner_diameter_min_max_count_list[0], core_inner_diameter_min_max_count_list[1], core_inner_diameter_min_max_count_list[2])
    window_w_list = np.linspace(window_w_min_max_count_list[0], window_w_min_max_count_list[1], window_w_min_max_count_list[2])
    window_h_list = np.linspace(window_h_min_max_count_list[0], window_h_min_max_count_list[1], window_h_min_max_count_list[2])
    stray_path_air_gap_length_list = np.linspace(stray_path_air_gap_length_min_max_count_list[0], stray_path_air_gap_length_min_max_count_list[1], stray_path_air_gap_length_min_max_count_list[2])
    mu_r_list = np.linspace(mu_r_min_max_count_list[0], mu_r_min_max_count_list[1], mu_r_min_max_count_list[2])

    tablet_hight_list = np.linspace(tablet_hight_min_max_count_list[0], tablet_hight_min_max_count_list[1],
                                    tablet_hight_min_max_count_list[2])

    # total turns
    n_p_top_list = np.arange(n_p_top_min_max_list[0], n_p_top_min_max_list[1] + 1)
    n_p_bot_list = np.arange(n_p_bot_min_max_list[0], n_p_bot_min_max_list[1] + 1)
    n_s_top_list = np.arange(n_s_top_min_max_list[0], n_s_top_min_max_list[1] + 1)
    n_s_bot_list = np.arange(n_s_bot_min_max_list[0], n_s_bot_min_max_list[1] + 1)

    # combinations
    combinations = len(core_inner_diameter_list) * len(window_w_list) * len(window_h_list) * len(stray_path_air_gap_length_list) * len(mu_r_list) * len(tablet_hight_list) * len(n_p_top_list) * len(n_p_bot_list) * len(n_s_top_list) * len(n_s_bot_list)
    print(f"Number of basic combinations: {combinations}")

    combination_dict_list = []
    # sweep through all parameter combinations
    count = 0
    for core_inner_diameter, window_w, window_h, stray_path_air_gap_length, mu_r, air_gap_middle_leg_list, tablet_hight, n_p_top, n_p_bot, n_s_top, n_s_bot in itertools.product(core_inner_diameter_list, window_w_list, window_h_list, stray_path_air_gap_length_list, mu_r_list, air_gap_middle_leg_list_list, tablet_hight_list, n_p_top_list, n_p_bot_list, n_s_top_list, n_s_bot_list):
        position_air_gap_percent_list_list = air_gap_placement_generator(air_gap_middle_leg_list, tablet_hight, window_h, sweep_distance_percent = 5)
        start_index = 0
        for position_air_gap_percent_list in position_air_gap_percent_list_list:
            # calculate dedicated reluctance parts of the core
            r_top, r_bot, r_stray = fmt.r_top_bot_stray(core_inner_diameter, air_gap_middle_leg_list, window_w, window_h, stray_path_air_gap_length, mu_r, start_index, position_air_gap_percent_list)

            # calculate matrix (reluctance, inductance, winding)
            reluctance_matrix = np.array([ [r_top + r_stray, -r_stray], [-r_stray, r_bot + r_stray] ])
            winding_matrix = np.array([ [n_p_top, n_s_top], [n_p_bot, n_s_bot] ])
            inductance_matrix = fmt.calculate_inductances(reluctance_matrix, winding_matrix)

            # summarize results
            if count == 0:
                reluctance_matrix_list = np.copy(reluctance_matrix)
                inductance_matrix_list = np.copy(inductance_matrix)
            elif count == 1:
                reluctance_matrix_list = np.append([reluctance_matrix_list], [reluctance_matrix], axis=0)
                inductance_matrix_list = np.append([inductance_matrix_list], [inductance_matrix], axis=0)
            else:
                reluctance_matrix_list = np.append(reluctance_matrix_list, [reluctance_matrix], axis=0)
                inductance_matrix_list = np.append(inductance_matrix_list, [inductance_matrix], axis=0)

            combination_dict = {
                "core_inner_diameter": core_inner_diameter,
                "window_w": window_w,
                "window_h": window_h,
                "stray_path_air_gap_length": stray_path_air_gap_length,
                "mu_r": mu_r,
                "air_gap_middle_leg_list": air_gap_middle_leg_list,
                "tablet_hight": tablet_hight,
                "reluctance_matrix": reluctance_matrix,
                "inductance_matrix": inductance_matrix
            }
        count += 1

    return combination_dict, reluctance_matrix_list, inductance_matrix_list


def air_gap_generator(total_air_gaps_min_max_list, total_air_gap_hight_min_max_count_list, sweep_distance = 0.01):
    """
    :param sweep_distance: air gap distance to sweep [0... 1],  0.01 = 1 percent.
    """

    air_gaps_list = np.arange(total_air_gaps_min_max_list[0], total_air_gaps_min_max_list[1] + 1)
    air_gap_hight_list = np.linspace(total_air_gap_hight_min_max_count_list[0], total_air_gap_hight_min_max_count_list[1], total_air_gap_hight_min_max_count_list[2])


    for total_air_gaps, total_air_gap_hight in itertools.product(air_gaps_list, air_gap_hight_list):
        air_gap_middle_leg_list_list = []
        if total_air_gaps == 2:
            for air_gap_1_factor in np.arange(sweep_distance, 1 - sweep_distance + sweep_distance, sweep_distance):
                air_gap_1 = air_gap_1_factor * total_air_gap_hight
                air_gap_2 = (1 - air_gap_1_factor) * total_air_gap_hight
                air_gap_middle_leg_list_list.append([air_gap_1, air_gap_2])
                if air_gap_2 < 0.9 * sweep_distance * total_air_gap_hight:
                    print(f"{air_gap_1_factor = }")
                    raise Exception("error in program code implementation")
        elif total_air_gaps == 3:
            for air_gap_1_factor in np.arange(sweep_distance, 1 - sweep_distance, sweep_distance):
                for air_gap_2_factor in np.arange(0.01, 1 - air_gap_1_factor - sweep_distance, sweep_distance):
                    air_gap_1 = air_gap_1_factor * total_air_gap_hight
                    air_gap_2 = air_gap_2_factor * total_air_gap_hight
                    air_gap_3 = total_air_gap_hight - air_gap_1 - air_gap_2
                    if air_gap_3 < 0.9 * sweep_distance * total_air_gap_hight:
                        print(f"{air_gap_1_factor = }")
                        print(f"{air_gap_2_factor = }")
                        raise Exception("error in program code implementation")
                    air_gap_middle_leg_list_list.append([air_gap_1, air_gap_2, air_gap_3])
        elif total_air_gaps == 4:
            for air_gap_1_factor in np.arange(sweep_distance, 1 - 2 * sweep_distance, sweep_distance):
                for air_gap_2_factor in np.arange(0.01, 1 - air_gap_1_factor - sweep_distance, sweep_distance):
                    for air_gap_3_factor in np.arange(0.01, 1 - air_gap_1_factor - air_gap_2_factor - sweep_distance, sweep_distance):
                        air_gap_1 = air_gap_1_factor * total_air_gap_hight
                        air_gap_2 = air_gap_2_factor * total_air_gap_hight
                        air_gap_3 = air_gap_3_factor * total_air_gap_hight
                        air_gap_4 = total_air_gap_hight - air_gap_1 - air_gap_2 - air_gap_3
                        if air_gap_4 < 0.9 * sweep_distance * total_air_gap_hight:
                            print(f"{air_gap_1_factor = }")
                            print(f"{air_gap_2_factor = }")
                            print(f"{air_gap_3_factor = }")
                            print(f"{air_gap_4 = }")
                            raise Exception("error in program code implementation")
                        air_gap_middle_leg_list_list.append([air_gap_1, air_gap_2, air_gap_3, air_gap_4])
        elif total_air_gaps == 5:
            for air_gap_1_factor in np.arange(sweep_distance, 1 - 2 * sweep_distance, sweep_distance):
                for air_gap_2_factor in np.arange(sweep_distance, 1 - air_gap_1_factor - sweep_distance, sweep_distance):
                    for air_gap_3_factor in np.arange(sweep_distance, 1 - air_gap_1_factor - air_gap_2_factor - sweep_distance, sweep_distance):
                        for air_gap_4_factor in np.arange(sweep_distance, 1 - air_gap_1_factor - air_gap_2_factor - air_gap_3_factor - sweep_distance, sweep_distance):
                            air_gap_1 = air_gap_1_factor * total_air_gap_hight
                            air_gap_2 = air_gap_2_factor * total_air_gap_hight
                            air_gap_3 = air_gap_3_factor * total_air_gap_hight
                            air_gap_4 = air_gap_4_factor * total_air_gap_hight
                            air_gap_5 = total_air_gap_hight - air_gap_1 - air_gap_2 - air_gap_3 - air_gap_4
                            if air_gap_5 < 0.9 * sweep_distance * total_air_gap_hight:
                                print(f"{air_gap_1_factor = }")
                                print(f"{air_gap_2_factor = }")
                                print(f"{air_gap_3_factor = }")
                                print(f"{air_gap_4_factor = }")
                                print(f"{air_gap_5 = }")
                                raise Exception("error in program code implementation")
                            air_gap_middle_leg_list_list.append([air_gap_1, air_gap_2, air_gap_3, air_gap_4])
        elif total_air_gaps > 5:
            raise NotImplementedError("air gaps > 5 are not supported for the reluctance model")
        else:
            raise Exception("total air gaps needs to be 2...5")
    return air_gap_middle_leg_list_list









if __name__ == "__main__":
    # primary concentrated equivalent circuit
    l_s = 85e-6
    l_s_percent = 10
    l_p_min = 100e-6
    n = 2.99

    n_p_top_min_max_list = [10, 12]
    n_p_bot_min_max_list = [30, 31]
    n_s_top_min_max_list = [50, 51]
    n_s_bot_min_max_list = [70, 71]

    total_air_gaps_min_max_list = [2,2]
    total_air_gap_hight_min_max_count_list = [0.0001, 0.0005, 5]
    tablet_hight_min_max_count_list = [0.005, 0.01, 5]

    # reluctance_matrix_allowed_combination_dict, reluctance_matrix_allowed_combination_list = reluctance_matrix_goal_calculation([l_s, l_s * 1.1, 2], [l_p_min, l_p_min, 1], [n, n, 1], n_p_top_min_max_list,
    #                                                                                                                             n_p_bot_min_max_list, n_s_top_min_max_list, n_s_bot_min_max_list)

    combinations = 3

    core_inner_diameter_min_max_count_list = [0.005, 0.03, combinations]
    window_w_min_max_count_list =  [0.01, 0.04, combinations]
    window_h_min_max_count_list = [0.03, 0.07, combinations]
    stray_path_air_gap_length_min_max_count_list = [0.0001, 0.0005, combinations]
    mu_r_min_max_count_list = [3000, 3000, combinations]

    air_gap_middle_leg_list_list = air_gap_generator(total_air_gaps_min_max_list, total_air_gap_hight_min_max_count_list, sweep_distance = 0.1)


    combination_dict, reluctance_matrix_list, inductance_matrix_list = core_geometry_generation(core_inner_diameter_min_max_count_list, window_w_min_max_count_list,
                            window_h_min_max_count_list, stray_path_air_gap_length_min_max_count_list,
                            mu_r_min_max_count_list, tablet_hight_min_max_count_list, air_gap_middle_leg_list_list,
                            n_p_top_min_max_list, n_p_bot_min_max_list, n_s_top_min_max_list, n_s_bot_min_max_list)

    print(f"{reluctance_matrix_list = }")
    print(f"{len(inductance_matrix_list) = }")

    # reluctance_matrix_real_allowed_combinations = np.array([])
    # for inductance_matrix in reluctance_matrix_list:
    #     #print(reluctance_matrix)
    #     l_s_geometry, l_p_geometry, n_geometry = fmt.calculate_ls_lh_n_from_inductance_matrix(inductance_matrix)
    #
    #     if l_s_geometry < l_s* 1.1 and l_s_geometry > 0.9 * l_s:
    #         print("ls found")
    #         if l_h_geometry > l_p_min:
    #             print("lp found")
    #             if n_geometry < n * 1.1 and n_geometry > n * 0.9:
    #                 print("n found")
    #                 reluctance_matrix_real_allowed_combinations = np.dstack(reluctance_matrix_real_allowed_combinations, inductance_matrix)
    # print(len(reluctance_matrix_real_allowed_combinations))







