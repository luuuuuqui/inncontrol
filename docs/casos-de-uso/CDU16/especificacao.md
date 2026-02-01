# CDU16 – Listar Hóspedes

**Descrição:** Permite visualizar a lista de todos os hóspedes registrados no sistema, facilitando a consulta de dados de contato e endereço vinculado.

**Ator Primário:** Administrador e Recepcionista.

**Pré-condições:** 
- O usuário deve estar logado no sistema.

**Pós-condições:** 
- A lista de hóspedes é exibida para consulta.

## Fluxo Principal

1. O usuário acessa a opção "Hóspede" no menu lateral.
2. O sistema exibe por padrão a aba "Listar" com a relação de hóspedes.
3. O sistema recupera os registros de hóspedes, incluindo as informações do usuário vinculado (Nome e E-mail) e o endereço cadastrado.
4. O sistema exibe uma tabela contendo as colunas: ID, Nome, E-mail e Endereço.
5. O usuário pode utilizar o campo de pesquisa para filtrar a lista por nome em tempo real.

## Fluxos de Exceção

- **FE1 – Nenhum hóspede encontrado:** Se não houver hóspedes cadastrados no sistema, será exibida a mensagem "Nenhum hóspede cadastrado.".