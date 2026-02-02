# CDU04 – Listar Quartos

**Descrição:** Permite visualizar todos os quartos cadastrados no sistema.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.

**Pós-condições:** 
- A lista de quartos é exibida para consulta.

## Fluxo Principal

1. O administrador acessa a opção "Quarto" no menu lateral.
2. O sistema exibe por padrão a aba "Listar".
3. O sistema recupera as informações dos quartos registrados.
4. O sistema exibe uma tabela contendo as colunas: ID, Tipo, Bloco e Número.

## Fluxos de Exceção

- **FE1 – Nenhum quarto encontrado:** Se não houver quartos cadastrados, o sistema exibe a mensagem "Nenhum quarto cadastrado.".