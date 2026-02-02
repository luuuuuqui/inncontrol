# CDU15 – Abrir Conta

**Descrição:** Permite que um visitante realize seu próprio cadastro no sistema.

**Ator Primário:** Visitante.

**Pré-condições:** - O visitante deve acessar o sistema.

**Pós-condições:** - Perfil de usuário criado para futuras reservas e serviços.

## Fluxo Principal

1. O visitante seleciona a opção "Criar Conta".
2. O visitante preenche Nome, E-mail e Senha.
3. O visitante informa dados de endereço e contato.
4. O sistema valida se o e-mail já existe.
5. O sistema cria o registro e confirma o sucesso.

## Fluxos de Exceção

- **FE1 – E-mail já cadastrado:** O sistema impede a criação e solicita um novo e-mail.
- **FE2 – Campos vazios:** O sistema alerta que todos os campos são obrigatórios.