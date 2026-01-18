# CDU19 – Relatório de Serviços Mais Consumidos

**Descrição:** Permite gerar um relatório com os serviços adicionais mais consumidos pelos hóspedes em um determinado período.

**Ator Primário:** Administrador.

**Pré-condições:**  
- O administrador deve estar logado no sistema.

**Pós-condições:**  
- O relatório de serviços mais consumidos é exibido.

## Fluxo Principal

1. O administrador acessa a opção Relatório de Serviços Mais Consumidos no sistema.
2. O sistema exibe o formulário para seleção do período.
3. O administrador informa o período desejado.
4. O administrador solicita a geração do relatório.
5. O sistema processa os dados de serviços consumidos.
6. O sistema exibe o relatório com os serviços mais consumidos.

## Fluxos de Exceção

- **FE1 – Período inválido:**  
  Se o período informado for inválido, o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Nenhum dado encontrado:**  
  Se não houver registros de serviços consumidos no período informado, o sistema exibirá uma mensagem informando a ausência de dados.
