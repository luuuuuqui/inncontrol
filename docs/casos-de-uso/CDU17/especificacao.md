# CDU17 – Registrar Serviço Consumido

**Descrição:** Permite registrar os serviços adicionais consumidos pelo hóspede durante a estadia, vinculando-os à reserva.

**Ator Primário:** Recepcionista.

**Pré-condições:**  
- O recepcionista deve estar logado no sistema.
- Deve existir uma reserva em andamento.

**Pós-condições:**  
- O serviço consumido é registrado na reserva.

## Fluxo Principal

1. O recepcionista acessa a opção Registrar Serviço Consumido no sistema.
2. O sistema exibe a lista de reservas em andamento.
3. O recepcionista seleciona a reserva do hóspede.
4. O sistema exibe os serviços adicionais disponíveis.
5. O recepcionista seleciona o serviço consumido e informa a quantidade.
6. O sistema registra o serviço na reserva.
7. O sistema atualiza o valor total da estadia.
8. O sistema exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Reserva inválida:**  
  Se a reserva não estiver em andamento, o sistema impedirá o registro do serviço.

- **FE2 – Serviço não selecionado:**  
  Se nenhum serviço for selecionado, o sistema exibirá uma mensagem solicitando a correção.
