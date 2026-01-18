# CDU18 – Listar Serviços da Reserva

**Descrição:** Permite visualizar todos os serviços adicionais consumidos em uma reserva específica.

**Ator Primário:** Administrador ou Recepcionista.

**Pré-condições:**  
- O usuário deve estar logado no sistema.
- Deve existir uma reserva cadastrada no sistema.

**Pós-condições:**  
- Os serviços consumidos da reserva são exibidos.

## Fluxo Principal

1. O usuário acessa a opção Listar Serviços da Reserva no sistema.
2. O sistema exibe a lista de reservas cadastradas.
3. O usuário seleciona a reserva desejada.
4. O sistema exibe os serviços consumidos vinculados à reserva.
5. O sistema exibe os detalhes dos serviços (nome, quantidade e valor).

## Fluxos de Exceção

- **FE1 – Reserva inexistente:**  
  Se a reserva selecionada não existir, o sistema exibirá uma mensagem de erro.

- **FE2 – Nenhum serviço registrado:**  
  Se a reserva não possuir serviços registrados, o sistema exibirá uma mensagem informando que não há serviços consumidos.
