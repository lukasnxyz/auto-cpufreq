#!/usr/bin/env python3
from subprocess import PIPE, run
from auto_cpufreq.core import footer

from auto_cpufreq.battery_scripts.ideapad_acpi import ideapad_acpi_print_thresholds, ideapad_acpi_setup
from auto_cpufreq.battery_scripts.ideapad_laptop import ideapad_laptop_print_thresholds, ideapad_laptop_setup
from auto_cpufreq.battery_scripts.thinkpad import thinkpad_print_thresholds, thinkpad_setup, thinkpad_set_threshold_fullcharge

def lsmod(module): return module in run(['lsmod'], stdout=PIPE, stderr=PIPE, text=True, shell=True).stdout

def battery_get_thresholds():
    if lsmod("ideapad_acpi"): ideapad_acpi_print_thresholds()
    elif lsmod("ideapad_laptop"): ideapad_laptop_print_thresholds()
    elif lsmod("thinkpad_acpi"): thinkpad_print_thresholds()
    else: return

def battery_setup():
    if lsmod("ideapad_acpi"): ideapad_acpi_setup()
    elif lsmod("ideapad_laptop"): ideapad_laptop_setup()
    elif lsmod("thinkpad_acpi"): thinkpad_setup()
    else: return

def fullcharge_thresholds(config):
    if config.config_thresholds_are_set():
        if lsmod("thinkpad_acpi"): thinkpad_set_threshold_fullcharge()
        else: return
    else:
        print("ERROR:\n\nTo run auto-cpufreq, you must have default battery thresholds in your config enabled!")
        footer()
        exit(1)
