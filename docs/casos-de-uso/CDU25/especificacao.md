# CDU25 – Iniciar Sessão

**Descrição:** Permite que o usuário (Administrador, Recepcionista ou Hóspede) se autentique no sistema para acessar suas funcionalidades específicas.

**Ator Primário:** Visitante.

**Pré-condições:** 
- O usuário deve possuir um cadastro ativo no banco de dados.

**Pós-condições:** 
- O usuário é autenticado, a sessão é iniciada e o menu lateral é atualizado conforme o perfil (permissões).

## Fluxo Principal

1. O usuário acessa o sistema.
2. O sistema exibe o formulário de login na tela inicial ou barra lateral.
3. O usuário informa seu **e-mail** e **senha**.
4. O usuário clica no botão "Entrar" (ou Login).
5. O sistema consulta o banco de dados para validar as credenciais.
6. O sistema identifica o perfil do usuário (Admin, Recepcionista, etc.) e armazena na sessão.
7. O sistema recarrega a interface, exibindo as opções de menu correspondentes ao perfil autenticado.

## Fluxos de Exceção

- **FE1 – Credenciais inválidas:** Se o e-mail não existir ou a senha estiver incorreta, o sistema exibe a mensagem "E-mail ou senha inválidos" e mantém o usuário na tela de login.

- **FE2 – Campos vazios:** Se o usuário tentar logar sem preencher os campos, o sistema alerta sobre o preenchimento obrigatório.