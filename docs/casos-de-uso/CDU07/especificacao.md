# CDU07 – Cadastrar Tipos de Quarto

**Descrição:** Permite que o administrador cadastre novos tipos de quarto no sistema, definindo suas características específicas.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.

**Pós-condições:** 
- O tipo de quarto é cadastrado no sistema.

## Fluxo Principal

1. O administrador acessa a opção "Tipo de Quarto" no menu lateral.
2. O sistema exibe o formulário de cadastro na aba "Inserir".
3. O administrador informa os dados do tipo de quarto (nome, descrição, capacidade e valor da diária).
4. O administrador confirma o cadastro clicando no botão "Inserir".
5. O sistema valida os dados informados.
6. O sistema salva o novo tipo de quarto.
7. O sistema exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Dados inválidos:** Se o administrador informar dados inválidos ou deixar campos obrigatórios em branco, o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Tipo de quarto já existente:** Se o administrador tentar cadastrar um tipo de quarto com nome já existente, o sistema exibirá uma mensagem informando o conflito.