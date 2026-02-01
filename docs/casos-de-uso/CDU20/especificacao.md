# CDU20 – Pedir Serviços Adicionais

**Descrição:** Permite que o hóspede, através de seu próprio acesso, solicite itens de consumo (como frigobar ou lavanderia) para sua estadia atual.

**Ator Primário:** Hóspede.

**Pré-condições:** 
- O hóspede deve estar logado no sistema.
- Deve existir uma reserva ativa vinculada a este hóspede.

**Pós-condições:** 
- O serviço solicitado é registrado e o valor é somado à conta da reserva.

## Fluxo Principal

1. O hóspede acessa o sistema e seleciona a opção "Consumo" (ou Pedir Serviços) no menu lateral.
2. O sistema exibe o formulário de solicitação.
3. O hóspede seleciona o serviço desejado na lista de itens disponíveis.
4. O hóspede informa a quantidade e confirma a solicitação.
5. O sistema registra o pedido no banco de dados, vinculando-o à reserva ativa.
6. O sistema exibe uma mensagem de sucesso confirmando a operação.

## Fluxos de Exceção

- **FE1 – Reserva inexistente ou inativa:** Se o sistema não identificar uma reserva ativa para o usuário logado, exibirá uma mensagem informando que não é possível solicitar serviços.

- **FE2 – Serviço indisponível:** Se o item selecionado não estiver cadastrado ou ativo no sistema, o pedido não será concluído.