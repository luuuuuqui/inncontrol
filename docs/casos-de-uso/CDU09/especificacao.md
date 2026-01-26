# CDU09 – Realizar Reserva

**Descrição:** Permite o registro de uma reserva no sistema, vinculando um hóspede a um quarto em um período específico.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.
- Devem existir hóspedes e quartos cadastrados no sistema.

**Pós-condições:** 
- A reserva é registrada no banco de dados.

## Fluxo Principal

1. O administrador acessa a opção Realizar Reserva no sistema.
2. O sistema exibe a lista de hóspedes e quartos cadastrados.
3. O administrador seleciona o hóspede que deseja vincular à reserva.
4. O administrador seleciona o quarto desejado.
5. O administrador informa o período de estadia (check-in e check-out).
6. O administrador define o status inicial da reserva (Pendente ou Confirmado).
7. O administrador confirma a reserva.
8. O sistema valida a disponibilidade do quarto para o período informado.
9. O sistema registra a reserva e exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Quarto indisponível:** Se o quarto selecionado já possuir uma reserva ativa para o período escolhido, o sistema exibirá uma mensagem de indisponibilidade.

- **FE2 – Dados inválidos:** Se as datas forem inconsistentes (ex: check-out anterior ao check-in) ou campos obrigatórios não forem preenchidos, o sistema exibirá uma mensagem de erro.