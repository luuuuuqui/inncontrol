# CDU13 – Realizar Check-in

**Descrição:** Permite confirmar a entrada do hóspede no hotel, alterando o status da reserva para “em andamento”.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.
- Deve existir uma reserva confirmada para o hóspede.
- A data de entrada deve ser compatível com a data atual.

**Pós-condições:** 
- O status da reserva é atualizado para “em andamento”.

## Fluxo Principal

1. O administrador acessa a opção Realizar Check-in no sistema.
2. O sistema exibe a lista de reservas confirmadas.
3. O administrador seleciona a reserva do hóspede.
4. O sistema exibe os dados da reserva.
5. O administrador confirma o check-in.
6. O sistema atualiza o status da reserva para "em andamento".
7. O sistema exibe uma mensagem de sucesso confirmando a operação.

## Fluxos de Exceção

- **FE1 – Reserva inexistente ou inválida:** Se a reserva não existir ou não estiver confirmada, o sistema exibirá uma mensagem de erro.

- **FE2 – Data incompatível:** Se a data atual não corresponder à data de entrada da reserva, o sistema impedirá o check-in e exibirá uma mensagem informativa.