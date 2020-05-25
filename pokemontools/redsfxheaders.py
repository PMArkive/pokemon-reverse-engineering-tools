#!/usr/bin/env python

rom = bytearray(open("baserom.gbc", "rb").read())

sfx_names_1 = [
	"Noise_Instrument01_1",
	"Noise_Instrument02_1",
	"Noise_Instrument03_1",
	"Noise_Instrument04_1",
	"Noise_Instrument05_1",
	"Noise_Instrument06_1",
	"Noise_Instrument07_1",
	"Noise_Instrument08_1",
	"Noise_Instrument09_1",
	"Noise_Instrument10_1",
	"Noise_Instrument11_1",
	"Noise_Instrument12_1",
	"Noise_Instrument13_1",
	"Noise_Instrument14_1",
	"Noise_Instrument15_1",
	"Noise_Instrument16_1",
	"Noise_Instrument17_1",
	"Noise_Instrument18_1",
	"Noise_Instrument19_1",
	"Cry00_1",
	"Cry01_1",
	"Cry02_1",
	"Cry03_1",
	"Cry04_1",
	"Cry05_1",
	"Cry06_1",
	"Cry07_1",
	"Cry08_1",
	"Cry09_1",
	"Cry0A_1",
	"Cry0B_1",
	"Cry0C_1",
	"Cry0D_1",
	"Cry0E_1",
	"Cry0F_1",
	"Cry10_1",
	"Cry11_1",
	"Cry12_1",
	"Cry13_1",
	"Cry14_1",
	"Cry15_1",
	"Cry16_1",
	"Cry17_1",
	"Cry18_1",
	"Cry19_1",
	"Cry1A_1",
	"Cry1B_1",
	"Cry1C_1",
	"Cry1D_1",
	"Cry1E_1",
	"Cry1F_1",
	"Cry20_1",
	"Cry21_1",
	"Cry22_1",
	"Cry23_1",
	"Cry24_1",
	"Cry25_1",
	"Get_Item1_1",
	"Get_Item2_1",
	"Tink_1",
	"Heal_HP_1",
	"Heal_Ailment_1",
	"Start_Menu_1",
	"Press_AB_1",
	"Pokedex_Rating_1",
	"Get_Key_Item_1",
	"Poisoned_1",
	"Trade_Machine_1",
	"Turn_On_PC_1",
	"Turn_Off_PC_1",
	"Enter_PC_1",
	"Shrink_1",
	"Switch_1",
	"Healing_Machine_1",
	"Teleport_Exit1_1",
	"Teleport_Enter1_1",
	"Teleport_Exit2_1",
	"Ledge_1",
	"Teleport_Enter2_1",
	"Fly_1",
	"Denied_1",
	"Arrow_Tiles_1",
	"Push_Boulder_1",
	"SS_Anne_Horn_1",
	"Withdraw_Deposit_1",
	"Cut_1",
	"Go_Inside_1",
	"Swap_1",
	"59_1",
	"Purchase_1",
	"Collision_1",
	"Go_Outside_1",
	"Save_1",
	"Pokeflute",
	"Safari_Zone_PA",
]

sfx_names_2 = [
	"Noise_Instrument01_2",
	"Noise_Instrument02_2",
	"Noise_Instrument03_2",
	"Noise_Instrument04_2",
	"Noise_Instrument05_2",
	"Noise_Instrument06_2",
	"Noise_Instrument07_2",
	"Noise_Instrument08_2",
	"Noise_Instrument09_2",
	"Noise_Instrument10_2",
	"Noise_Instrument11_2",
	"Noise_Instrument12_2",
	"Noise_Instrument13_2",
	"Noise_Instrument14_2",
	"Noise_Instrument15_2",
	"Noise_Instrument16_2",
	"Noise_Instrument17_2",
	"Noise_Instrument18_2",
	"Noise_Instrument19_2",
	"Cry00_2",
	"Cry01_2",
	"Cry02_2",
	"Cry03_2",
	"Cry04_2",
	"Cry05_2",
	"Cry06_2",
	"Cry07_2",
	"Cry08_2",
	"Cry09_2",
	"Cry0A_2",
	"Cry0B_2",
	"Cry0C_2",
	"Cry0D_2",
	"Cry0E_2",
	"Cry0F_2",
	"Cry10_2",
	"Cry11_2",
	"Cry12_2",
	"Cry13_2",
	"Cry14_2",
	"Cry15_2",
	"Cry16_2",
	"Cry17_2",
	"Cry18_2",
	"Cry19_2",
	"Cry1A_2",
	"Cry1B_2",
	"Cry1C_2",
	"Cry1D_2",
	"Cry1E_2",
	"Cry1F_2",
	"Cry20_2",
	"Cry21_2",
	"Cry22_2",
	"Cry23_2",
	"Cry24_2",
	"Cry25_2",
	"Level_Up",
	"Get_Item2_2",
	"Tink_2",
	"Heal_HP_2",
	"Heal_Ailment_2",
	"Start_Menu_2",
	"Press_AB_2",
	"Ball_Toss",
	"Ball_Poof",
	"Faint_Thud",
	"Run",
	"Dex_Page_Added",
	"Caught_Mon",
	"Peck",
	"Faint_Fall",
	"Battle_09",
	"Pound",
	"Battle_0B",
	"Battle_0C",
	"Battle_0D",
	"Battle_0E",
	"Battle_0F",
	"Damage",
	"Not_Very_Effective",
	"Battle_12",
	"Battle_13",
	"Battle_14",
	"Vine_Whip",
	"Battle_16",
	"Battle_17",
	"Battle_18",
	"Battle_19",
	"Super_Effective",
	"Battle_1B",
	"Battle_1C",
	"Doubleslap",
	"Battle_1E",
	"Horn_Drill",
	"Battle_20",
	"Battle_21",
	"Battle_22",
	"Battle_23",
	"Battle_24",
	"Battle_25",
	"Battle_26",
	"Battle_27",
	"Battle_28",
	"Battle_29",
	"Battle_2A",
	"Battle_2B",
	"Battle_2C",
	"Psybeam",
	"Battle_2E",
	"Battle_2F",
	"Psychic_M",
	"Battle_31",
	"Battle_32",
	"Battle_33",
	"Battle_34",
	"Battle_35",
	"Battle_36",
	"Silph_Scope",
]

sfx_names_3 = [
	"Noise_Instrument01_3",
	"Noise_Instrument02_3",
	"Noise_Instrument03_3",
	"Noise_Instrument04_3",
	"Noise_Instrument05_3",
	"Noise_Instrument06_3",
	"Noise_Instrument07_3",
	"Noise_Instrument08_3",
	"Noise_Instrument09_3",
	"Noise_Instrument10_3",
	"Noise_Instrument11_3",
	"Noise_Instrument12_3",
	"Noise_Instrument13_3",
	"Noise_Instrument14_3",
	"Noise_Instrument15_3",
	"Noise_Instrument16_3",
	"Noise_Instrument17_3",
	"Noise_Instrument18_3",
	"Noise_Instrument19_3",
	"Cry00_3",
	"Cry01_3",
	"Cry02_3",
	"Cry03_3",
	"Cry04_3",
	"Cry05_3",
	"Cry06_3",
	"Cry07_3",
	"Cry08_3",
	"Cry09_3",
	"Cry0A_3",
	"Cry0B_3",
	"Cry0C_3",
	"Cry0D_3",
	"Cry0E_3",
	"Cry0F_3",
	"Cry10_3",
	"Cry11_3",
	"Cry12_3",
	"Cry13_3",
	"Cry14_3",
	"Cry15_3",
	"Cry16_3",
	"Cry17_3",
	"Cry18_3",
	"Cry19_3",
	"Cry1A_3",
	"Cry1B_3",
	"Cry1C_3",
	"Cry1D_3",
	"Cry1E_3",
	"Cry1F_3",
	"Cry20_3",
	"Cry21_3",
	"Cry22_3",
	"Cry23_3",
	"Cry24_3",
	"Cry25_3",
	"Get_Item1_3",
	"Get_Item2_3",
	"Tink_3",
	"Heal_HP_3",
	"Heal_Ailment_3",
	"Start_Menu_3",
	"Press_AB_3",
	"Pokedex_Rating_3",
	"Get_Key_Item_3",
	"Poisoned_3",
	"Trade_Machine_3",
	"Turn_On_PC_3",
	"Turn_Off_PC_3",
	"Enter_PC_3",
	"Shrink_3",
	"Switch_3",
	"Healing_Machine_3",
	"Teleport_Exit1_3",
	"Teleport_Enter1_3",
	"Teleport_Exit2_3",
	"Ledge_3",
	"Teleport_Enter2_3",
	"Fly_3",
	"Denied_3",
	"Arrow_Tiles_3",
	"Push_Boulder_3",
	"SS_Anne_Horn_3",
	"Withdraw_Deposit_3",
	"Cut_3",
	"Go_Inside_3",
	"Swap_3",
	"59_3",
	"Purchase_3",
	"Collision_3",
	"Go_Outside_3",
	"Save_3",
	"Intro_Lunge",
	"Intro_Hip",
	"Intro_Hop",
	"Intro_Raise",
	"Intro_Crash",
	"Intro_Whoosh",
	"Slots_Stop_Wheel",
	"Slots_Reward",
	"Slots_New_Spin",
	"Shooting_Star",
]

sfx_names_4 = [
	"Noise_Instrument01_4",
	"Noise_Instrument02_4",
	"Noise_Instrument03_4",
	"Noise_Instrument04_4",
	"Noise_Instrument05_4",
	"Noise_Instrument06_4",
	"Noise_Instrument07_4",
	"Noise_Instrument08_4",
	"Noise_Instrument09_4",
	"Noise_Instrument10_4",
	"Noise_Instrument11_4",
	"Noise_Instrument12_4",
	"Noise_Instrument13_4",
	"Noise_Instrument14_4",
	"Noise_Instrument15_4",
	"Noise_Instrument16_4",
	"Noise_Instrument17_4",
	"Noise_Instrument18_4",
	"Noise_Instrument19_4",
	"Cry00_4",
	"Cry01_4",
	"Cry02_4",
	"Cry03_4",
	"Cry04_4",
	"Cry05_4",
	"Cry06_4",
	"Cry07_4",
	"Cry08_4",
	"Cry09_4",
	"Cry0A_4",
	"Cry0B_4",
	"Cry0C_4",
	"Cry0D_4",
	"Cry0E_4",
	"Cry0F_4",
	"Cry10_4",
	"Cry11_4",
	"Cry12_4",
	"Cry13_4",
	"Cry14_4",
	"Cry15_4",
	"Cry16_4",
	"Cry17_4",
	"Cry18_4",
	"Cry19_4",
	"Cry1A_4",
	"Cry1B_4",
	"Cry1C_4",
	"Cry1D_4",
	"Cry1E_4",
	"Cry1F_4",
	"Cry20_4",
	"Cry21_4",
	"Cry22_4",
	"Cry23_4",
	"Cry24_4",
	"Cry25_4",
	"Get_Item1_4",
	"Get_Item2_4",
	"Tink_4",
	"Heal_HP_4",
	"Heal_Ailment_4",
	"Start_Menu_4",
	"Press_AB_4",
	"Surfing_Jump",
	"Surfing_Flip",
	"Surfing_Crash",
	"Unknown_802cc",
	"Surfing_Land",
	"Get_Item2_4_2",
]

sfx_banks = [
	0x02,
	0x08,
	0x1f,
	# 0x20, # yellow only
]

sfx_groups = {
	0x02: sfx_names_1,
	0x08: sfx_names_2,
	0x1f: sfx_names_3,
	# 0x20: sfx_names_4, # yellow only
}

def dump_all_sfx_headers_in_bank(bank, sfx_names, path, i):
	file = open(path + "sfxheaders" + str(i) + ".asm", "w")
	file.write("SFX_Headers_{}::\n".format(i))
	file.write("\tdb $ff, $ff, $ff ; padding\n")
	address = bank * 0x4000 + 3
	for sfx_name in sfx_names:
		file.write("\nSFX_{}::\n".format(sfx_name))
		file.write("\taudio_header SFX_{}".format(sfx_name))
		num_channels = (rom[address] >> 6) + 1
		for channel in range(num_channels):
			file.write(", Ch{}".format(rom[address] % 0x10 + 1))
			address += 3
		file.write("\n")
	file.close()

def dump_all_sfx_headers(path):
	import os
	os.makedirs(path, exist_ok=True)
	for i, bank in enumerate(sfx_banks):
		dump_all_sfx_headers_in_bank(bank, sfx_groups[bank], path, i + 1)

if __name__ == "__main__":
	dump_all_sfx_headers("audio/headers/")
