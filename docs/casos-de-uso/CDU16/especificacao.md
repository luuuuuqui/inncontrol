# CDU16 – Listar Hóspedes

**Descrição:** Permite visualizar a lista de hóspedes cadastrados no sistema, com opções de busca e filtro.

**Ator Primário:** Administrador ou Recepcionista.

**Pré-condições:**  
- O usuário deve estar logado no sistema.

**Pós-condições:**  
- A lista de hóspedes é exibida conforme os filtros aplicados.

## Fluxo Principal

1. O usuário acessa a opção Listar Hóspedes no sistema.
2. O sistema exibe a lista de hóspedes cadastrados.
3. O usuário pode realizar buscas por nome ou CPF.
4. O sistema atualiza a lista conforme os critérios informados.
5. O sistema exibe os hóspedes correspondentes à busca.

## Fluxos de Exceção

- **FE1 – Nenhum hóspede encontrado:**  
  Se não existir hóspede que atenda aos critérios informados, o sistema exibirá uma mensagem informando que não há registros.
