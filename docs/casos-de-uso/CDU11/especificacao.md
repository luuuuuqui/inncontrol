# CDU11 – Listar Reservas

**Descrição:** Permite visualizar todas as reservas cadastradas no sistema, facilitando o controle de ocupação.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O usuário deve estar logado no sistema.

**Pós-condições:** 
- A lista de reservas é exibida para consulta.

## Fluxo Principal

1. O administrador acessa a opção Listar Reservas no sistema.
2. O sistema busca os dados de todas as reservas no banco de dados.
3. O sistema exibe a lista completa (Hóspede, Quarto, Datas e Status).
4. O administrador visualiza as informações na tela.

## Fluxos de Exceção

- **FE1 – Nenhuma reserva encontrada:** Se não existir nenhuma reserva cadastrada, o sistema exibirá uma mensagem informando que não há registros para exibir.