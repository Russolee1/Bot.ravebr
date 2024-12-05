import requests

# Lista de IDs de administradores permitidos
ADMIN_IDS = ["Russo_lee", "docinho06"]  # Substitua pelos IDs reais dos administradores

def is_admin(user_id):
    """
    Verifica se o usuário é um administrador.
    """
    return user_id in ADMIN_IDS

def follow_user(bot_id, user_id, bot_token):
    """
    Faz o bot seguir outro usuário no Highrise.
    """
    API_URL = "https://api.highrise.com/bots/{bot_id}/follow"  # URL da API do Highrise
    endpoint = API_URL.format(bot_id=bot_id)
    
    headers = {
        "Authorization": f"Bearer {bot_token}",
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

if __name__ == "__main__":
    # Substitua pelos valores reais do bot e configure as permissões
    BOT_ID = "seu_bot_id"
    BOT_TOKEN = "seu_token_do_bot"

    # Solicita o ID do usuário executando e o comando
    executor_id = input("Digite seu ID de administrador: ")
    if not is_admin(executor_id):
        print("Acesso negado: Você não tem permissão para executar este comando.")
        exit()

    # Solicita o comando e o ID do usuário a ser seguido
    command = input("Digite o comando (ex: follow <id_do_usuario>): ")
    parts = command.split()

    if len(parts) == 2 and parts[0].lower() == "follow":
        user_id_to_follow = parts[1]
        follow_user(BOT_ID, user_id_to_follow, BOT_TOKEN)
    else:
        print("Comando inválido! Use: follow <id_do_usuario>")