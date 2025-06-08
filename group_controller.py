#Path: evoapi_mcp\group_controller.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# group_manager.py
from dotenv import load_dotenv
from datetime import datetime
from evolutionapi.client import EvolutionClient
from group import Group


from message_sandeco import MessageSandeco



# Carregar variáveis de ambiente
load_dotenv()


class GroupController:
    def __init__(self):
        """
        Inicializa o gerenciador de grupos para a API Evolution, carregando configurações do ambiente.
        """
        self.base_url = os.getenv("EVO_API_URL")
        self.api_token = os.getenv("EVO_API_TOKEN")
        self.instance_id = os.getenv("EVO_INSTANCE_NAME")
        self.instance_token = os.getenv("EVO_INSTANCE_TOKEN")
        
        paths_this = os.path.dirname(__file__)
        
        self.csv_file = os.path.join(paths_this,"group_summary.csv")

        if not all([self.base_url, self.api_token, self.instance_id, self.instance_token]):
            raise ValueError(
                "As variáveis de ambiente necessárias (EVO_API_URL, EVO_API_TOKEN, EVO_INSTANCE_NAME, EVO_INSTANCE_TOKEN) não estão configuradas corretamente."
            )

        self.client = EvolutionClient(base_url=self.base_url, api_token=self.api_token)
        self.groups = []



    def fetch_groups(self):
        """
        Busca todos os grupos da instância, atualiza a lista interna de grupos e carrega os dados de resumo.
        """

        # Busca os grupos da API
        groups_data = self.client.group.fetch_all_groups(
            instance_id=self.instance_id,
            instance_token=self.instance_token,
            get_participants=False
        )

        # Atualiza a lista de grupos com objetos `Group`
        self.groups = []
        for group in groups_data:
            # Dados básicos do grupo
            group_id = group["id"]


            # Criação do objeto Group (apenas name e id)
            self.groups.append(
                Group(
                    group_id=group_id,
                    name=group.get("subject", "Sem nome"),
                    subject_owner="",
                    subject_time=0,
                    picture_url=None,
                    size=0,
                    creation=0,
                    owner="",
                    restrict=False,
                    announce=False,
                    is_community=False,
                    is_community_announce=False,
                )
            )
            
        return self.groups


    def get_groups(self):
        """
        Retorna a lista de grupos.

        :return: Lista de objetos `Group`.
        """
        return self.groups

    def find_group_by_id(self, group_id):
        """
        Encontra um grupo pelo ID.

        :param group_id: ID do grupo a ser encontrado.
        :return: Objeto `Group` correspondente ou `None` se não encontrado.
        """
        
        if not self.groups:
            self.groups = self.fetch_groups()
        
        for group in self.groups:
            if group.group_id == group_id:
                return group
        return None

    def filter_groups_by_owner(self, owner):
        """
        Filtra grupos pelo proprietário.

        :param owner: ID do proprietário.
        :return: Lista de grupos que pertencem ao proprietário especificado.
        """
        return [group for group in self.groups if group.owner == owner]
    
    

    def get_messages(self, group_id, start_date, end_date):
        # Convertendo as datas para o formato ISO 8601 com T e Z
        def to_iso8601(date_str):
            # Parseando a data no formato 'YYYY-MM-DD HH:MM:SS'
            dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            # Convertendo para o formato ISO 8601 com Z
            return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

        # Ajustando os parâmetros de data
        timestamp_start = to_iso8601(start_date)
        timestamp_end = to_iso8601(end_date)

        # Buscando as mensagens do grupo
        group_mensagens = self.client.chat.get_messages(
            instance_id=self.instance_id,
            remote_jid=group_id,
            instance_token=self.instance_token,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
            page=1,
            offset=1000
        )
        
        msgs = MessageSandeco.get_messages(group_mensagens)
        
        data_obj = datetime.strptime(timestamp_start, "%Y-%m-%dT%H:%M:%SZ")
        # Obter o timestamp
        timestamp_limite = int(data_obj.timestamp())
        
        msgs_filtradas = []
        for msg in msgs:
            if msg.message_timestamp >= timestamp_limite:
                msgs_filtradas.append(msg)

        
        return msgs_filtradas
        
        
          
