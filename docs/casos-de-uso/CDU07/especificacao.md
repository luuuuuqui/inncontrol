# CDU07 – Cadastrar Tipos de Quarto

**Descrição:** Permite que o administrador cadastre novos tipos de quarto no sistema, definindo suas características específicas.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.

**Pós-condições:** 
- O tipo de quarto é cadastrado no sistema.

## Fluxo Principal

1. O administrador acessa a opção Cadastrar Tipos de Quarto no sistema.
2. O sistema exibe o formulário de cadastro de tipo de quarto.
3. O administrador informa os dados do tipo de quarto (nome, descrição, capacidade e valor).
4. O administrador confirma o cadastro.
5. O sistema valida os dados informados.
6. O sistema salva o novo tipo de quarto.
7. O sistema exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Dados inválidos:** Se o administrador informar dados inválidos ou deixar campos obrigatórios em branco, o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Tipo de quarto já existente:** Se o administrador tentar cadastrar um tipo de quarto já existente, o sistema exibirá uma mensagem informando o conflito.