import requests
import time
import sys  # to interact with terminal
from colorama import init, Fore # for coloring things

init(autoreset=True)

# def spinner():
#     while True:
#         for cursor in '|/-\\':
#             yield cursor

def get_balance(address):
    url = f'https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance'
    response = requests.get(url)
    if response.status_code == 200: # means if OK
        data = response.json()  # saves the response in json file

        # balance is in satoshis; We have to convert to BTC
        return data['balance'] / 1e8

    else:
        return None


def main():
    print(Fore.LIGHTYELLOW_EX + f"No Illegal Purpose Intended. Using This Tool Makes Only You Liable For Your Actions")
    address = input(Fore.CYAN + "Enter Bitcoin wallet address: ")
    # spin = spinner()
    print(Fore.YELLOW + "Fetching balance ", end="")
    # for _ in range(1):
    #     sys.stdout.write(next(spin))
    #     sys.stdout.flush()
    #     time.sleep(0.1)
    #     sys.stdout.write('\b')

    balance = get_balance(address)
    if balance is not None:
        print(Fore.GREEN + f"\nBalance for {address}: {balance} BTC")
    else:
        print(Fore.RED + "\nFailed to retrieve balance. Check the address man")

if __name__ == "__main__":
    main()
