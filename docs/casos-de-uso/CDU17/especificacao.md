# CDU18 – Listar Serviços da Reserva

**Descrição:** Permite visualizar detalhadamente todos os produtos e serviços adicionais que foram lançados como consumo em uma reserva específica.

**Ator Primário:** Administrador e Recepcionista.

**Pré-condições:** 
- O usuário deve estar logado no sistema.
- Devem existir registros de consumo vinculados a reservas.

**Pós-condições:** 
- Os detalhes do consumo (item, quantidade e reserva vinculada) são exibidos para conferência.

## Fluxo Principal

1. O usuário acessa a opção "Consumo" no menu lateral.
2. O sistema exibe por padrão a aba "Listar".
3. O sistema recupera todos os registros de consumo do banco de dados.
4. O sistema exibe uma tabela com as colunas: Identificador, Reserva, Adicional, Quantidade e Data.
5. O usuário identifica os serviços vinculados à reserva desejada através da coluna "Reserva".

## Fluxos de Exceção

- **FE1 – Nenhum serviço registrado:** Se não houver nenhum lançamento de consumo no sistema, a tabela será exibida vazia ou com a mensagem "Nenhum consumo cadastrado.".

- **FE2 – Erro na recuperação de dados:** Caso ocorra uma falha na conexão com o banco de dados ao tentar listar os serviços, o sistema exibirá uma mensagem de erro técnica.