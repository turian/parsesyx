#!/usr/bin/env python3

import json

old_to_new_mapping = {
    # Global Parameters
    "ALG": "algorithm",
    "FB": "feedback",
    "LFS": "lfo_speed",
    "LFD": "lfo_delay",
    "LPMD": "lfo_pm_depth",
    "LAMD": "lfo_am_depth",
    "LPMS": "p_mode_sens",
    "LFW": "lfo_wave",
    "LKS": "lfo_key_sync",
    "TRNSP": "transpose",
    "PR1": "pitch_eg_rate_1",
    "PR2": "pitch_eg_rate_2",
    "PR3": "pitch_eg_rate_3",
    "PR4": "pitch_eg_rate_4",
    "PL1": "pitch_eg_level_1",
    "PL2": "pitch_eg_level_2",
    "PL3": "pitch_eg_level_3",
    "PL4": "pitch_eg_level_4",
    "NAME CHAR 1": "program",  # With specific handling for character positions
    "NAME CHAR 2": "program",  # With specific handling for character positions
    "NAME CHAR 3": "program",  # With specific handling for character positions
    "NAME CHAR 4": "program",  # With specific handling for character positions
    "NAME CHAR 5": "program",  # With specific handling for character positions
    "NAME CHAR 6": "program",  # With specific handling for character positions
    "NAME CHAR 7": "program",  # With specific handling for character positions
    "NAME CHAR 8": "program",  # With specific handling for character positions
    "NAME CHAR 9": "program",  # With specific handling for character positions
    "NAME CHAR 10": "program",  # With specific handling for character positions
    # Operator-Specific Parameters
    # Replace `x_` with `op1_` to `op6_` depending on the operator number.
    "0_R1": "op1_eg_rate_1",
    "0_R2": "op1_eg_rate_2",
    "0_R3": "op1_eg_rate_3",
    "0_R4": "op1_eg_rate_4",
    "0_L1": "op1_eg_level_1",
    "0_L2": "op1_eg_level_2",
    "0_L3": "op1_eg_level_3",
    "0_L4": "op1_eg_level_4",
    "0_BP": "op1_break_point",
    "0_LD": "op1_l_scale_depth",
    "0_RD": "op1_r_scale_depth",
    "0_RC": "op1_r_key_scale",
    "0_LC": "op1_l_key_scale",
    "0_DET": "op1_osc_detune",
    "0_RS": "op1_rate_scaling",
    "0_KVS": "op1_key_velocity",
    "0_AMS": "op1_a_mod_sens",
    "0_OL": "op1_output_level",
    "0_FC": "op1_f_coarse",
    "0_M": "op1_mode",
    "0_FF": "op1_f_fine",
    "1_R1": "op2_eg_rate_1",
    "1_R2": "op2_eg_rate_2",
    "1_R3": "op2_eg_rate_3",
    "1_R4": "op2_eg_rate_4",
    "1_L1": "op2_eg_level_1",
    "1_L2": "op2_eg_level_2",
    "1_L3": "op2_eg_level_3",
    "1_L4": "op2_eg_level_4",
    "1_BP": "op2_break_point",
    "1_LD": "op2_l_scale_depth",
    "1_RD": "op2_r_scale_depth",
    "1_RC": "op2_r_key_scale",
    "1_LC": "op2_l_key_scale",
    "1_DET": "op2_osc_detune",
    "1_RS": "op2_rate_scaling",
    "1_KVS": "op2_key_velocity",
    "1_AMS": "op2_a_mod_sens",
    "1_OL": "op2_output_level",
    "1_FC": "op2_f_coarse",
    "1_M": "op2_mode",
    "1_FF": "op2_f_fine",
    "2_R1": "op3_eg_rate_1",
    "2_R2": "op3_eg_rate_2",
    "2_R3": "op3_eg_rate_3",
    "2_R4": "op3_eg_rate_4",
    "2_L1": "op3_eg_level_1",
    "2_L2": "op3_eg_level_2",
    "2_L3": "op3_eg_level_3",
    "2_L4": "op3_eg_level_4",
    "2_BP": "op3_break_point",
    "2_LD": "op3_l_scale_depth",
    "2_RD": "op3_r_scale_depth",
    "2_RC": "op3_r_key_scale",
    "2_LC": "op3_l_key_scale",
    "2_DET": "op3_osc_detune",
    "2_RS": "op3_rate_scaling",
    "2_KVS": "op3_key_velocity",
    "2_AMS": "op3_a_mod_sens",
    "2_OL": "op3_output_level",
    "2_FC": "op3_f_coarse",
    "2_M": "op3_mode",
    "2_FF": "op3_f_fine",
    "3_R1": "op4_eg_rate_1",
    "3_R2": "op4_eg_rate_2",
    "3_R3": "op4_eg_rate_3",
    "3_R4": "op4_eg_rate_4",
    "3_L1": "op4_eg_level_1",
    "3_L2": "op4_eg_level_2",
    "3_L3": "op4_eg_level_3",
    "3_L4": "op4_eg_level_4",
    "3_BP": "op4_break_point",
    "3_LD": "op4_l_scale_depth",
    "3_RD": "op4_r_scale_depth",
    "3_RC": "op4_r_key_scale",
    "3_LC": "op4_l_key_scale",
    "3_DET": "op4_osc_detune",
    "3_RS": "op4_rate_scaling",
    "3_KVS": "op4_key_velocity",
    "3_AMS": "op4_a_mod_sens",
    "3_OL": "op4_output_level",
    "3_FC": "op4_f_coarse",
    "3_M": "op4_mode",
    "3_FF": "op4_f_fine",
    "4_R1": "op5_eg_rate_1",
    "4_R2": "op5_eg_rate_2",
    "4_R3": "op5_eg_rate_3",
    "4_R4": "op5_eg_rate_4",
    "4_L1": "op5_eg_level_1",
    "4_L2": "op5_eg_level_2",
    "4_L3": "op5_eg_level_3",
    "4_L4": "op5_eg_level_4",
    "4_BP": "op5_break_point",
    "4_LD": "op5_l_scale_depth",
    "4_RD": "op5_r_scale_depth",
    "4_RC": "op5_r_key_scale",
    "4_LC": "op5_l_key_scale",
    "4_DET": "op5_osc_detune",
    "4_RS": "op5_rate_scaling",
    "4_KVS": "op5_key_velocity",
    "4_AMS": "op5_a_mod_sens",
    "4_OL": "op5_output_level",
    "4_FC": "op5_f_coarse",
    "4_M": "op5_mode",
    "4_FF": "op5_f_fine",
    "5_R1": "op6_eg_rate_1",
    "5_R2": "op6_eg_rate_2",
    "5_R3": "op6_eg_rate_3",
    "5_R4": "op6_eg_rate_4",
    "5_L1": "op6_eg_level_1",
    "5_L2": "op6_eg_level_2",
    "5_L3": "op6_eg_level_3",
    "5_L4": "op6_eg_level_4",
    "5_BP": "op6_break_point",
    "5_LD": "op6_l_scale_depth",
    "5_RD": "op6_r_scale_depth",
    "5_RC": "op6_r_key_scale",
    "5_LC": "op6_l_key_scale",
    "5_DET": "op6_osc_detune",
    "5_RS": "op6_rate_scaling",
    "5_KVS": "op6_key_velocity",
    "5_AMS": "op6_a_mod_sens",
    "5_OL": "op6_output_level",
    "5_FC": "op6_f_coarse",
    "5_M": "op6_mode",
    "5_FF": "op6_f_fine",
    "OKS": "osc_key_sync",
}

assert sorted(list(set(old_to_new_mapping.keys()))) == sorted(
    list(old_to_new_mapping.keys())
)
assert sorted(
    [v for v in list(set(old_to_new_mapping.values())) if v != "program"]
) == sorted([v for v in list(set(old_to_new_mapping.values())) if v != "program"])


old_obj = json.loads(open("main.json").readline())
new_obj = json.load(open("01f8ce55dd814c46604a46623728054e35478fb7.json"))

for k in old_obj:
    if k not in old_to_new_mapping:
        print(k)

for k in old_to_new_mapping:
    if k not in old_obj:
        print(k)

for k in new_obj:
    if k not in old_to_new_mapping.values():
        print(k)

for k in old_to_new_mapping:
    if k not in old_obj:
        print(k)
