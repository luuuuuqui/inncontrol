# CDU12 – Cancelar Reserva

**Descrição:** Permite que o usuário realize o cancelamento de uma reserva existente no sistema.

**Ator Primário:** Administrador ou Hóspede.

**Pré-condições:** 
- O usuário deve estar logado no sistema.
- Deve existir uma reserva cadastrada vinculada ao usuário ou acessível pelo administrador.

**Pós-condições:** 
- O status da reserva é alterado para "Cancelado" no banco de dados.

## Fluxo Principal

1. O usuário acessa a opção de gerenciamento de reservas ou seu perfil pessoal.
2. O sistema exibe a lista de reservas disponíveis.
3. O usuário seleciona a reserva que deseja cancelar.
4. O usuário solicita o cancelamento da reserva selecionada.
5. O sistema solicita a confirmação da operação.
6. O usuário confirma o cancelamento.
7. O sistema atualiza o status da reserva para cancelado.
8. O sistema exibe uma mensagem de sucesso confirmando a operação.

## Fluxos de Exceção

- **FE1 – Reserva já cancelada:** Se o usuário tentar cancelar uma reserva que já está cancelada, o sistema informará que a operação já foi realizada.

- **FE2 – Desistência do usuário:** Se o usuário não confirmar a operação, o sistema mantém a reserva como estava e retorna à tela anterior.