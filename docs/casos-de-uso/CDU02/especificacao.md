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
3. O administrador seleciona a aba conforme a ação desejada.
4. O administrador realiza as alterações necessárias nos campos ou seleciona o usuário.
5. O administrador clica no botão correspondente à ação (Inserir, Salvar Alterações, Alterar Senha ou Excluir).
6. O sistema valida os dados fornecidos.
7. O sistema executa a operação solicitada.
8. O sistema exibe uma mensagem de sucesso e atualiza a lista de usuários.

## Fluxos de Exceção

- **FE1 – Dados inválidos:** Se o administrador informar dados inválidos ou deixar campos obrigatórios em branco, o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Usuário já existente:** Se o administrador tentar cadastrar ou atualizar um usuário com e-mail já existente, o sistema exibirá uma mensagem informando o conflito.

- **FE3 – Exclusão não permitida:** Se o administrador tentar excluir um usuário que possua vínculo com outras operações, o sistema impedirá a exclusão e exibirá uma mensagem de erro.