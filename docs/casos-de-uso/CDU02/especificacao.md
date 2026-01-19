# CDU02 – Gerenciar Usuários

**Descrição:** Permite que o administrador gerencie os usuários do sistema, podendo listar, cadastrar, atualizar, alterar senha e excluir usuários.

**Ator Primário:** Administrador.

**Pré-condições:**  

- O administrador deve estar logado no sistema.

**Pós-condições:**  

- Usuários cadastrados, atualizados, senha alterada ou removidos conforme a ação executada.

## Fluxo Principal

1. O administrador acessa a opção "Usuário" no menu lateral.
2. O sistema exibe abas para as operações: Listar, Inserir, Atualizar, Alterar Senha, Excluir.
3. O administrador seleciona uma aba conforme a ação desejada.

### Listar Usuários

1. O sistema exibe uma tabela com os usuários cadastrados, mostrando ID, Nome, Email, Telefone e Tipo de Perfil.
2. Se não houver usuários, exibe mensagem informativa.

### Operações de Gerenciamento

Para inserir, atualizar, alterar senha ou excluir usuários:

1. O administrador faz as alterações necessárias nos campos ou seleciona o usuário.
2. O administrador clica no botão correspondente à ação (Inserir, Salvar Alterações, Alterar Senha ou Excluir).
3. O sistema valida os dados fornecidos.
4. Se válido, o sistema executa a operação no banco de dados e exibe uma mensagem de sucesso.
5. O sistema atualiza a lista de usuários.

## Fluxos de Exceção

- **FE1 – Dados inválidos:**  
  Se o administrador informar dados inválidos ou obrigatórios em branco (Nome, Email, Senha), o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Usuário já existente:**  
  Se o administrador tentar cadastrar ou atualizar um usuário com email já existente, o sistema exibirá uma mensagem informando o conflito.

- **FE3 – Exclusão não permitida:**  
  (Não implementado) Se o administrador tentar excluir um usuário que possua vínculo com reservas ou operações ativas, o sistema impedirá a exclusão e exibirá uma mensagem explicativa.
