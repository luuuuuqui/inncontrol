# CDU11 – Listar Reservas

**Descrição:** Permite visualizar todas as reservas cadastradas no sistema, com opções de filtro por período, status e hóspede.

**Ator Primário:** Administrador ou Recepcionista.

**Pré-condições:**  
- O usuário deve estar logado no sistema.

**Pós-condições:**  
- A lista de reservas é exibida conforme os filtros aplicados.

## Fluxo Principal

1. O usuário acessa a opção Listar Reservas no sistema.
2. O sistema exibe a lista de todas as reservas cadastradas.
3. O usuário pode aplicar filtros por período, status ou hóspede.
4. O sistema atualiza a lista conforme os filtros selecionados.
5. O sistema exibe as reservas correspondentes à busca.

## Fluxos de Exceção

- **FE1 – Nenhuma reserva encontrada:**  
  Se não existir nenhuma reserva que atenda aos filtros informados, o sistema exibirá uma mensagem informando que não há reservas a serem exibidas.
