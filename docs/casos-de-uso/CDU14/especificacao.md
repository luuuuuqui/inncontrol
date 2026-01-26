# CDU14 – Realizar Check-out

**Descrição:** Permite finalizar a estadia do hóspede, calcular o valor total da hospedagem e registrar o encerramento da conta.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.
- Deve existir uma reserva com status “em andamento”.

**Pós-condições:** 
- A estadia é finalizada no sistema.
- O valor total é calculado e registrado.

## Fluxo Principal

1. O administrador acessa a opção de Check-out no sistema.
2. O sistema exibe a lista de reservas que estão com status "em andamento".
3. O administrador seleciona a reserva do hóspede que está saindo.
4. O sistema calcula o valor total da estadia com base nas diárias.
5. O sistema exibe o resumo financeiro para conferência.
6. O administrador confirma a finalização do check-out.
7. O sistema altera o status da reserva para finalizada.
8. O sistema exibe uma mensagem de sucesso confirmando a operação.

## Fluxos de Exceção

- **FE1 – Reserva inválida:** Se a reserva selecionada não estiver em andamento, o sistema impedirá a operação e exibirá uma mensagem de erro.

- **FE2 – Desistência da operação:** Se o administrador não confirmar a finalização, o sistema mantém a reserva em aberto e retorna à tela anterior.