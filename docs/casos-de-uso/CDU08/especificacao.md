# CDU08 – Cadastrar Serviços Adicionais

**Descrição:** Permite que o administrador cadastre serviços adicionais oferecidos pelo hotel, como café da manhã, lavanderia e transporte.

**Ator Primário:** Administrador.

**Pré-condições:**  
- O administrador deve estar logado no sistema.

**Pós-condições:**  
- O serviço adicional é cadastrado no sistema.

## Fluxo Principal

1. O administrador acessa a opção Cadastrar Serviços Adicionais no sistema.
2. O sistema exibe o formulário de cadastro de serviços adicionais.
3. O administrador informa os dados do serviço (nome, descrição e valor).
4. O administrador confirma o cadastro.
5. O sistema valida os dados informados.
6. O sistema salva o serviço adicional.
7. O sistema exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Dados inválidos:**  
  Se o administrador informar dados inválidos ou deixar campos obrigatórios em branco, o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Serviço já existente:**  
  Se o administrador tentar cadastrar um serviço que já exista, o sistema exibirá uma mensagem informando o conflito.
