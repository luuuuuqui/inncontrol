# CDU01 – Iniciar Sessão

**Descrição:** Permite que o usuário faça login no sistema.

**Ator Primário:** Visitante.

**Pré-condições:** O visitante deve ter uma conta no sistema.

**Pós-condições:** Usuário estará logado.  

## Fluxo Principal

1. O usuário acessa a página inicial do sistema.
2. No menu lateral, o usuário seleciona a opção "Entrar no Sistema".
3. O sistema exibe um formulário de login com campos para e-mail e senha.
4. O usuário preenche os campos de e-mail e senha.
5. O usuário clica no botão "Entrar" ou pressiona a tecla Enter.
6. O sistema verifica as credenciais no banco de dados.
7. Se as credenciais forem válidas, o sistema armazena os dados do usuário na sessão (ID, nome, tipo de perfil) e exibe uma mensagem de sucesso.
8. O sistema redireciona o usuário para o menu apropriado com base no tipo de perfil (administrador ou outro).

## Fluxos De Exceção

- **FE1 – Dados inválidos:**  
  Se o usuário digitar um email ou senha incorreto, o sistema irá exibir uma mensagem de erro avisando que o login foi inválido e solicitará outra tentativa.

- **FE2 – Campos obrigatórios não preenchidos:**  
  Se o usuário não preencher o e-mail ou a senha, o sistema irá exibir uma mensagem de aviso solicitando o preenchimento dos campos.