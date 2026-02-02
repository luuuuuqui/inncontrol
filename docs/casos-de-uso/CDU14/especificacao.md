# CDU14 – Cadastrar Hóspede

**Descrição:** Permite vincular dados de endereço a um usuário já existente no sistema, habilitando-o para realizar reservas e estadias.

**Ator Primário:** Administrador e Recepcionista.

**Pré-condições:** 
- O funcionário deve estar autenticado no sistema.
- Deve existir uma conta de usuário cadastrada que ainda não possua perfil de hóspede.

**Pós-condições:** 
- O perfil de hóspede é criado e vinculado ao usuário selecionado.

## Fluxo Principal

1. O usuário acessa a opção "Hóspede" no menu lateral.
2. O sistema exibe o painel de gerenciamento e o usuário seleciona a aba "Inserir".
3. O usuário seleciona a conta do usuário que deseja tornar hóspede em uma lista de seleção.
4. O usuário informa o endereço completo do hóspede.
5. O usuário confirma o cadastro clicando no botão "Inserir".
6. O sistema valida se o endereço foi preenchido corretamente.
7. O sistema valida se o usuário escolhido já não possui um perfil de hóspede vinculado.
8. O sistema registra o vínculo e exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Dados inválidos:** Se o endereço for deixado em branco ou nenhum usuário for selecionado, o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Hóspede já cadastrado:** Se o usuário selecionado já possuir um cadastro de hóspede ativo, o sistema exibirá a mensagem "Este usuário já possui cadastro de hóspede."