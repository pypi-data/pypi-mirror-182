working_directory = '/home/nikolasf/Downloads/2022-11-20_simulation_femmt'
if not os.path.exists(working_directory):
    os.mkdir(working_directory)

file = os.path.join("/home/nikolasf/Downloads/2022-11-20_simulation_femmt/fem_simulation_data/case505.json")

geo = fmt.MagneticComponent.decode_settings_from_log(file, working_directory)

geo.create_model(freq=100000, visualize_before=True, save_png=False)

geo.single_simulation(freq=100000, current=[8], show_results=True)