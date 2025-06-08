#!/usr/bin/env python3
"""
Script para Corrigir Servidor MCP Evolution API
Demonstra a configuração correta para https://api.frontzin.com.br
"""

import json
import requests
from typing import Dict, Any

class EvolutionAPIMCPFixed:
    """Servidor MCP Evolution API Corrigido"""
    
    def __init__(self, api_key: str = None):
        self.api_base = "https://api.frontzin.com.br"
        self.instance = "Daniel_Dias"
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        if api_key:
            self.headers["apikey"] = api_key
    
    def get_groups(self) -> Dict[str, Any]:
        """CORRIGIDO: Buscar grupos usando Evolution API"""
        if not self.api_key:
            return {
                "error": "API Key necessária. Configure no Evolution Manager.",
                "manager_url": f"{self.api_base}/manager",
                "status": "auth_required"
            }
        
        # Evolution API endpoint correto
        endpoint = f"{self.api_base}/chat/findChats/{self.instance}"
        
        try:
            response = requests.get(endpoint, headers=self.headers, timeout=30)
            
            if response.status_code == 200:
                chats = response.json()
                # Filtrar apenas grupos (terminam com @g.us)
                groups = [chat for chat in chats if chat.get("id", "").endswith("@g.us")]
                
                return {
                    "status": "success",
                    "groups": groups,
                    "total_groups": len(groups),
                    "total_chats": len(chats)
                }
            else:
                return {
                    "error": f"HTTP {response.status_code}: {response.text}",
                    "status": "api_error"
                }
                
        except Exception as e:
            return {
                "error": str(e),
                "status": "connection_error"
            }
    
    def send_message_to_group(self, group_id: str, message: str) -> Dict[str, Any]:
        """CORRIGIDO: Enviar mensagem para grupo"""
        if not self.api_key:
            return {
                "error": "API Key necessária",
                "status": "auth_required"
            }
        
        endpoint = f"{self.api_base}/message/sendText/{self.instance}"
        
        payload = {
            "number": group_id,  # Evolution API usa "number" para grupos também
            "text": message
        }
        
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers, timeout=30)
            
            if response.status_code == 200:
                return {
                    "status": "success",
                    "response": response.json()
                }
            else:
                return {
                    "error": f"HTTP {response.status_code}: {response.text}",
                    "status": "api_error"
                }
                
        except Exception as e:
            return {
                "error": str(e),
                "status": "connection_error"
            }
    
    def get_group_messages(self, group_id: str, start_date: str = None, end_date: str = None) -> Dict[str, Any]:
        """CORRIGIDO: Buscar mensagens de grupo"""
        if not self.api_key:
            return {
                "error": "API Key necessária",
                "status": "auth_required"
            }
        
        endpoint = f"{self.api_base}/chat/findMessages/{self.instance}"
        
        payload = {
            "where": {
                "key": {
                    "remoteJid": group_id
                }
            },
            "limit": 50  # Ajustar conforme necessário
        }
        
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers, timeout=30)
            
            if response.status_code == 200:
                return {
                    "status": "success",
                    "messages": response.json()
                }
            else:
                return {
                    "error": f"HTTP {response.status_code}: {response.text}",
                    "status": "api_error"
                }
                
        except Exception as e:
            return {
                "error": str(e),
                "status": "connection_error"
            }

# Teste sem API Key para demonstrar problema
def demonstrate_fix():
    """Demonstra a correção necessária"""
    print("🔧 DEMONSTRAÇÃO: Correção do Servidor MCP")
    print("=" * 60)
    
    # Teste sem API Key
    print("1. 🔐 Testando SEM API Key:")
    client_no_key = EvolutionAPIMCPFixed()
    result = client_no_key.get_groups()
    print(f"   Status: {result['status']}")
    print(f"   Erro: {result['error']}")
    print(f"   Manager: {result['manager_url']}")
    
    print("\n2. 📚 Configuração Necessária:")
    print("   ✅ Acessar: https://api.frontzin.com.br/manager")
    print("   ✅ Fazer login com API Key Global")
    print("   ✅ Configurar instância 'Daniel_Dias'")
    print("   ✅ Obter API Key da instância")
    
    print("\n3. 🛠️  Endpoints Corretos:")
    endpoints = {
        "❌ Antigo (Errado)": "localhost:8081/group/fetchAllGroups/Daniel_Dias",
        "✅ Novo (Correto)": "https://api.frontzin.com.br/chat/findChats/Daniel_Dias"
    }
    
    for label, endpoint in endpoints.items():
        print(f"   {label}: {endpoint}")
    
    print("\n4. 📋 Headers Necessários:")
    print("   Content-Type: application/json")
    print("   Accept: application/json")
    print("   apikey: <SUA_API_KEY>")

# Configuração MCP corrigida completa
MCP_EVOLUTION_CONFIG = {
    "server_info": {
        "name": "Evolution API MCP Server",
        "api_base": "https://api.frontzin.com.br",
        "version": "2.2.3",
        "manager_url": "https://api.frontzin.com.br/manager",
        "documentation": "https://doc.evolution-api.com"
    },
    "authentication": {
        "required": True,
        "method": "API Key",
        "header": "apikey",
        "obtain_from": "Evolution Manager Login"
    },
    "instance": {
        "name": "Daniel_Dias",
        "required": True,
        "usage": "Todas as URLs requerem /{instance}"
    },
    "endpoints": {
        "get_groups": {
            "url": "/chat/findChats/{instance}",
            "method": "GET",
            "filter": "groups only (id ends with @g.us)"
        },
        "send_message_to_group": {
            "url": "/message/sendText/{instance}",
            "method": "POST",
            "payload": {"number": "group_id", "text": "message"}
        },
        "get_group_messages": {
            "url": "/chat/findMessages/{instance}",
            "method": "POST",
            "payload": {"where": {"key": {"remoteJid": "group_id"}}, "limit": 50}
        },
        "send_message_to_phone": {
            "url": "/message/sendText/{instance}",
            "method": "POST",
            "payload": {"number": "phone_number", "text": "message"}
        }
    },
    "mcp_tools_corrections": {
        "get_groups": "REQUER: Evolution API Key + findChats endpoint",
        "send_message_to_group": "FUNCIONA: Estrutura similar mas endpoint correto",
        "get_group_messages": "REQUER: API Key + findMessages endpoint",
        "send_message_to_phone": "FUNCIONA: Já usa estrutura correta"
    }
}

if __name__ == "__main__":
    demonstrate_fix()
    
    print(f"\n📁 Configuração MCP Completa Corrigida:")
    print(json.dumps(MCP_EVOLUTION_CONFIG, indent=2, ensure_ascii=False))
    
    print(f"\n🎯 PRÓXIMOS PASSOS:")
    print("1. Obter API Key Global no Evolution Manager")
    print("2. Reconfigurar servidor MCP com endpoints corretos")
    print("3. Adicionar header 'apikey' em todas as requisições")
    print("4. Testar get_groups() novamente")
