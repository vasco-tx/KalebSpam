import requests
from pystyle import Colors, Colorate, Center
import time
import os 

os.system("cls" if os.name == "nt" else "clear")

red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
reset = "\033[0m"


def banner(): 
	logo = f"""

 _____ _____ __    _____ _____ 
|  |  |  _  |  |  |   __| __  |
|    -|     |  |__|   __| __ -|
|__|__|__|__|_____|_____|_____|

	  [Desenvolvido por Vascotx]
		"""

	options = f"""
		[{green}1{reset}] Enviar uma mensagem			[{green}4{reset}] Várias mensagens com webhook							
		[{green}2{reset}] Enviar várias mensagens     	[{green}5{reset}] Créditos
		[{green}3{reset}] Uma mensagem com webhook webhook	[{green}6{reset}] Servidor da Kaleb

	"""

	logo = Center.XCenter(logo)
	options = Center.XCenter(options)
	print(Colorate.Horizontal(Colors.green_to_white, logo, 1))
	print(options)


optl = f"""    

	 _____ _____ __    _____ _____ 
	|  |  |  _  |  |  |   __| __  |
	|    -|     |  |__|   __| __ -|                 
	|__|__|__|__|_____|_____|_____|
		"""
obs = f""" 
Bem vindo ao KalebSpammer.
Use {green}.config{reset} para mais informações.

"""
optl = Center.XCenter(optl)
print(Colorate.Horizontal(Colors.green_to_white, optl, 1))
print(Center.XCenter(obs))




chc = input(f"[{green}+{reset}] | >>> ")

if chc == ".config":
	usertoken = input(f"[{green}+{reset}] | Token da conta q vc vai usar [{green}>>>{reset}] ")
	chnid = int(input(f"[{green}+{reset}] | Id do canal [{green}>>>{reset}] "))
	os.system("cls" if os.name == "nt" else "clear")
	req_url = f"https://discord.com/api/v9/channels/{chnid}/messages"

	headers = {
		"Authorization": usertoken
	}

else:
	print(f"[{yellow}!{reset}] Usa .config pra configurar a porra da tool.")
	time.sleep(2)
	exit()


while True:
	os.system('clear' if os.name != 'nt' else 'cls')
	banner()
	chc = int(input(f"[{green}>>>{reset}] "))
	match chc:
		case 1:
			msg = input(f"[{green}Mensagem{reset}] >>> ")
			payload = {
			"content": msg
			}
			response = requests.post(req_url, payload, headers=headers)
			os.system('clear' if os.name != 'nt' else 'cls')
			if response.status_code == 200:
				print(f"[{green}+{reset}] | Mensagem enviada com sucesso")
			else:
				print(f"[{yellow}+{reset}] | -> {response.status_code}")
			time.sleep(2)

		case 2:
			msgf = input(f"[{green}Mensagem{reset}] >>> ")
			try:
				reps = int(input(f"[{green}Número de mensagens{reset}] >>> "))
			except ValueError:
				print(f"[{yellow}!{reset}] | O número de mensagens tem que ser um {red}número inteiro{reset}")
			payload = {
				"content": msgf
			}
			for i in range(reps):
				response = requests.post(req_url, payload, headers=headers)
				if response.status_code == 200:
					print(f"[{green}+{reset}] | Mensagem enviada com sucesso")
				else:
					print(f"[{yellow}+{reset}] | -> {response.status_code}")
				i = i + 1
			print(f"[{green}+{reset}] | Todas as mensagens foram enviadas.")
			time.sleep(3)

		case 3:
			webhook = input(f"[{green}Url da webhook{reset}] >>> ")
			msg = input(f"[{green}Mensagem{reset}] >>> ")
			data = {
			"content": msg
			}
			response = requests.post(webhook, json=data)
			if response.status_code == 200 or 204:
				print(f"[{green}+{reset}] | Mensagem enviada com sucesso")
			else:
				print(f"[{yellow}+{reset}] | -> {response.status_code}")
			time.sleep(3)

		case 4:
			webhook = input(f"[{green}Url da webhook{reset}] >>> ")
			msg = input(f"[{green}Mensagem{reset}] >>> ")
			try:
				reps = int(input(f"[{green}Número de mensagens{reset}] >>> "))
			except ValueError:
				print(f"[{yellow}!{reset}] | O número de mensagens tem que ser um {red}número inteiro{reset}")
			data = {
			"content": msg
			}
			for i in range(reps):
				response = requests.post(webhook, json=data)
				if response.status_code == 200 or 204:
					print(f"[{green}+{reset}] | Mensagem enviada com sucesso")
				else:
					print(f"[{yellow}+{reset}] | -> {response.status_code}")
			time.sleep(3)
			i = i + 1
		case 5:
			print(f"[{yellow}*{reset}] A ferramenta foi TOTALMENTE desenvolvida por Vascotx")
			print(f"[{yellow}*{reset}] A ferramenta foi desenvolvida com o apoio de Gwst4tx")
			input()
		case 6:
			print(f"[{yellow}!{reset}] Servidor da kaleb: {green}https://discord.gg/utrC3TV3Ww{reset}")
			input()

