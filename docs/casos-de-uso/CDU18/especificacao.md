# CDU18 – Listar Serviços da Reserva

**Descrição:** Permite visualizar todos os serviços adicionais consumidos em uma reserva específica.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.
- Deve existir uma reserva cadastrada no sistema.

**Pós-condições:** 
- Os serviços consumidos da reserva são exibidos.

## Fluxo Principal

1. O administrador acessa a opção Listar Serviços da Reserva no sistema.
2. O sistema exibe a lista de reservas cadastradas.
3. O administrador seleciona a reserva desejada.
4. O sistema busca e exibe os serviços consumidos vinculados à reserva.
5. O sistema detalha os serviços informando nome, quantidade e valor unitário.

## Fluxos de Exceção

- **FE1 – Reserva inexistente:** Se a reserva selecionada não for encontrada no banco de dados, o sistema exibirá uma mensagem de erro.

- **FE2 – Nenhum serviço registrado:** Se a reserva não possuir serviços adicionais lançados, o sistema exibirá uma mensagem informando que não há registros de consumo.