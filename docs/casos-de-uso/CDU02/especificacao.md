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

### Inserir Usuário

1. O administrador preenche os campos: Nome, Email, Telefone, Senha, Tipo de Perfil e ID Externo do Perfil (opcional).
2. O administrador clica em "Inserir".
3. O sistema valida se Nome, Email e Senha estão preenchidos.
4. O sistema verifica se o Email já está em uso.
5. O sistema insere o novo usuário no banco de dados.
6. O sistema exibe mensagem de sucesso e atualiza a lista.

### Atualizar Usuário

1. O administrador seleciona um usuário da lista.
2. O sistema preenche os campos com os dados atuais.
3. O administrador edita os campos desejados (Nome, Email, Telefone, Tipo de Perfil, ID Externo).
4. O administrador clica em "Salvar Alterações".
5. O sistema verifica se o Email já está em uso por outro usuário.
6. O sistema atualiza os dados no banco de dados.
7. O sistema exibe mensagem de sucesso e atualiza a lista.

### Alterar Senha

1. O administrador seleciona um usuário da lista.
2. O administrador informa a nova senha.
3. O administrador clica em "Alterar Senha".
4. O sistema valida se a senha foi informada.
5. O sistema atualiza a senha no banco de dados.
6. O sistema exibe mensagem de sucesso.

### Excluir Usuário

1. O administrador seleciona um usuário da lista.
2. O administrador clica em "Excluir".
3. O sistema remove o usuário do banco de dados.
4. O sistema exibe mensagem de sucesso e atualiza a lista.

## Fluxos de Exceção

- **FE1 – Dados inválidos:**  
  Se o administrador informar dados inválidos ou obrigatórios em branco (Nome, Email, Senha), o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Usuário já existente:**  
  Se o administrador tentar cadastrar ou atualizar um usuário com email já existente, o sistema exibirá uma mensagem informando o conflito.

- **FE3 – Exclusão não permitida:**  
  (Não implementado) Se o administrador tentar excluir um usuário que possua vínculo com reservas ou operações ativas, o sistema impedirá a exclusão e exibirá uma mensagem explicativa.
