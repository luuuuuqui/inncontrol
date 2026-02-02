# CDU01 – Iniciar Sessão

**Descrição:** Permite que o usuário faça login no sistema para acessar funcionalidades restritas.

**Ator Primário:** Visitante (Administrador ou Hóspede).

**Pré-condições:** 
- O usuário deve possuir uma conta cadastrada no sistema.

**Pós-condições:** 
- O usuário é autenticado e redirecionado para o menu correspondente ao seu perfil.

## Fluxo Principal

1. O usuário acessa a página inicial do sistema.
2. No menu lateral, o usuário seleciona a opção "Entrar no Sistema".
3. O sistema exibe o formulário de login (e-mail e senha).
4. O usuário preenche as credenciais e confirma o acesso.
5. O sistema valida as credenciais no banco de dados.
6. O sistema identifica o perfil do usuário e inicia a sessão.
7. O sistema exibe uma mensagem de sucesso e redireciona para o menu principal.

## Fluxos de Exceção

- **FE1 – Credenciais inválidas:** Se o e-mail ou a senha estiverem incorretos, o sistema exibirá uma mensagem de erro e solicitará uma nova tentativa.

- **FE2 – Campos não preenchidos:** Se o usuário tentar entrar sem preencher todos os campos, o sistema emitirá um alerta solicitando o preenchimento obrigatório.