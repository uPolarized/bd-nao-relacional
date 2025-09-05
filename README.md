# CRUD MongoDB com PyMongo (atividade individual)

Projeto simples que demonstra operações **CRUD** (Create, Read, Update, Delete) em uma coleção `alunos` no MongoDB usando **PyMongo**.

## ✅ O que tem aqui
- Conexão com MongoDB (local via Docker por padrão).
- Funções de **CREATE**, **READ**, **UPDATE** e **DELETE**.
- Script de demonstração que executa as operações em sequência.
- `docker-compose.yml` para subir MongoDB e **mongo-express** (UI web).

---

## 🚀 Como rodar

### 1) Subir o MongoDB (recomendado via Docker)
> Requisitos: [Docker Desktop](https://www.docker.com/) instalado e rodando.

No terminal, dentro da pasta do projeto:

```bash
docker compose up -d
```

Isso vai iniciar:
- **MongoDB** ouvindo em `localhost:27017`
- **mongo-express** em `http://localhost:8081` (UI opcional)

> Para parar: `docker compose down`

### 2) Preparar o ambiente Python
Crie e ative um ambiente virtual e instale as dependências:

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3) Configurar variáveis de ambiente (opcional)
Copie o arquivo `.env.example` para `.env` e ajuste a `MONGO_URI` se necessário.

- Local (Docker): `mongodb://localhost:27017/`
- Atlas (nuvem): `mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net/?retryWrites=true&w=majority`

### 4) Executar o exemplo CRUD
```bash
python app/main.py
```

Saída esperada (aproximada):
```
[CREATE] ID inserido: 66f...
[READ] Todos os alunos: [...]
[UPDATE] Documentos atualizados: 1
[READ] João atualizado: [...]
[DELETE] Documentos removidos: 1
```

---

## 📁 Estrutura
```
mongo-crud-pymongo/
├─ app/
│  ├─ crud.py          
│  ├─ db.py            
│  └─ main.py         
├─ .env.example
├─ .gitignore
├─ docker-compose.yml  
├─ requirements.txt
└─ README.md
```



## 📚 Referências r
- PyMongo docs: https://pymongo.readthedocs.io/en/stable/
- MongoDB docs: https://www.mongodb.com/docs/
```

