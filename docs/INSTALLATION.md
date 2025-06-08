# 📦 Guia de Instalação Detalhado

Este guia fornece instruções passo a passo para instalar e configurar o EvoAPI MCP Server.

## 📋 Índice

- [Pré-requisitos](#pré-requisitos)
- [Instalação do UV](#instalação-do-uv)
- [Configuração do Projeto](#configuração-do-projeto)
- [Configuração de Variáveis de Ambiente](#configuração-de-variáveis-de-ambiente)
- [Configuração do Claude Desktop](#configuração-do-claude-desktop)
- [Verificação da Instalação](#verificação-da-instalação)
- [Solução de Problemas](#solução-de-problemas)

## 🔧 Pré-requisitos

### Sistema Operacional
- Windows 10/11, macOS 10.15+, ou Linux Ubuntu 18.04+

### Software Necessário
- **Python 3.11 ou superior**
- **Git** (para clonar o repositório)
- **Claude Desktop** (para integração MCP)

### Serviços Externos
- **Evolution API** configurada e funcionando
- **Instância WhatsApp** conectada na Evolution API

## 🚀 Instalação do UV

O UV é um gerenciador de pacotes Python ultrarrápido. Instale globalmente:

### Windows
```powershell
pip install uv
```

### macOS/Linux
```bash
pip install uv
# ou
pip3 install uv
```

### Verificação
```bash
uv --version
```

## 📁 Configuração do Projeto

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/evoapi-mcp.git
cd evoapi-mcp
```

### 2. Inicialização (se necessário)
Se não existir `pyproject.toml`:
```bash
uv init
```

### 3. Instalação de Dependências
```bash
# Instalar dependências principais
uv add mcp[cli] evolutionapi python-dotenv

# Ou sincronizar dependências existentes
uv sync
```

## 🔐 Configuração de Variáveis de Ambiente

### 1. Criar Arquivo .env
```bash
# Copiar o exemplo
cp .env.example .env

# Editar o arquivo
# Windows
notepad .env

# macOS/Linux
nano .env
```

### 2. Preencher Credenciais
```env
# Evolution API Configuration
EVO_API_URL=https://sua-evolution-api.com
EVO_API_TOKEN=seu_token_global_aqui
EVO_INSTANCE_NAME=sua_instancia
EVO_INSTANCE_TOKEN=token_da_instancia_aqui
```

### 3. Obter Credenciais da Evolution API

#### URL da API
- URL base da sua instância Evolution API
- Exemplo: `https://api.evolutionapi.com`

#### Token Global
- Token de autenticação global da Evolution API
- Obtido na configuração inicial da API

#### Nome da Instância
- Nome único da sua instância WhatsApp
- Exemplo: `minha_empresa_wpp`

#### Token da Instância
- Token específico da instância criada
- Gerado ao criar uma nova instância

## 🖥️ Configuração do Claude Desktop

### 1. Localizar Arquivo de Configuração

#### Windows
```powershell
code $env:AppData\Claude\claude_desktop_config.json
```

#### macOS
```bash
code ~/.config/claude/claude_desktop_config.json
```

#### Linux
```bash
code ~/.config/claude/claude_desktop_config.json
```

### 2. Adicionar Configuração MCP

Adicione ao arquivo JSON:

```json
{
  "mcpServers": {
    "evolution_api": {
      "command": "uv",
      "args": [
        "--directory",
        "/caminho/completo/para/evoapi_mcp",
        "run",
        "evoapi_mcp.py"
      ]
    }
  }
}
```

#### Exemplo Windows
```json
{
  "mcpServers": {
    "evolution_api": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Users\\usuario\\projetos\\evoapi_mcp",
        "run",
        "evoapi_mcp.py"
      ]
    }
  }
}
```

#### Exemplo macOS/Linux
```json
{
  "mcpServers": {
    "evolution_api": {
      "command": "uv",
      "args": [
        "--directory",
        "/home/usuario/projetos/evoapi_mcp",
        "run",
        "evoapi_mcp.py"
      ]
    }
  }
}
```

### 3. Reiniciar Claude Desktop
Feche e reabra o Claude Desktop para carregar a nova configuração.

## ✅ Verificação da Instalação

### 1. Teste de Importações
```bash
python -c "from evoapi_mcp import get_groups; print('✅ Importações OK')"
```

### 2. Teste de Configuração
```bash
python -c "from group_controller import GroupController; gc = GroupController(); print(f'✅ Controller: {gc.base_url}')"
```

### 3. Teste de Variáveis de Ambiente
```bash
python -c "
from dotenv import load_dotenv
import os
load_dotenv()
print('✅ Variáveis carregadas:')
for var in ['EVO_API_URL', 'EVO_API_TOKEN', 'EVO_INSTANCE_NAME', 'EVO_INSTANCE_TOKEN']:
    print(f'  {var}: {'✅' if os.getenv(var) else '❌'}')
"
```

### 4. Teste no Claude
Abra o Claude Desktop e teste:
```
Liste meus grupos do WhatsApp
```

## 🔧 Solução de Problemas

### Erro: "UV não encontrado"
```bash
# Reinstalar UV
pip install --upgrade uv

# Verificar PATH
echo $PATH  # Linux/macOS
echo $env:PATH  # Windows PowerShell
```

### Erro: "Módulo não encontrado"
```bash
# Reinstalar dependências
uv sync --force

# Verificar virtual environment
uv venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate  # Windows
```

### Erro: "API não responde"
1. Verificar se Evolution API está funcionando
2. Testar URL diretamente no navegador
3. Verificar tokens de autenticação
4. Confirmar que instância WhatsApp está conectada

### Erro: "Claude não reconhece MCP"
1. Verificar caminho absoluto no `claude_desktop_config.json`
2. Reiniciar Claude Desktop
3. Verificar logs do Claude (Menu > Desenvolvedor > Console)

### Erro: "Permissão negada"
```bash
# Dar permissões de execução (Linux/macOS)
chmod +x evoapi_mcp.py

# Executar como administrador (Windows)
# Executar terminal como administrador
```

## 📞 Suporte

Se encontrar problemas não listados aqui:

1. Verifique os logs do Claude Desktop
2. Execute os testes de verificação
3. Consulte a documentação da Evolution API
4. Abra uma issue no GitHub com:
   - Sistema operacional
   - Versão do Python
   - Mensagem de erro completa
   - Passos para reproduzir o problema

---

**Próximo passo:** [Configuração Avançada](CONFIGURATION.md)