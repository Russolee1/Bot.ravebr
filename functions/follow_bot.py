from highrise.models import *
import asyncio
from asyncio import Task

async def follow_user(self: BaseBot, user: User, message: str) -> None:
    """
    Função principal para seguir outro usuário baseado no nickname.
    """
    async def following_loop(self: BaseBot, user: User, message: str) -> None:
        if message.startswith("/following_loop"):
            await self.highrise.chat("Comando inválido, use /follow <nickname>")
            return

        while True:
            # Obtém a lista de usuários na sala
            room_users = (await self.highrise.get_room_users()).content
            for room_user, position in room_users:
                if room_user.id == user.id:
                    user_position = position
                    break
            print(user_position)
            if type(user_position) != AnchorPosition:
                await self.highrise.walk_to(Position(user_position.x + 1, user_position.y, user_position.z))
            await asyncio.sleep(0.5)

    # Verifica se já existe uma tarefa para seguir alguém
    taskgroup = self.highrise.tg
    task_list = list(taskgroup._tasks)
    for task in task_list:
        if task.get_name() == "following_loop":
            await self.highrise.chat("Já estou seguindo alguém.")
            return

    # Cria a tarefa para seguir o usuário
    taskgroup.create_task(coro=following_loop(self, user, message))
    task_list: list[Task] = list(taskgroup._tasks)

    # Define o nome da tarefa para "following_loop"
    for task in task_list:
        if task.get_coro().__name__ == "following_loop":
            task.set_name("following_loop")
    await self.highrise.chat(f"Estou seguindo {user.username} 🚶‍♂️")


async def stop_following(self: BaseBot, user: User, message: str) -> None:
    """
    Função para parar de seguir o usuário.
    """
    taskgroup = self.highrise.tg
    task_list = list(taskgroup._tasks)
    
    for task in task_list:
        if task.get_name() == "following_loop":
            task.cancel()
            await self.highrise.chat(f"Parando de seguir {user.username}")
            return
    
    await self.highrise.chat("Não estou seguindo ninguém.")
    return


async def follow_by_nickname(self: BaseBot, message: str) -> None:
    """
    Função para buscar o ID do usuário pelo nickname e seguir.
    """
    nickname = message.split(" ")[1]  # Espera que o comando seja "/follow <nickname>"
    
    # Aqui você deve fazer uma consulta para obter o ID do usuário com base no nickname
    user = await self.highrise.get_user_by_nickname(nickname)  # Assumindo que essa função existe
    
    if user:
        await follow_user(self, user, message)
    else:
        await self.highrise.chat(f"Usuário com o nickname '{nickname}' não encontrado.")