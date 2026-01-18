# CDU02 – Gerenciar Usuários

**Descrição:** Permite que o administrador gerencie os usuários do sistema, podendo cadastrar, listar, atualizar e excluir usuários.

**Ator Primário:** Administrador.

**Pré-condições:**  
- O administrador deve estar logado no sistema.

**Pós-condições:**  
- Usuários cadastrados, atualizados ou removidos conforme a ação executada.

## Fluxo Principal

1. O administrador acessa a opção Gerenciar Usuários no sistema.
2. O sistema exibe a lista de usuários cadastrados.
3. O administrador escolhe uma das ações:
- Cadastrar novo usuário
- Atualizar usuário existente
- Excluir usuário
4. O administrador informa os dados necessários conforme a ação escolhida.
5. O sistema valida os dados informados.
6. O sistema executa a ação solicitada.
7. O sistema exibe uma mensagem de sucesso.
## Fluxos de Exceção

- **FE1 – Dados inválidos:**  
  Se o administrador informar dados inválidos ou obrigatórios em branco, o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Usuário já existente:**  
  Se o administrador tentar cadastrar um usuário com email ou CPF já existente, o sistema exibirá uma mensagem informando o conflito.

- **FE3 – Exclusão não permitida:**  
  Se o administrador tentar excluir um usuário que possua vínculo com reservas ou operações ativas, o sistema impedirá a exclusão e exibirá uma mensagem explicativa.
