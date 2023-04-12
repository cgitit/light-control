import json

global data

def write_ip(data):
	with open('ip_list.cfg', "w") as outfile:
		json.dump(data, outfile)

def read_ip():
	with open('ip_list.cfg') as json_file:
		data = json.load(json_file)
		return data

def menu():
	print("1.) Clear IP Addresses \n"
	"2.) List Current Addresses \n"
	"3.) Set ALL IP Addresses \n"
	"4.) ADD IP Address \n"
	"5.) REMOVE IP Address \n"
	"6.) Sort IP's in order \n"
	"Q.) Return to Main Menu \n")

def add_IP():
	global IP
	print("Please enter the last three digits of ONE IP addresses. \n")
	print("Example: 192.168.1.100 Enter: 100 \n" )
	IP = input("IP Address: ")

def sub_setup():
	while True:
		data = read_ip()
		print("\nIP Settings")
		print("-------------")
		menu()
		selection = input('Option: ')
		if selection == "1":
			data['IP_LIST'] = []
			write_ip(data)
			read_ip()
			print(data['IP_LIST'])
		elif selection == "2":
			try:
				data = read_ip()
				if data['IP_LIST']:
					print(data['IP_LIST'])
				else:
					print("IP list is empty.")
			except:
				print("IP List is empty")
		elif selection == "3":
			data = {}
			data['IP_LIST'] = []
			write_ip(data)
			count = input("How many lights do your have: ")
			for each in range(int(count)):
				add_IP()
				if IP in data['IP_LIST']:
					print("Already in list")
				else:
					data['IP_LIST'].append(IP)
					write_ip(data)
			read_ip()
			print(data['IP_LIST'])
		elif selection == "4":
			added_ip = input("Please enter the last three digits of ONE IP address: ")
			try:
				read_ip()
				if added_ip in data['IP_LIST']:
					print("Already in list")
				else:
					data['IP_LIST'].append(added_ip)
					write_ip(data)
			except:
				print("ERROR")
				print("Try using option 3 first.")
			try:
				read_ip()
				print(data['IP_LIST'])
			except:
				print("Could not print IP list.. yet?")
		elif selection == "5":
			read_ip()
			print(data['IP_LIST'])
			x = input("Which IP would you like to remove: ")
			data['IP_LIST'].remove(x)
			write_ip(data)
			print(data['IP_LIST'])
		elif selection == "6":
			data['IP_LIST'].sort()
			write_ip(data)
			data = read_ip()
			print(data['IP_LIST'])
		elif selection == "Q" or selection == "q":
			break
		else:
			print("Error 1")

sub_setup()
