# CDU05 – Manter Tipo de Quarto

**Descrição:** Permite que o administrador gerencie os tipos de quarto no sistema, podendo listar, cadastrar, atualizar e excluir tipos de quarto.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.

**Pós-condições:** 
- Os tipos de quarto são atualizados no sistema conforme a ação realizada.

## Fluxo Principal

1. O administrador acessa a opção "Tipo de Quarto" no menu lateral.
2. O sistema exibe o painel com as abas: Listar, Inserir, Atualizar, Excluir.
3. O sistema exibe na aba "Listar" todos os tipos cadastrados com ID, Nome, Descrição, Capacidade e Valor da Diária.
4. O administrador seleciona a aba correspondente à operação desejada.
5. O administrador preenche os campos solicitados ou seleciona um tipo existente na lista.
6. O administrador clica no botão correspondente à ação (Inserir, Salvar Alterações ou Excluir).
7. O sistema valida os dados e a integridade das informações.
8. O sistema executa a operação e exibe uma mensagem de sucesso, atualizando a interface.

## Fluxos de Exceção

- **FE1 – Campos obrigatórios não preenchidos:** Se o administrador tentar inserir ou atualizar sem preencher todos os campos, o sistema exibe a mensagem "Preencha todos os campos.".

- **FE2 – Nome duplicado:** Se o administrador tentar cadastrar ou atualizar um tipo de quarto com um nome que já existe, o sistema informará que o item já está cadastrado.

- **FE3 – Dados inválidos:** Se forem informados valores negativos para a diária ou capacidade igual ou inferior a zero, o sistema exibirá uma mensagem de erro impedindo a gravação.

- **FE4 – Erro inesperado:** Caso ocorra uma falha durante o processamento, o sistema exibirá uma mensagem detalhando o erro.