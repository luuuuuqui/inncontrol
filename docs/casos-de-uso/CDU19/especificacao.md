# CDU19 – Histórico de Estadias

**Descrição:** Permite visualizar detalhadamente todas as estadias passadas e atuais de um hóspede no sistema, incluindo períodos e valores.

**Ator Primário:** Administrador e Recepcionista.

**Pré-condições:** 
- O usuário deve estar logado no sistema.
- O hóspede deve possuir pelo menos uma reserva (ativa ou finalizada) no banco de dados.

**Pós-condições:** 
- O histórico completo de movimentações do hóspede é exibido para consulta.

## Fluxo Principal

1. O usuário acessa a opção de consultas ou relatórios de estadias no menu lateral.
2. O sistema exibe o painel de histórico.
3. O usuário seleciona o hóspede desejado através de uma lista ou campo de pesquisa.
4. O sistema recupera todas as reservas vinculadas àquele hóspede no banco de dados.
5. O sistema exibe a lista cronológica contendo informações como: Quarto, Data de Entrada, Data de Saída, Status e Valor Total.

## Fluxos de Exceção

- **FE1 – Hóspede não selecionado:** Se o usuário tentar realizar a busca sem definir um hóspede, o sistema solicitará a seleção obrigatória.

- **FE2 – Nenhum histórico encontrado:** Se o hóspede selecionado não possuir registros de reserva, o sistema exibirá a mensagem "Nenhum histórico disponível para este hóspede.".