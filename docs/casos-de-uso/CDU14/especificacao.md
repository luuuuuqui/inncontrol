# CDU14 – Realizar Check-out

**Descrição:** Permite finalizar a estadia do hóspede, realizando o cálculo automático do valor total (diárias e consumos) e registrando o encerramento da conta no sistema.

**Ator Primário:** Administrador e Recepcionista.

**Pré-condições:** 
- O usuário deve estar logado no sistema.
- Deve existir uma reserva com status indicando que a estadia está em curso.

**Pós-condições:** 
- A reserva é finalizada e o registro de pagamento é gerado com o valor total calculado.

## Fluxo Principal

1. O usuário acessa a opção de gestão de reservas ou pagamentos no menu lateral.
2. O sistema exibe a lista de reservas ativas.
3. O usuário seleciona a reserva do hóspede que deseja realizar o check-out.
4. O sistema calcula automaticamente o valor total da estadia, multiplicando o valor da diária pelo número de dias e somando todos os itens de consumo registrados.
5. O sistema exibe o resumo financeiro para conferência do usuário.
6. O usuário registra o pagamento informando a data, forma de pagamento e status.
7. O sistema altera o status da reserva para finalizada (ou equivalente) e salva o registro financeiro.
8. O sistema exibe uma mensagem de sucesso confirmando a operação.

## Fluxos de Exceção

- **FE1 – Reserva já paga:** Se o usuário tentar registrar um pagamento para uma reserva que já possui um registro financeiro vinculado, o sistema exibirá uma mensagem de erro informando que o pagamento já existe.

- **FE2 – Erro no cálculo de datas:** Se as datas de check-in e check-out da reserva apresentarem inconsistências, o sistema impedirá o cálculo do valor e exibirá uma mensagem de erro.

- **FE3 – Itens de consumo sem valor:** Se houver um item de consumo vinculado a um adicional que foi removido, o sistema poderá ignorar o item no cálculo total para evitar erros de processamento.