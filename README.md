# InnControl

Sistema de Gerenciamento de Hotel e Pousada

## Sobre o Projeto

O **InnControl** é um sistema web desenvolvido para facilitar a gestão de hotéis e pousadas de pequeno e médio porte. O sistema oferece controle completo de reservas, check-in/check-out, gerenciamento de quartos, registro de serviços adicionais e relatórios gerenciais.

Desenvolvido como projeto final da disciplina de **Programação Orientada a Objetos**, **Análise e Projeto Orientada a Objetos** e **Banco de Dados** do curso Técnico em Informática para Internet do IFRN - Campus Natal Central.

## Integrantes do Grupo

- [Lucas Gabriel da Silva Duarte](https://github.com/luuuuuqui)
- [João Gustavo Alves da Silva](https://github.com/JGustavo123)
- [José Luan Ribeiro Vieira](https://github.com/luanzxy)
- [Winnicius da Silva Faustino de Alcântara](https://github.com/winsilv16)

## Objetivo do Sistema

Centralizar e automatizar a gestão de estabelecimentos hoteleiros, permitindo:

- Controle eficiente de reservas e disponibilidade
- Gestão de check-in e check-out
- Registro de hóspedes e histórico de estadias
- Controle de serviços adicionais consumidos
- Geração de relatórios gerenciais com gráficos
- Diferentes perfis de acesso (Administrador, Recepcionista, Hóspede)

## Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Framework Web:** Streamlit
- **Banco de Dados:** SQLite3
- **Arquitetura:** MVC (Model-View-Controller) em camadas
- **Controle de Versão:** Git/GitHub
- **Diagramas UML:** LucidChart e Astah

## Bibliotecas Utilizadas

### Bibliotecas Obrigatórias

* **streamlit** (≥1.28.0): Framework web para criação da interface do sistema
* **pandas** (≥2.0.0): Manipulação e análise de dados para relatórios e tabelas

### Bibliotecas Opcionais (Funcionalidades Avançadas)

As seguintes bibliotecas são opcionais, mas recomendadas para aproveitar todas as funcionalidades do sistema:

* **fpdf2** (≥2.7.0): Geração de relatórios em PDF (módulo de Relatórios Gerenciais)
* **plotly** (≥5.17.0): Criação de gráficos interativos nos dashboards de relatórios
* **openpyxl** (≥3.1.0): Exportação de dados para arquivos Excel (.xlsx)

> **Nota:** O sistema funciona sem as bibliotecas opcionais, mas algumas funcionalidades estarão desabilitadas (como exportação de PDF/Excel e gráficos interativos).

## Instalação

### Pré-requisitos

* Python 3.8 ou superior
* pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/inncontrol.git
   cd inncontrol
   ```

2. **Crie um ambiente virtual (recomendado):**

   **Windows:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **Linux/Mac:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   **Instalação básica (apenas bibliotecas obrigatórias):**

   ```bash
   pip install streamlit pandas
   ```

   **Instalação completa (com todas as funcionalidades):**

   ```bash
   pip install -r requirements.txt
   ```

   Ou instale manualmente:

   ```bash
   pip install streamlit pandas fpdf2 plotly openpyxl
   ```

## Como Executar

1. **Navegue até a pasta do projeto:**
   ```bash
   cd src
   ```

2. **Execute o sistema:**
   ```bash
   streamlit run index.py
   ```

3. **Acesse o sistema:**
   * O Streamlit abrirá automaticamente no navegador
   * Se não abrir, acesse: `http://localhost:8501`

## Estrutura do Projeto

```
inncontrol/
├── src/
│   ├── dao/              # Camada de acesso a dados
│   ├── models/           # Modelos de dados
│   ├── templates/        # Interfaces de usuário (UI)
│   ├── index.py         # Arquivo principal
│   └── views.py         # Camada de lógica de negócio
├── requirements.txt      # Dependências do projeto
└── README.md            # Este arquivo
```

## Documentação

Toda a documentação técnica e diagramas UML estão disponíveis na pasta [`docs/`](docs/):

- [Documento de Visão](docs/visao-do-produto/visaodoproduto.pdf)
- [Casos de Uso](docs/casos-de-uso/)
- [Diagramas UML](docs/diagrama-de-classes/)

## Licença

Este projeto está licenciado sob a Licença MIT.

Desenvolvido para fins educacionais como parte do curso Técnico em Informática para Internet do IFRN.
