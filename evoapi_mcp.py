#Path: evoapi_mcp\evoapi_mcp.py

from mcp.server.fastmcp import FastMCP
from group_controller import GroupController
from datetime import datetime
from send_sandeco import SendSandeco

# Inicializa o servidor FastMCP com nome "pong"
mcp = FastMCP("evoapi_mcp")


@mcp.tool(name="get_groups")
def get_groups() -> str:
    """
    Recupera e retorna uma lista formatada de grupos do WhatsApp disponíveis.

    Esta ferramenta permite ao agente obter os grupos cadastrados, exibindo
    informações relevantes como o ID do grupo e seu nome, em formato textual.
    A resposta pode ser usada para seleção posterior de um grupo para envio
    de mensagens.

    Returns:
        str: Lista de grupos no formato:
            "Grupo ID: <id>, Nome: <nome>\n"
    """
    controller = GroupController()
    groups = controller.fetch_groups()

    string_groups = ""
    for grupo in groups:
        string_groups += f"Grupo ID: {grupo.group_id}, Nome: {grupo.name}\n"

    return string_groups


@mcp.tool(name="get_group_messages")
def get_group_messages(group_id: str, start_date: str, end_date: str) -> str:
    """
    Recupera as mensagens enviadas em um grupo do WhatsApp dentro de um intervalo de datas especificado.

    Esta ferramenta permite ao agente acessar o histórico de conversas de um grupo,
    retornando as mensagens publicadas entre `start_date` e `end_date`, com detalhes 
    como remetente, horário, tipo da mensagem e conteúdo textual.

    Args:
        group_id (str): Identificador único do grupo do WhatsApp.
        start_date (str): Data e hora de início no formato 'YYYY-MM-DD HH:MM:SS'.
        end_date (str): Data e hora de término no formato 'YYYY-MM-DD HH:MM:SS'.

    Returns:
        str: Lista de mensagens formatadas, com os campos:
            - Usuário
            - Data e hora
            - Tipo da mensagem
            - Texto

        Cada mensagem é separada por um delimitador visual.
    """
    controller = GroupController()
    messages = controller.get_messages(group_id, start_date, end_date)
    
    messages_string = ""
    for message in messages:
        messages_string += f"Mensagem -----------------------------------\n"
        messages_string += f"Usuário: {message.push_name}\n"
        messages_string += f"Data e hora: {datetime.fromtimestamp(message.message_timestamp).strftime('%d/%m/%Y %H:%M:%S')}\n"
        messages_string += f"Tipo: {message.message_type}\n"
        messages_string += f"Texto: {message.get_text()}\n"

    return messages_string

def _send_message(recipient: str, message: str) -> str:
    """
    Método privado que encapsula a lógica comum de envio de mensagens.

    Args:
        recipient (str): ID do destinatário (grupo ou número de telefone)
        message (str): Conteúdo da mensagem

    Returns:
        str: Mensagem de sucesso ou erro
    """
    send = SendSandeco()
   
    send.textMessage(recipient, message)
    return "Mensagem enviada com sucesso"
   
   

@mcp.tool(name="send_message_to_group")
def send_message_to_group(group_id: str, message: str)->str:
    """
    Envia uma mensagem de texto para um grupo específico do WhatsApp.

    Esta ferramenta permite ao agente enviar mensagens para grupos do WhatsApp
    utilizando a API do WhatsApp. A mensagem será entregue ao grupo identificado
    pelo group_id fornecido.

    Args:
        group_id (str): Identificador único do grupo do WhatsApp no formato 
            'XXXXXXXXXXXXXXXXX@g.us'. Este ID pode ser obtido através da 
            ferramenta get_groups().
        message (str): Conteúdo da mensagem a ser enviada. Pode conter texto
            formatado, emojis e quebras de linha.

    Returns:
        str: Mensagem indicando o resultado da operação:
            - "Mensagem enviada com sucesso" em caso de êxito
            - "Erro ao enviar mensagem: <descrição>" em caso de falha

    Raises:
        Exception: Possíveis erros durante o envio da mensagem, como:
            - Grupo não encontrado
            - Problemas de conexão
            - Falha na autenticação
            - Formato inválido de mensagem
    """
    return _send_message(group_id, message)



@mcp.tool(name="send_message_to_phone")
def send_message_to_phone(cellphone: str, message: str)->str:
    """
    Envia uma mensagem de texto para um número de telefone específico via WhatsApp.
    Somente use para enviar mensagens para números de telefone 
    explicitamente. Caso contrario use a função send_message_to_group.
    Esta ferramenta permite ao agente enviar mensagens diretamente para números
    de telefone individuais utilizando a API do WhatsApp. A mensagem será entregue
    ao destinatário somente se o número estiver registrado no WhatsApp.

    Args:
        cellphone (str): Número do telefone no formato internacional, incluindo
            código do país e DDD, sem caracteres especiais. 
            se por acaso falta o 55, coloque 55 coloque o 55 na frente do numero.
            Mas o usuário tem que informa o DDD obrigatoriamente.
            Exemplo: '5511999999999' para um número de São Paulo, Brasil.
            
        message (str): Conteúdo da mensagem a ser enviada. Pode conter texto
            formatado, emojis e quebras de linha.

    Returns:
        str: Mensagem indicando o resultado da operação:
            - "Mensagem enviada com sucesso" em caso de êxito
            - "Erro ao enviar mensagem: <descrição>" em caso de falha

    Raises:
        Exception: Possíveis erros durante o envio da mensagem, como:
            - Número inválido ou mal formatado
            - Número não registrado no WhatsApp
            - Problemas de conexão
            - Falha na autenticação
            - Formato inválido de mensagem
    """
    return _send_message(cellphone, message)



if __name__ == "__main__":

    mcp.run(transport='stdio')
    #send_message_to_phone('5562981685163', 'teste')


    

