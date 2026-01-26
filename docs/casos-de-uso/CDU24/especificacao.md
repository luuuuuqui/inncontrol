# CDU24 – Pedir Serviços Adicionais

**Descrição:** Permite que o hóspede solicite serviços adicionais durante sua estadia.

**Ator Primário:** Hóspede.

**Pré-condições:** 
- O hóspede deve estar logado no sistema.
- Deve possuir uma reserva ativa.

**Pós-condições:** 
- O serviço solicitado será registrado e associado à reserva do hóspede.

## Fluxo Principal

1. O hóspede acessa a página inicial do sistema.
2. No menu lateral, o hóspede seleciona a opção "Pedir Serviços Adicionais".
3. O sistema exibe a lista de serviços disponíveis.
4. O hóspede seleciona o serviço desejado.
5. O hóspede confirma a solicitação.
6. O sistema registra o serviço solicitado no banco de dados.
7. O sistema exibe uma mensagem de sucesso confirmando a operação.

## Fluxos de Exceção

- **FE1 – Reserva inexistente ou inativa:** Se o hóspede não possuir uma reserva ativa, o sistema exibirá uma mensagem informando que não é possível solicitar serviços adicionais.

- **FE2 – Serviço indisponível:** Se o serviço selecionado não estiver disponível, o sistema exibirá uma mensagem informando a indisponibilidade.