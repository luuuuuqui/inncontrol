# CDU12 – Cancelar Reserva

**Descrição:** Permite que o usuário cancele uma reserva existente, respeitando as regras de prazo definidas pelo sistema.

**Ator Primário:** Administrador, Recepcionista ou Hóspede.

**Pré-condições:**  
- O usuário deve estar logado no sistema.
- Deve existir uma reserva ativa no sistema.

**Pós-condições:**  
- A reserva é cancelada no sistema.

## Fluxo Principal

1. O usuário acessa a opção Cancelar Reserva no sistema.
2. O sistema exibe a lista de reservas disponíveis para cancelamento.
3. O usuário seleciona a reserva que deseja cancelar.
4. O sistema exibe os detalhes da reserva e as regras de cancelamento.
5. O sistema solicita a confirmação do cancelamento.
6. O usuário confirma o cancelamento.
7. O sistema cancela a reserva.
8. O sistema exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Cancelamento fora do prazo:**  
  Se a reserva não puder ser cancelada por estar fora do prazo permitido, o sistema exibirá uma mensagem informando o motivo.

- **FE2 – Cancelamento cancelado pelo usuário:**  
  Se o usuário desistir da operação, o sistema não realizará o cancelamento e retornará à lista de reservas.
