import requests

# Substitua pelos valores reais da API
API_URL = "https://api.highrise.com"  # URL da API do Highrise
BOT_TOKEN = "seu_token_do_bot_aqui"  # Token de autenticação do bot

def follow_user(bot_id, user_id):
    """
    Faz o bot seguir outro usuário no Highrise.
    """
    endpoint = f"{API_URL}/bots/{bot_id}/follow"
    headers = {
        "Authorization": f"Bearer {BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "target_user_id": user_id
    }
    
    response = requests.post(endpoint, json=data, headers=headers)
    
    if response.status_code == 200:
        print(f"Bot começou a seguir o usuário {user_id} com sucesso!")
    else:
        print(f"Erro ao tentar seguir o usuário: {response.status_code} - {response.text}")

# IDs do bot e do usuário alvo
bot_id = "id_do_seu_bot_aqui"
user_id = "id_do_usuario_a_seguir"

# Faz o bot seguir o usuário
follow_user(bot_id, user_id)