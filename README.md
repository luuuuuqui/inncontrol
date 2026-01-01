# InnControl

Sistema de Gerenciamento de Hotel e Pousada

## Sobre o Projeto

O **InnControl** é um sistema web desenvolvido para facilitar a gestão de hotéis e pousadas de pequeno e médio porte. O sistema oferece controle completo de reservas, check-in/check-out, gerenciamento de quartos, registro de serviços adicionais e relatórios gerenciais.

Desenvolvido como projeto final da disciplina de **Programação Orientada a Objetos**, **Análise e Projeto Orientada a Objetos** e **Banco de Dados** do curso Técnico em Informática para Internet do IFRN - Campus Natal Central.

## Integrantes do Grupo

- [Lucas Gabriel da Silva Duarte](https://github.com/luuuuuqui)
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

## Estrutura do Repositório

``` 
inncontrol/
├── docs/                                    # Documentação do projeto
│   ├── visao-do-produto/                    # Documento de visão
│   │   ├── visao.pdf
│   │   └── visao.md
│   ├── requisitos/                          # Requisitos do sistema
│   │   ├── requisitos-funcionais.md
│   │   └── requisitos-nao-funcionais.md
│   ├── casos-de-uso/                        # Casos de uso detalhados
│   │   ├── UC01-efetuar-login/
│   │   │   ├── especificacao.md
│   │   │   ├── diagrama-uc01.png
│   │   │   ├── seq-uc01.png
│   │   │   └── com-uc01.png
│   │   ├── UC02-realizar-reserva/
│   │   │   ├── especificacao.md
│   │   │   ├── diagrama-uc02.png
│   │   │   ├── seq-uc02.png
│   │   │   └── com-uc02.png
│   │   ├── UC03-realizar-checkin/
│   │   │   ├── especificacao.md
│   │   │   ├── diagrama-uc03.png
│   │   │   ├── seq-uc03.png
│   │   │   └── com-uc03.png
│   │   └── diagrama-casos-de-uso-geral.png
│   ├── diagrama-de-classes/                 # Diagramas de classes
│   │   ├── classes-modelo.png
│   │   ├── classes-persistencia.png
│   │   ├── classes-operacoes.png
│   │   ├── classes-interface.png
│   │   └── classes-editavel.puml
│   └── diagramas-fontes/                    # Arquivos editáveis
│       ├── plantuml/
│       └── draw-io/
├── src/                                     # Código fonte (implementação)
│   ├── model/                               # Entidades do sistema
│   ├── view/                                # Operações/Controladores
│   ├── template/                            # Interface Streamlit
│   ├── dao/                                 # Persistência de dados
│   └── database/                            # Banco de dados SQLite
├── tests/                                   # Testes do sistema
├── requirements.txt                         # Dependências do projeto
├── LICENSE                                  # Licença MIT
└── README.md                                # Este arquivo
```

## Documentação

Toda a documentação técnica e diagramas UML estão disponíveis na pasta [`docs/`](docs/):

- [Documento de Visão](docs/visao-do-produto/visao.pdf)
- [Casos de Uso](docs/casos-de-uso/)
- [Diagramas UML](docs/diagrama-de-classes/)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

Desenvolvido para fins educacionais como parte do curso Técnico em Informática para Internet do IFRN.
