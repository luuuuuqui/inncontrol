# CDU11 – Listar Reservas

**Descrição:** Permite visualizar todas as reservas cadastradas no sistema, apresentando informações detalhadas sobre o hóspede, quarto, período de estadia e valores totais.

**Ator Primário:** Administrador e Recepcionista.

**Pré-condições:** 
- O usuário deve estar logado no sistema.

**Pós-condições:** 
- A lista de reservas é exibida para consulta e gestão da ocupação.

## Fluxo Principal

1. O usuário acessa a opção "Reserva" no menu lateral.
2. O sistema exibe por padrão a aba "Listar" com o painel de reservas.
3. O sistema recupera a lista de todas as reservas registradas, ordenadas por identificador.
4. O sistema exibe uma tabela contendo colunas como: Identificador (ID), Hóspede, Quarto, Check-in, Check-out, Valor Total e Status.
5. O usuário visualiza as informações na tela.

## Fluxos de Exceção

- **FE1 – Nenhuma reserva encontrada:** Se não houver registros de reservas no sistema, será exibida a mensagem "Nenhuma reserva cadastrada.".