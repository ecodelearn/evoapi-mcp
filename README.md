
## Instale o "UV" no Python geral da sua máquina
## Abra o terminal do windows de digite
pip install uv

## Se não existir o pyprojetc.toml execute
uv init 

## Instale o mcp[cli]
uv add mcp[cli] evolutionapi python-dotenv

## Se existir o pyprojetc.toml execute
uv sync
## que vai instalar as dependências do projeto

## Para editar o json do claude
## execute a linha abaixo no terminal do vscode
code $env:AppData\Claude\claude_desktop_config.json