# CDU03 – Gerenciar Quartos

**Descrição:** Permite que o administrador gerencie os quartos do sistema, podendo listar, cadastrar, atualizar e excluir quartos.

**Ator Primário:** Administrador.

**Pré-condições:**  

- O administrador deve estar logado no sistema.
- Deve existir ao menos um tipo de quarto cadastrado para inserir quartos.

**Pós-condições:**  

- Quartos cadastrados, atualizados ou removidos conforme a ação executada.

## Fluxo Principal

1. O administrador acessa a opção "Quarto" no menu lateral.
2. O sistema exibe abas para as operações: Listar, Inserir, Atualizar, Excluir.
3. O administrador seleciona uma aba conforme a ação desejada.

### Listar Quartos

1. O sistema exibe uma tabela com os quartos cadastrados, mostrando ID, Tipo, Bloco e Número.
2. Se não houver quartos, exibe mensagem informativa.

### Inserir Quarto

1. O administrador seleciona o Tipo de Quarto.
2. O administrador preenche o Bloco e o Número do Quarto.
3. O administrador clica em "Inserir".
4. O sistema valida se o Bloco está preenchido.
5. O sistema verifica se já existe um quarto com o mesmo Número no mesmo Bloco.
6. O sistema insere o novo quarto no banco de dados.
7. O sistema exibe mensagem de sucesso e atualiza a lista.

### Atualizar Quarto

1. O administrador seleciona um quarto da lista.
2. O sistema preenche os campos com os dados atuais.
3. O administrador edita os campos desejados (Tipo de Quarto, Bloco, Número).
4. O administrador clica em "Salvar Alterações".
5. O sistema verifica se já existe outro quarto com o mesmo Número no mesmo Bloco.
6. O sistema atualiza os dados no banco de dados.
7. O sistema exibe mensagem de sucesso e atualiza a lista.

### Excluir Quarto

1. O administrador seleciona um quarto da lista.
2. O administrador clica em "Excluir".
3. O sistema remove o quarto do banco de dados.
4. O sistema exibe mensagem de sucesso e atualiza a lista.

## Fluxos De Exceção

- **FE1 – Dados inválidos:**  
  Se o administrador não informar o bloco, o sistema exibirá uma mensagem de erro.

- **FE2 – Dados repetidos:**  
  Se o administrador tentar inserir ou atualizar um quarto com número e bloco já existentes, o sistema exibirá uma mensagem de erro avisando que já existe um quarto com o mesmo número no bloco.
