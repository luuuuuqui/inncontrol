# CDU19 – Relatório de Serviços Mais Consumidos

**Descrição:** Permite ao administrador gerar e visualizar um relatório consolidado que identifica os serviços e produtos adicionais com maior volume de consumo em um intervalo de tempo específico.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar autenticado no sistema.
- Devem existir registros de consumo no banco de dados para o período selecionado.

**Pós-condições:** 
- O relatório é exibido na tela com a listagem dos itens e suas respectivas quantidades totais consumidas.

## Fluxo Principal

1. O administrador acessa a opção **Relatórios** no menu lateral.
2. O sistema exibe o painel de relatórios e o administrador seleciona a aba correspondente aos **Serviços Mais Consumidos**.
3. O administrador informa a **Data Inicial** e a **Data Final** para o filtro.
4. O administrador clica no botão para gerar o relatório.
5. O sistema realiza a busca no banco de dados, agrupando os consumos por serviço e somando suas quantidades.
6. O sistema exibe o relatório formatado em uma tabela na interface.

## Fluxos de Exceção

- **FE1 – Período inválido:** Se a data inicial for posterior à data final, o sistema impedirá o processamento e exibirá uma mensagem de erro solicitando a correção das datas.
- **FE2 – Nenhum dado encontrado:** Caso não existam lançamentos de consumo no intervalo de tempo informado, o sistema exibirá a mensagem "Nenhum registro encontrado para este período.".