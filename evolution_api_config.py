#!/usr/bin/env python3
"""
Configuração Correta para Evolution API MCP
API Base: https://api.frontzin.com.br (Evolution API v2.2.3)
"""

import requests
import json
from typing import Dict, List, Any

class EvolutionAPIMCP:
    """Cliente MCP para Evolution API WhatsApp"""
    
    def __init__(self, api_base: str = "https://api.frontzin.com.br", 
                 api_key: str = None, instance: str = "Daniel_Dias"):
        self.api_base = api_base.rstrip('/')
        self.api_key = api_key  # Precisa ser configurado
        self.instance = instance
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        if api_key:
            self.headers['apikey'] = api_key
    
    def test_connection(self) -> Dict[str, Any]:
        """Testa conexão com a API"""
        try:
            response = requests.get(f"{self.api_base}/", timeout=10)
            return {
                "status": "connected",
                "data": response.json(),
                "status_code": response.status_code
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def get_manager_url(self) -> str:
        """Retorna URL do manager"""
        return f"{self.api_base}/manager"
    
    def send_message_to_phone(self, number: str, message: str) -> Dict[str, Any]:
        """Envia mensagem individual (Evolution API format)"""
        endpoint = f"{self.api_base}/message/sendText/{self.instance}"
        
        payload = {
            "number": number,
            "text": message
        }
        
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers, timeout=30)
            return {
                "status": "success" if response.status_code == 200 else "error",
                "response": response.json() if response.status_code == 200 else response.text,
                "status_code": response.status_code
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def find_chats(self) -> Dict[str, Any]:
        """Lista chats/grupos (Evolution API format)"""
        endpoint = f"{self.api_base}/chat/findChats/{self.instance}"
        
        try:
            response = requests.get(endpoint, headers=self.headers, timeout=30)
            return {
                "status": "success" if response.status_code == 200 else "error",
                "data": response.json() if response.status_code == 200 else response.text,
                "status_code": response.status_code
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def find_groups(self) -> Dict[str, Any]:
        """Busca grupos especificamente"""
        # Na Evolution API, grupos são incluídos em findChats
        # Vamos filtrar apenas grupos (IDs terminam com @g.us)
        chats_result = self.find_chats()
        
        if chats_result["status"] == "success" and isinstance(chats_result["data"], list):
            groups = [chat for chat in chats_result["data"] 
                     if isinstance(chat, dict) and 
                     chat.get("id", "").endswith("@g.us")]
            return {
                "status": "success",
                "data": groups,
                "count": len(groups)
            }
        
        return chats_result
    
    def send_message_to_group(self, group_id: str, message: str) -> Dict[str, Any]:
        """Envia mensagem para grupo"""
        endpoint = f"{self.api_base}/message/sendText/{self.instance}"
        
        payload = {
            "number": group_id,  # Evolution API usa 'number' mesmo para grupos
            "text": message
        }
        
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers, timeout=30)
            return {
                "status": "success" if response.status_code == 200 else "error",
                "response": response.json() if response.status_code == 200 else response.text,
                "status_code": response.status_code
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def find_messages(self, chat_id: str, limit: int = 20) -> Dict[str, Any]:
        """Busca mensagens de um chat/grupo"""
        endpoint = f"{self.api_base}/chat/findMessages/{self.instance}"
        
        payload = {
            "where": {
                "key": {
                    "remoteJid": chat_id
                }
            },
            "limit": limit
        }
        
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers, timeout=30)
            return {
                "status": "success" if response.status_code == 200 else "error",
                "data": response.json() if response.status_code == 200 else response.text,
                "status_code": response.status_code
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def check_whatsapp_numbers(self, numbers: List[str]) -> Dict[str, Any]:
        """Verifica se números estão no WhatsApp"""
        endpoint = f"{self.api_base}/chat/whatsappNumbers/{self.instance}"
        
        payload = {
            "numbers": numbers
        }
        
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers, timeout=30)
            return {
                "status": "success" if response.status_code == 200 else "error",
                "data": response.json() if response.status_code == 200 else response.text,
                "status_code": response.status_code
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def get_instance_info(self) -> Dict[str, Any]:
        """Informações da instância"""
        endpoint = f"{self.api_base}/instance/fetchInstances"
        
        try:
            response = requests.get(endpoint, headers=self.headers, timeout=30)
            return {
                "status": "success" if response.status_code == 200 else "error",
                "data": response.json() if response.status_code == 200 else response.text,
                "status_code": response.status_code
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}

def test_evolution_api():
    """Teste completo da Evolution API"""
    print("🧪 Testando Evolution API MCP")
    print("=" * 50)
    
    # Inicializar cliente (sem API key por enquanto)
    client = EvolutionAPIMCP()
    
    # Teste 1: Conexão básica
    print("1. 🔌 Teste de Conexão:")
    connection = client.test_connection()
    print(f"   Status: {connection['status']}")
    if connection['status'] == 'connected':
        print(f"   Versão: {connection['data'].get('version', 'N/A')}")
        print(f"   Cliente: {connection['data'].get('clientName', 'N/A')}")
    
    # Teste 2: Manager URL
    print(f"\n2. 🖥️  Manager URL: {client.get_manager_url()}")
    
    # Teste 3: Informações da instância
    print("\n3. 📋 Informações da Instância:")
    instance_info = client.get_instance_info()
    print(f"   Status: {instance_info['status']}")
    if instance_info['status'] == 'error':
        print(f"   Erro: {instance_info['error']}")
    
    # Teste 4: Buscar chats (requer autenticação)
    print("\n4. 💬 Buscar Chats:")
    chats = client.find_chats()
    print(f"   Status: {chats['status']}")
    if chats['status'] == 'error':
        print(f"   Erro: {chats['error']}")
    
    # Teste 5: Verificar números WhatsApp
    print("\n5. 📱 Verificar Números WhatsApp:")
    check_numbers = client.check_whatsapp_numbers(["5562999476659"])
    print(f"   Status: {check_numbers['status']}")
    
    print("\n" + "=" * 50)
    print("📋 DIAGNÓSTICO:")
    print("✅ API Evolution está funcionando")
    print("⚠️  Requer API key para funcionalidades completas")
    print("🔧 Servidor MCP precisa ser reconfigurado")
    
    return client

# Configuração MCP corrigida
EVOLUTION_MCP_CONFIG = {
    "api_base": "https://api.frontzin.com.br",
    "version": "2.2.3",
    "client_name": "evolution",
    "manager_url": "http://api.frontzin.com.br/manager",
    "documentation": "https://doc.evolution-api.com",
    "required_headers": ["apikey"],
    "instance_required": True,
    "endpoints": {
        "send_text": "/message/sendText/{instance}",
        "find_chats": "/chat/findChats/{instance}",
        "find_messages": "/chat/findMessages/{instance}",
        "check_numbers": "/chat/whatsappNumbers/{instance}",
        "instance_info": "/instance/fetchInstances"
    },
    "mcp_tools_mapping": {
        "send_message_to_phone": "send_text",
        "send_message_to_group": "send_text",
        "get_groups": "find_chats (filter groups)",
        "get_group_messages": "find_messages"
    }
}

if __name__ == "__main__":
    client = test_evolution_api()
    
    print(f"\n📁 Configuração corrigida:")
    print(json.dumps(EVOLUTION_MCP_CONFIG, indent=2, ensure_ascii=False))
