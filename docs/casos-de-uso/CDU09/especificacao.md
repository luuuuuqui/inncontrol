# CDU09 – Realizar Reserva

**Descrição:** Permite que o hóspede realize a reserva de um quarto, selecionando datas, tipo de quarto e serviços adicionais.

**Ator Primário:** Hóspede.

**Pré-condições:**  
- O hóspede deve estar logado no sistema.
- Deve existir quarto disponível para o período selecionado.

**Pós-condições:**  
- A reserva é registrada no sistema.

## Fluxo Principal

1. O hóspede acessa a opção Realizar Reserva no sistema.
2. O sistema exibe os quartos disponíveis para o período informado.
3. O hóspede seleciona o quarto desejado.
4. O hóspede informa as datas de entrada e saída.
5. O hóspede pode selecionar serviços adicionais.
6. O sistema calcula o valor total da reserva.
7. O hóspede confirma a reserva.
8. O sistema registra a reserva.
9. O sistema exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Quarto indisponível:**  
  Se o quarto selecionado não estiver disponível para o período escolhido, o sistema exibirá uma mensagem informando a indisponibilidade.

- **FE2 – Dados inválidos:**  
  Se as datas informadas forem inválidas ou inconsistentes, o sistema exibirá uma mensagem de erro e solicitará a correção.
