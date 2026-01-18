# CDU14 – Realizar Check-out

**Descrição:** Permite finalizar a estadia do hóspede, calcular o valor total da hospedagem e gerar o pagamento.

**Ator Primário:** Recepcionista.

**Pré-condições:**  
- O recepcionista deve estar logado no sistema.
- Deve existir uma reserva com status “em andamento”.

**Pós-condições:**  
- A estadia é finalizada.
- O valor total é calculado.
- O pagamento é gerado.

## Fluxo Principal

1. O recepcionista acessa a opção Realizar Check-out no sistema.
2. O sistema exibe a lista de reservas em andamento.
3. O recepcionista seleciona a reserva do hóspede.
4. O sistema calcula o valor total da estadia (diárias + serviços consumidos).
5. O sistema exibe o valor total a ser pago.
6. O recepcionista confirma o check-out.
7. O sistema finaliza a estadia e registra o pagamento.
8. O sistema exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Pagamento não confirmado:**  
  Se o pagamento não for confirmado, o sistema não finalizará o check-out e exibirá uma mensagem informativa.

- **FE2 – Reserva inválida:**  
  Se a reserva não estiver em andamento, o sistema impedirá o check-out e exibirá uma mensagem de erro.
