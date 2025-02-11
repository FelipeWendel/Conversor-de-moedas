import requests

def get_exchange_rate(base_currency, target_currency):
    """
    Obtem a taxa de câmbio atualizada da API do ExchangeRate-API.

    Args:
        base_currency (str): Moeda base (ex: USD)
        target_currency (str): Moeda alvo (ex: BRL)

    Returns:
        float: Taxa de câmbio
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target_currency]

def convert_currency(base_currency, target_currency, amount):
    """
    Converte um valor de uma moeda para outra usando a taxa de câmbio atualizada.

    Args:
        base_currency (str): Moeda base (ex: USD)
        target_currency (str): Moeda alvo (ex: BRL)
        amount (float): Valor a ser convertido

    Returns:
        float: Valor convertido
    """
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    return amount * exchange_rate

def main():
    print("Conversor de Moedas")
    print("-------------------")

    base_currency = input("Digite a moeda base (ex: USD, BRL, EUR): ")
    target_currency = input("Digite a moeda alvo (ex: USD, BRL, EUR): ")

    while True:
        try:
            amount = float(input("Digite o valor a ser convertido: "))
            break
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    converted_amount = convert_currency(base_currency, target_currency, amount)
    print(f"{amount} {base_currency} é igual a {converted_amount} {target_currency}")

if __name__ == "__main__":
    main()