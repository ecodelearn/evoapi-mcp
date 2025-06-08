# 📖 Guia de Uso - EvoAPI MCP Server

Este guia mostra como usar o EvoAPI MCP Server de forma prática, com exemplos reais de comandos e cenários de uso.

## 📋 Índice

- [Primeiros Passos](#primeiros-passos)
- [Comandos Básicos](#comandos-básicos)
- [Comandos Avançados](#comandos-avançados)
- [Cenários de Uso](#cenários-de-uso)
- [Boas Práticas](#boas-práticas)
- [Troubleshooting](#troubleshooting)

## 🚀 Primeiros Passos

### Verificar Conexão
Antes de usar, verifique se o servidor está funcionando:

```
Teste a conexão com a Evolution API
```

### Listar Grupos Disponíveis
```
Liste todos os meus grupos do WhatsApp
```

**Resposta esperada:**
```
Grupo ID: 120363123456789@g.us, Nome: Família
Grupo ID: 120363987654321@g.us, Nome: Trabalho
Grupo ID: 120363555666777@g.us, Nome: Amigos
```

## 💬 Comandos Básicos

### 1. Enviar Mensagem para Grupo
```
Envie a mensagem "Bom dia pessoal! 🌅" para o grupo Família
```

```
Mande "Reunião às 14h na sala de conferências" para o grupo Trabalho
```

### 2. Enviar Mensagem para Número Individual
```
Envie "Olá! Como você está?" para o número 11999887766
```

```
Mande uma mensagem para 5511988776655 dizendo "Documentos enviados por email"
```

### 3. Consultar Histórico de Mensagens
```
Mostre as mensagens do grupo Família das últimas 24 horas
```

```
Quero ver as mensagens do grupo Trabalho de ontem
```

```
Recupere as mensagens do grupo 120363123456789@g.us entre 2025-01-07 09:00:00 e 2025-01-07 18:00:00
```

## 🎯 Comandos Avançados

### 1. Análise de Atividade de Grupo
```
Analise a atividade do grupo Trabalho na última semana e me dê um resumo
```

### 2. Busca por Palavras-chave
```
Procure mensagens que contenham "reunião" no grupo Trabalho nas últimas 48 horas
```

### 3. Envio de Mensagens Formatadas
```
Envie para o grupo Família:
📋 *LISTA DE COMPRAS*
• Pão
• Leite 
• Ovos
• Frutas

Quem pode ir ao mercado hoje? 🛒
```

### 4. Mensagens com Emojis e Formatação
```
Mande para o grupo Amigos:
🎉 *FESTA DE ANIVERSÁRIO* 🎂

📅 Data: Sábado, 15/01
🕖 Horário: 19h
📍 Local: Casa do João

Confirmem presença! 🙋‍♀️🙋‍♂️
```

## 🎭 Cenários de Uso

### Cenário 1: Gestão de Equipe
```
# Manhã - Verificar mensagens da equipe
Mostre as mensagens do grupo Equipe TI desde às 8h de hoje

# Enviar briefing diário
Envie para o grupo Equipe TI:
🌅 *BOM DIA EQUIPE!*

📋 Agenda de hoje:
• 09h - Standup meeting
• 10h - Review do código
• 14h - Deploy em produção
• 16h - Retrospectiva semanal

Qualquer dúvida, me chamem! 💪
```

### Cenário 2: Atendimento ao Cliente
```
# Verificar mensagens de suporte
Mostre mensagens do grupo Suporte Cliente nas últimas 2 horas

# Responder cliente
Envie para 5511999888777:
Olá! Recebi sua solicitação de suporte.
Vou analisar seu caso e retorno em até 1 hora.

Ticket #1234 aberto ✅
```

### Cenário 3: Família
```
# Verificar atividade familiar
Quais foram as últimas mensagens do grupo Família?

# Organizar evento
Envie para o grupo Família:
👨‍👩‍👧‍👦 *ALMOÇO DE DOMINGO*

Quem vem para o almoço da vovó?
📅 Domingo, 12/01 às 12h

Respondam até sexta! 🍽️
```

### Cenário 4: Notificações Automáticas
```
# Notificação de sistema
Envie para o grupo TI:
🚨 *ALERTA DE SISTEMA*

Servidor de backup apresentou falha às 03:15
Status: Em investigação ⚠️
ETA resolução: 30 minutos

Acompanhem o chat para updates.
```

## ✅ Boas Práticas

### 1. Formato de Números
- **Correto**: `5511999888777` (código país + DDD + número)
- **Incorreto**: `11999888777`, `(11) 99988-8777`

### 2. Datas e Horários
- **Formato**: `YYYY-MM-DD HH:MM:SS`
- **Exemplo**: `2025-01-08 14:30:00`

### 3. Identificação de Grupos
- Use sempre o nome do grupo quando possível
- Em caso de ambiguidade, use o ID do grupo

### 4. Mensagens Claras
- Use formatação Markdown quando apropriado
- Inclua emojis para melhor comunicação
- Seja específico nas datas e horários

### 5. Segurança
- Nunca compartilhe tokens ou credenciais
- Cuidado com informações sensíveis em grupos
- Verifique destinatários antes de enviar

## 🔧 Troubleshooting

### Problema: "Grupo não encontrado"
```
# Listar grupos primeiro
Liste todos os meus grupos do WhatsApp

# Usar ID específico
Envie mensagem para o grupo 120363123456789@g.us
```

### Problema: "Número inválido"
```
# Verificar formato
Correto: 5511999888777
Incorreto: (11) 99988-8777

# Adicionar código do país se necessário
Para número sem 55: adicione 55 na frente
```

### Problema: "Falha na conexão"
```
# Verificar status da API
Teste a conexão com a Evolution API

# Verificar configurações
Confirme se as variáveis de ambiente estão corretas
```

### Problema: "Histórico vazio"
```
# Verificar intervalo de datas
Use datas válidas: 2025-01-07 09:00:00

# Verificar se grupo tem mensagens
Teste com intervalo maior de tempo
```

## 📝 Exemplos de Comandos Prontos

### Para Copiar e Usar

#### Gestão de Equipe
```
Envie para o grupo Equipe:
📊 *RELATÓRIO DIÁRIO*
✅ Tasks concluídas: 8/10
⏳ Em andamento: 2
🎯 Meta da sprint: 85% completa
```

#### Comunicação Familiar
```
Mande para o grupo Família:
🏠 *LEMBRETE CASA*
• Lixo: Terça e Sexta
• Contas: Vencimento dia 15
• Reunião familiar: Domingo 14h
```

#### Atendimento Profissional
```
Envie para 5511999888777:
Prezado cliente,
Seu pedido #1234 foi processado.
Previsão de entrega: 2-3 dias úteis.
Código de rastreamento será enviado em breve.
```

#### Notificação de Sistema
```
Envie para o grupo TI:
⚡ *UPDATE SISTEMA*
Deploy v2.1.3 concluído ✅
• Correções de bugs aplicadas
• Performance melhorada em 15%
• Novos recursos disponíveis
```

---

**Próximos passos:**
- [API Reference](API.md) - Documentação técnica completa
- [Configuração Avançada](CONFIGURATION.md) - Personalizações
- [Exemplos](EXAMPLES.md) - Mais casos de uso