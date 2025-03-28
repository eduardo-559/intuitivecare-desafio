# 🚀 Desafio Técnico – IntuitiveCare

Este projeto foi desenvolvido como parte do processo seletivo da IntuitiveCare. Ele consiste na construção de uma solução completa para extração, transformação, carga, análise e visualização de dados.

---

## 🔧 Tecnologias Utilizadas

- **Python 3.12**
- **Flask** (API REST)
- **BeautifulSoup4** (web scraping de PDF)
- **PostgreSQL** (banco de dados relacional)
- **Vue.js** (interface web)
- **HTML + CSS + JavaScript**

---

## 🧠 Funcionalidades

- 🗂 Extração automatizada de dados tabulares a partir de arquivos PDF.
- 🧹 Transformação e limpeza dos dados (tratamento de encoding, formatação numérica).
- 🗃 Armazenamento em banco relacional PostgreSQL.
- 🌐 API REST para consulta de dados.
- 📊 Interface em Vue.js exibindo o Top 10 operadoras com maior saldo final.
- 📌 Código modular e bem estruturado, com foco em clareza e boas práticas.

---

## ▶️ Como Executar o Projeto

### 1. Backend (API Flask)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

    A API estará disponível em: http://localhost:5000
```

### 2. Banco de Dados
```
Crie o banco e as tabelas no PostgreSQL:

CREATE DATABASE ans;

Em seguida, execute os comandos SQL abaixo para as tabelas:

-- Tabela operadoras
CREATE TABLE operadoras (
  registro_ans VARCHAR,
  cnpj VARCHAR,
  razao_social TEXT,
  nome_fantasia TEXT,
  modalidade TEXT,
  logradouro TEXT,
  numero TEXT,
  complemento TEXT,
  bairro TEXT,
  cidade TEXT,
  uf CHAR(2),
  cep VARCHAR,
  ddd TEXT,
  telefone TEXT,
  fax TEXT,
  email TEXT,
  representante TEXT,
  cargo_representante TEXT,
  data_registro TEXT,
  status TEXT
);

-- Tabela demonstrativos
CREATE TABLE demonstrativos (
  data DATE,
  reg_ans VARCHAR,
  cd_conta_contabil VARCHAR,
  descricao TEXT,
  vl_saldo_inicial TEXT,
  vl_saldo_final TEXT
);

Utilize o comando \COPY para importar os arquivos .csv contidos na pasta banco_dados/.
```
### 3. Frontend (Vue.js)
```
cd frontend
npm install
npm run serve

    A interface estará acessível em: http://localhost:8080
```

📌 Observações Finais

Este projeto foi desenvolvido com foco em organização, clareza e boas práticas, simulando um ambiente real de trabalho e entregando uma solução funcional, escalável e pronta para evoluir.
