# CDU04 – Listar Quartos

**Descrição:** Permite visualizar todos os quartos cadastrados no sistema, com opção de filtros por tipo e disponibilidade.

**Ator Primário:** Administrador, Recepcionista ou Hóspede.

**Pré-condições:**  
- O usuário deve estar logado no sistema.

**Pós-condições:**  
- A lista de quartos é exibida conforme os filtros selecionados.

## Fluxo Principal

1. O usuário acessa a opção Listar Quartos no sistema.
2. O sistema exibe todos os quartos cadastrados.
3. O usuário pode selecionar filtros por tipo de quarto e disponibilidade.
4. O sistema atualiza a lista conforme os filtros aplicados.
5. O sistema exibe os quartos correspondentes à busca.

## Fluxos de Exceção

- **FE1 – Nenhum quarto encontrado:**  
  Se não existir nenhum quarto que atenda aos filtros informados, o sistema exibirá uma mensagem informando que não há quartos disponíveis.
