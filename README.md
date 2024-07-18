# chatbot no bash/terminal openai

Chatbot no bash/terminal utilizando a api da openai. 

## Para rodar o chatbot: 

```bash
python -m venv venv
```

```bash
Linux:
source venv/bin/activate
OU
. venv/bin/activate
```

```bash
Windows:
.\venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
python chatbot.py
```

## Para rodar o chat via poetry:
```bash
poetry install
```
```bash
poetry run python chatbot.py
```

## Autenticação da API

Setar a variável de ambiente com o seguinte nome:
```bash
export OPENAI_API_KEY="seu_token"
```
Ou criar o arquivo .env no diretório do programa com a variável OPENAI_API_KEY=seu_token, pois a openai autentica automaticamente o 
parâmetro api_key de OpenAI() com a varável de ambiente setada exatamente como OPENAI_API_KEY