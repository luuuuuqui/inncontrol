# CDU15 – Cadastrar Hóspede

**Descrição:** Permite cadastrar os dados de um hóspede no sistema para utilização em reservas e estadias.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O usuário deve estar logado no sistema.

**Pós-condições:** 
- O hóspede é cadastrado no sistema.

## Fluxo Principal

1. O administrador acessa a opção Cadastrar Hóspede no sistema.
2. O sistema exibe o formulário de cadastro de hóspede.
3. O administrador informa os dados do hóspede (nome, e-mail, telefone e endereço).
4. O administrador confirma o cadastro.
5. O sistema valida os dados informados.
6. O sistema salva o hóspede no banco de dados.
7. O sistema exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Dados inválidos:** Se o administrador informar dados inválidos ou deixar campos obrigatórios em branco, o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Hóspede já cadastrado:** Se o e-mail informado já estiver vinculado a um hóspede existente, o sistema exibirá uma mensagem informando o conflito.