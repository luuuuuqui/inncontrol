# CDU23 – Atualizar Tarifas em Lote

**Descrição:** Permite atualizar os valores das tarifas dos quartos em lote para um determinado período ou tipo de quarto.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.
- Deve existir tipo de quarto cadastrado no sistema.

**Pós-condições:** 
- As tarifas dos quartos são atualizadas conforme os critérios definidos.

## Fluxo Principal

1. O administrador acessa a opção Atualizar Tarifas em Lote no sistema.
2. O sistema exibe o formulário de atualização de tarifas.
3. O administrador seleciona o tipo de quarto e o período desejado.
4. O administrador informa o novo valor da tarifa.
5. O administrador confirma a atualização.
6. O sistema valida os dados informados.
7. O sistema atualiza as tarifas dos quartos em lote.
8. O sistema exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Valor inválido:** Se o valor informado for inválido, o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Nenhum quarto afetado:** Se não houver quartos que atendam aos critérios informados, o sistema exibirá uma mensagem informando que nenhuma tarifa foi atualizada.