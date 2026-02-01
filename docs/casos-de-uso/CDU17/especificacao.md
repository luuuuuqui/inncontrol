# CDU17 – Registrar Serviço Consumido

**Descrição:** Permite registrar o consumo de produtos ou serviços adicionais vinculando-os a uma reserva específica.

**Ator Primário:** Administrador e Recepcionista.

**Pré-condições:** 
- O usuário deve estar logado no sistema.
- Devem existir reservas e itens adicionais cadastrados no sistema.

**Pós-condições:** 
- O consumo é registrado e o valor total da reserva é atualizado.

## Fluxo Principal

1. O usuário acessa a opção "Consumo" no menu lateral.
2. O sistema exibe a interface e o usuário seleciona a aba "Inserir".
3. O usuário seleciona a reserva do hóspede em uma lista de seleção.
4. O usuário seleciona o item adicional consumido (produto ou serviço).
5. O usuário informa a quantidade consumida e a data do registro.
6. O usuário confirma a operação clicando no botão "Lançar Consumo".
7. O sistema valida se a quantidade informada é superior a zero.
8. O sistema registra o consumo, exibe uma mensagem de sucesso e atualiza a lista de consumos.

## Fluxos de Exceção

- **FE1 – Quantidade inválida:** Se o usuário informar uma quantidade igual ou inferior a zero, o sistema exibirá a mensagem "A quantidade deve ser maior que zero." e impedirá a gravação.

- **FE2 – Dados incompletos:** Se o usuário não selecionar uma reserva ou um item adicional, o sistema impedirá a confirmação do lançamento.