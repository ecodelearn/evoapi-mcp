#!/usr/bin/env python3
"""
Configuração Corrigida para Servidor MCP WhatsApp
API Base: https://api.frontzin.com.br
"""

import requests
import json
from typing import Dict, List, Any
from datetime import datetime

class WhatsAppMCPClient:
    """Cliente MCP para WhatsApp usando API externa"""
    
    def __init__(self, api_base_url: str = "https://api.frontzin.com.br"):
        self.api_base = api_base_url.rstrip('/')
        self.user_id = "Daniel_Dias"  # Ajustar conforme necessário
        
    def send_message_to_phone(self, cellphone: str, message: str) -> Dict[str, Any]:
        """Envia mensagem para número individual"""
        endpoint = f"{self.api_base}/message/sendText"
        
        # Garantir formato correto do número (55 + DDD + número)
        if not cellphone.startswith('55'):
            if len(cellphone) == 11:  # DDD + número
                cellphone = f"55{cellphone}"
            elif len(cellphone) == 10:  # DDD sem 9 + número
                ddd = cellphone[:2]
                numero = cellphone[2:]
                cellphone = f"55{ddd}9{numero}"
        
        payload = {
            "number": cellphone,
            "text": message
        }
        
        try:
            response = requests.post(endpoint, json=payload, timeout=30)
            return {
                "status": "success" if response.status_code == 200 else "error",
                "response": response.json() if response.status_code == 200 else response.text,
                "status_code": response.status_code
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def get_groups(self) -> List[Dict[str, Any]]:
        """Lista grupos disponíveis"""
        endpoint = f"{self.api_base}/group/fetchAllGroups/{self.user_id}"
        
        try:
            response = requests.get(endpoint, params={"getParticipants": "false"}, timeout=30)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"HTTP {response.status_code}: {response.text}"}
        except Exception as e:
            return {"error": str(e)}
    
    def get_group_messages(self, group_id: str, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        """Recupera mensagens de um grupo"""
        endpoint = f"{self.api_base}/group/messages/{group_id}"
        
        params = {
            "start_date": start_date,
            "end_date": end_date
        }
        
        try:
            response = requests.get(endpoint, params=params, timeout=30)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"HTTP {response.status_code}: {response.text}"}
        except Exception as e:
            return {"error": str(e)}
    
    def send_message_to_group(self, group_id: str, message: str) -> Dict[str, Any]:
        """Envia mensagem para grupo"""
        endpoint = f"{self.api_base}/group/sendMessage"
        
        payload = {
            "group_id": group_id,
            "message": message
        }
        
        try:
            response = requests.post(endpoint, json=payload, timeout=30)
            return {
                "status": "success" if response.status_code == 200 else "error",
                "response": response.json() if response.status_code == 200 else response.text,
                "status_code": response.status_code
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def test_api_connection(self) -> Dict[str, Any]:
        """Testa conectividade com a API"""
        try:
            response = requests.get(f"{self.api_base}/health", timeout=10)
            return {
                "status": "connected",
                "api_base": self.api_base,
                "response_time": response.elapsed.total_seconds(),
                "status_code": response.status_code
            }
        except Exception as e:
            return {
                "status": "disconnected",
                "api_base": self.api_base,
                "error": str(e)
            }

def test_whatsapp_mcp():
    """Função de teste completa"""
    print("🚀 Testando WhatsApp MCP com API Externa")
    print("="*50)
    
    client = WhatsAppMCPClient()
    
    # Teste de conectividade
    print("🔌 Testando conectividade...")
    connection = client.test_api_connection()
    print(f"Status: {connection['status']}")
    
    # Teste de envio individual
    print("\n📱 Testando envio individual...")
    phone_result = client.send_message_to_phone(
        "5562999476659", 
        "🧪 Teste via Python MCP Client\n✅ API Externa funcionando!"
    )
    print(f"Resultado: {phone_result['status']}")
    
    # Teste de grupos
    print("\n👥 Testando listagem de grupos...")
    groups = client.get_groups()
    if isinstance(groups, list):
        print(f"Encontrados {len(groups)} grupos")
    else:
        print(f"Erro: {groups.get('error', 'Erro desconhecido')}")
    
    print("\n" + "="*50)
    print("✅ Teste concluído!")

# Configuração para servidor MCP
MCP_CONFIG = {
    "whatsapp": {
        "api_base_url": "https://api.frontzin.com.br",
        "user_id": "Daniel_Dias",
        "timeout": 30,
        "endpoints": {
            "send_individual": "/message/sendText",
            "send_group": "/group/sendMessage", 
            "get_groups": "/group/fetchAllGroups/{user_id}",
            "get_messages": "/group/messages/{group_id}",
            "health_check": "/health"
        }
    }
}

if __name__ == "__main__":
    test_whatsapp_mcp()
    
    print("\n📋 Configuração MCP sugerida:")
    print(json.dumps(MCP_CONFIG, indent=2, ensure_ascii=False))
