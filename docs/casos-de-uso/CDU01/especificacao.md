# CDU01 – Iniciar Sessão

**Descrição:** Permite que o usuário faça login no sistema para acessar funcionalidades restritas de acordo com seu nível de permissão.

**Ator Primário:** Visitante (Administrador, Recepcionista ou Hóspede).

**Pré-condições:** 
- O usuário deve possuir uma conta cadastrada no sistema.

**Pós-condições:** 
- O usuário é autenticado e redirecionado para o menu correspondente ao seu perfil.

## Fluxo Principal

1. O usuário acessa a página inicial do sistema.
2. No menu lateral, o usuário seleciona a opção "Entrar no Sistema".
3. O sistema exibe o formulário de login solicitando e-mail e senha.
4. O usuário preenche as credenciais e confirma o acesso.
5. O sistema valida se o e-mail e a senha informados estão corretos.
6. O sistema identifica o perfil do usuário e inicia a sessão.
7. O sistema exibe uma mensagem de sucesso informando que o login foi realizado.
8. O sistema exibe o menu de opções específico para o perfil do usuário (Administrador, Recepcionista ou Hóspede).

## Fluxos de Exceção

- **FE1 – Credenciais inválidas:** Caso o e-mail ou a senha estejam incorretos, o sistema exibe a mensagem "E-mail ou senha inválidos".

- **FE2 – Campos não preenchidos:** Se o usuário tentar entrar sem preencher o e-mail ou a senha, o sistema exibe um alerta solicitando o preenchimento dos campos.

- **FE3 – Perfil não reconhecido:** Se o tipo de conta do usuário não for identificado, o sistema exibe uma mensagem orientando o contato com o suporte.