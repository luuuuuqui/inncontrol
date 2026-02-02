# CDU05 – Manter Tipo de Quarto

**Descrição:** Permite que o administrador gerencie os tipos de quarto no sistema, incluindo listar, inserir, atualizar e excluir tipos de quarto.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O usuário deve estar logado como administrador no sistema.

**Pós-condições:** 
- Os tipos de quarto estarão atualizados no banco de dados conforme as operações realizadas.

## Fluxo Principal

1. O administrador acessa a interface de gerenciamento de tipos de quarto.
2. O sistema exibe a aba "Listar" com todos os tipos cadastrados (ID, Nome, Descrição, Capacidade e Valor da Diária).
3. O administrador seleciona a aba desejada para Inserir, Atualizar ou Excluir.
4. O administrador preenche os campos necessários ou seleciona o registro na lista.
5. O administrador clica no botão correspondente à ação.
6. O sistema valida os dados fornecidos.
7. O sistema executa a operação no banco de dados.
8. O sistema exibe uma mensagem de sucesso e recarrega a interface.

## Fluxos de Exceção

- **FE1 – Campos obrigatórios não preenchidos:** Se algum campo obrigatório não for preenchido, o sistema exibirá uma mensagem solicitando o preenchimento total.

- **FE2 – Nome duplicado:** Se o nome do tipo de quarto já existir no sistema, o administrador será informado do conflito.

- **FE3 – Dados inválidos:** Se a capacidade ou o valor da diária forem preenchidos com valores negativos ou em formato incorreto, o sistema exibirá uma mensagem de erro.

- **FE4 – Erro inesperado:** Em caso de falha na comunicação com o banco de dados, o sistema exibirá uma mensagem detalhando o erro ocorrido.