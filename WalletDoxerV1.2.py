import requests
import time
import sys  # to interact with terminal
from colorama import init, Fore  # for coloring things

init(autoreset=True)


# def spinner():
#     while True:
#         for cursor in '|/-\\':
#             yield cursor

def get_balance(address):
    try:
        url = f'https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance'
        response = requests.get(url)
        if response.status_code == 200:  # means if OK
            data = response.json()  # saves the response in json file

            # balance is in satoshis; We have to convert to BTC
            return {
                'balance': data['final_balance'] / 1e8,  # you know why did i used 1e8?
                'total_received': data['total_received'] / 1e8,
                'total_sent': data['total_sent'] / 1e8,
                'transactions': data['n_tx']
            }

        else:
            return None
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Error: {e}")


def main():
    banner = r"""
░█░█░█▀█░█░░░█░░░█▀▀░▀█▀░█▀▄░█▀█░█░█░█▀▀░█▀▄
░█▄█░█▀█░█░░░█░░░█▀▀░░█░░█░█░█░█░▄▀▄░█▀▀░█▀▄
░▀░▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀░░▀▀▀░▀░▀░▀▀▀░▀░▀  V 1.2
                                              By Mr. BILRED
 """
    print(Fore.CYAN + banner)
    print(Fore.GREEN + f"LET ME SEE HOW RICH YOU REALLY ARE!")
    print(Fore.LIGHTYELLOW_EX + f"No Illegal Purpose Intended. Using This Tool Makes Only You Liable For Your Actions")
    address = input(Fore.CYAN + "Enter Bitcoin wallet address: ")
    # spin = spinner()
    print(Fore.YELLOW + "Fetching balance ", end="")
    # for _ in range(1):
    #     sys.stdout.write(next(spin))
    #     sys.stdout.flush()
    #     time.sleep(0.1)
    #     sys.stdout.write('\b')

    info = get_balance(address)
    if info is not None:
        print(Fore.GREEN + f"\nWallet Info for {address}")
        print(Fore.CYAN + f"Current Balance    : {Fore.YELLOW}{info['balance']} BTC")
        print(Fore.CYAN + f"Total Sent         : {Fore.YELLOW}{info['total_sent']} BTC")
        print(Fore.CYAN + f"Total Received     : {Fore.YELLOW}{info['total_received']} BTC")
        print(Fore.CYAN + f"Total transactions : {Fore.YELLOW}{info['transactions']}")

    else:
        print(Fore.RED + "\nFailed to retrieve balance. Check the address man")


if __name__ == "__main__":
    main()
