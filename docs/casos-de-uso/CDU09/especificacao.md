# CDU09 – Realizar Reserva

**Descrição:** Permite o registro de uma nova reserva no sistema, vinculando um hóspede a um quarto em um período específico.

**Ator Primário:** Administrador e Recepcionista.

**Pré-condições:** 
- O usuário deve estar logado no sistema.
- Devem existir hóspedes e quartos cadastrados.

**Pós-condições:** 
- A reserva é registrada e fica disponível para consulta e check-in.

## Fluxo Principal

1. O usuário acessa a opção "Reserva" no menu lateral.
2. O sistema exibe o painel de reservas e o usuário seleciona a aba "Inserir".
3. O usuário seleciona o hóspede e o quarto desejado nas listas exibidas.
4. O usuário informa o período de estadia (data de check-in e data de check-out).
5. O usuário seleciona o status inicial da reserva (ex: Pendente ou Confirmada).
6. O usuário confirma a operação clicando no botão "Inserir Reserva".
7. O sistema valida se o quarto está disponível no período e se as datas são consistentes.
8. O sistema registra a reserva e exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Quarto indisponível:** Se o quarto selecionado já possuir uma reserva que se sobreponha ao período escolhido, o sistema exibirá a mensagem "Quarto indisponível!" informando o período ocupado.

- **FE2 – Datas inconsistentes:** Se a data de check-in for igual ou posterior à data de check-out, o sistema exibirá uma mensagem de erro informando que o check-in deve ser anterior ao check-out.

- **FE3 – Cadastros insuficientes:** Se não houver hóspedes ou quartos cadastrados, o sistema exibirá um aviso informando que é necessário realizar esses cadastros antes de criar uma reserva.