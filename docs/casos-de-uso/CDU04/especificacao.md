# CDU04 – Listar Quartos

**Descrição:** Permite visualizar todos os quartos cadastrados no sistema.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O usuário deve estar logado no sistema.

**Pós-condições:** 
- A lista de quartos é exibida.

## Fluxo Principal

1. O administrador acessa a opção "Quarto" no menu lateral e seleciona a aba "Listar".
2. O sistema busca todos os quartos registrados no banco de dados.
3. O sistema exibe uma tabela contendo ID, Tipo, Bloco e Número de cada quarto.
4. Caso não existam registros, o sistema informa que a lista está vazia.

## Fluxos de Exceção

- **FE1 – Nenhum quarto encontrado:** Se não existir nenhum quarto cadastrado na base de dados, o sistema exibirá uma mensagem informando que não há registros para exibição.