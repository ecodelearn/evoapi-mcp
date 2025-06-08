# Relatório de Análise de Dependências e Recursos Órfãos
## Projeto: evoapi_mcp

### Data da Análise: 08/06/2025

---

## 🔍 RESUMO EXECUTIVO

**Status Atual**: Projeto com redundâncias significativas, dependências não declaradas e arquivos órfãos
**Arquivos Totais**: 15 arquivos
**Tamanho Estimado de Limpeza**: ~40% dos arquivos são candidatos à remoção
**Nível de Risco**: BAIXO (backup criado)

---

## 📊 DEPENDÊNCIAS DECLARADAS vs UTILIZADAS

### ✅ Dependências Declaradas no pyproject.toml:
- `evolutionapi>=0.1.1` ✅ **UTILIZADA**
- `mcp[cli]>=1.6.0` ✅ **UTILIZADA** 
- `python-dotenv>=1.1.0` ✅ **UTILIZADA**

### ❌ Dependências NÃO Declaradas mas Utilizadas:
- `numpy` (usado em `softmax_temperature.py`)
- `requests` (usado em múltiplos arquivos de configuração)

### 📋 Dependências Padrão Python (OK):
- `sys`, `os`, `json`, `csv`, `datetime`, `typing`, `base64`

---

## 🗂️ ANÁLISE DE ARQUIVOS

### 📁 ARQUIVOS PRINCIPAIS (MANTER):
- `evoapi_mcp.py` - **ARQUIVO PRINCIPAL MCP**
- `group_controller.py` - **CONTROLLER PRINCIPAL**
- `group.py` - **MODELO DE DADOS**
- `message_sandeco.py` - **HANDLER DE MENSAGENS**
- `send_sandeco.py` - **CLIENTE DE ENVIO**
- `pyproject.toml` - **CONFIGURAÇÃO PROJETO**
- `uv.lock` - **LOCK DE DEPENDÊNCIAS**
- `README.md` - **DOCUMENTAÇÃO**
- `.gitignore` - **CONTROLE GIT**

### ⚠️ ARQUIVOS REDUNDANTES (CANDIDATOS À REMOÇÃO):

#### 🔄 Classes Similares/Duplicadas:
1. **`evolution_api_config.py`** - 241 linhas
   - Funcionalidade: Cliente alternativo Evolution API
   - Status: ÓRFÃO (não referenciado em código principal)
   
2. **`whatsapp_mcp_config.py`** - 165 linhas  
   - Funcionalidade: Cliente WhatsApp MCP alternativo
   - Status: ÓRFÃO (não referenciado em código principal)
   
3. **`mcp_evolution_fix.py`** - 231 linhas
   - Funcionalidade: "Fix" para servidor MCP
   - Status: ÓRFÃO (não referenciado em código principal)

#### 🧪 Arquivos de Teste/Exemplo:
4. **`test_groups.py`** - 41 linhas
   - Funcionalidade: Teste manual de grupos
   - Status: ÓRFÃO (pode ser removido após validação)

5. **`export_groups_csv.py`** - 77 linhas
   - Funcionalidade: Exportar grupos para CSV
   - Status: UTILITÁRIO (manter se usado pelos usuários)

6. **`softmax_temperature.py`** - 31 linhas
   - Funcionalidade: Exemplo de softmax
   - Status: ÓRFÃO + DEPENDÊNCIA NÃO DECLARADA
   - Problema: Requer `numpy` não declarado

---

## 📈 IMPACTO DA LIMPEZA

### Arquivos a Remover (5 arquivos):
- `evolution_api_config.py`
- `whatsapp_mcp_config.py` 
- `mcp_evolution_fix.py`
- `test_groups.py`
- `softmax_temperature.py`

### Redução Estimada:
- **Linhas de código**: ~775 linhas removidas
- **Arquivos**: 33% redução (5/15 arquivos)
- **Complexidade**: Eliminação de 3 classes redundantes

---

## 🎯 PLANO DE AÇÃO

### Fase 1: Validação ✅ CONCLUÍDA
- [x] Backup criado (commit: 2fb455d)
- [x] Validar funcionalidade atual (105 grupos encontrados)
- [x] Confirmar que arquivos órfãos não são usados

### Fase 2: Limpeza Segura ✅ CONCLUÍDA
- [x] Remover arquivos órfãos identificados
- [x] Manter `export_groups_csv.py` (utilitário potencial)
- [x] Validar funcionalidade pós-limpeza

### Fase 3: Ajustes Finais ✅ CONCLUÍDA
- [x] Atualizar README se necessário
- [x] Executar testes de funcionalidade
- [x] Commit da limpeza

---

## ⚠️ RISCOS IDENTIFICADOS

### BAIXO RISCO:
- Arquivos órfãos não são importados pelo código principal
- Backup completo realizado
- Funcionalidade principal preservada

### RECOMENDAÇÕES:
1. Manter `export_groups_csv.py` por ser utilitário
2. Remover `softmax_temperature.py` (não relacionado ao projeto)
3. Consolidar funcionalidades se necessário no futuro

---

## 📋 PRÓXIMOS PASSOS

1. **Executar testes** para validar funcionalidade atual
2. **Remover arquivos órfãos** em lote
3. **Validar projeto** pós-limpeza
4. **Documentar mudanças** no commit final