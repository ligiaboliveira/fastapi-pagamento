## Fastapi Pagamento

### Sobre o projeto

API de pagamento com fastAPI

---

### Instalação e configuração

**Clone o repositório:**
```bash
$ git clone https://github.com/seu-usuario/fastapi-pagamento.git
```

**Navegue até o diretório do projeto:**
```bash
$ cd fastapi-pagamento
```

**Crie um ambiente virtual (opcional, mas recomendado):**
```bash
$ python3 -m venv .venv
```

**Ative o ambiente virtual:**
```bash
$ source .venv/bin/activate
```

**Instale as dependências do projeto:**
```bash
$ pip install -r requirements.txt
```

**Adicione as migrations**
```bash
$ python -m app.seed
```

**Inicie o servidor de desenvolvimento:**
```bash
$ uvicorn app.main:app --reload
```

**Acesse a aplicação em seu navegador web:**
> http://127.0.0.1:8000/