# CDU05 – Manter Tipo de Quarto

**Descrição:** Permite que o administrador gerencie os tipos de quarto no sistema, incluindo listar, inserir, atualizar e excluir tipos de quarto.

**Ator Primário:** Administrador.

**Pré-condições:**

- O usuário deve estar logado como administrador no sistema.

**Pós-condições:**

- Os tipos de quarto estarão atualizados no banco de dados conforme as operações realizadas.

## Fluxo Principal

### Listar Tipos de Quarto

1. O administrador acessa a aba "Listar" na interface de gerenciamento de tipos de quarto.
2. O sistema exibe uma tabela com todos os tipos de quarto cadastrados, incluindo ID, Nome, Descrição, Capacidade e Valor da Diária.
3. Se não houver tipos cadastrados, o sistema exibe uma mensagem informativa: "Nenhum tipo de quarto cadastrado."

### Inserir Tipo de Quarto

1. O administrador acessa a aba "Inserir" na interface de gerenciamento de tipos de quarto.
2. O administrador preenche os campos: Nome, Descrição, Capacidade (número inteiro positivo) e Valor da Diária (valor decimal positivo).
3. O administrador clica no botão "Inserir".
4. O sistema valida os dados e insere o novo tipo de quarto no banco de dados.
5. O sistema exibe uma mensagem de sucesso e recarrega a interface.

### Atualizar Tipo de Quarto

1. O administrador acessa a aba "Atualizar" na interface de gerenciamento de tipos de quarto.
2. O sistema exibe um seletor com os tipos de quarto existentes (formato: ID - Nome).
3. O administrador seleciona um tipo de quarto.
4. O sistema preenche os campos editáveis com os valores atuais: Nome, Descrição, Capacidade e Valor da Diária.
5. O administrador edita os campos desejados.
6. O administrador clica no botão "Salvar Alterações".
7. O sistema valida os dados e atualiza o tipo de quarto no banco de dados.
8. O sistema exibe uma mensagem de sucesso e recarrega a interface.

### Excluir Tipo de Quarto

1. O administrador acessa a aba "Excluir" na interface de gerenciamento de tipos de quarto.
2. O sistema exibe um seletor com os tipos de quarto existentes (formato: ID - Nome).
3. O administrador seleciona um tipo de quarto.
4. O administrador clica no botão "Excluir".
5. O sistema remove o tipo de quarto do banco de dados.
6. O sistema exibe uma mensagem de sucesso e recarrega a interface.

## Fluxos de Exceção

- **FE1 – Campos obrigatórios não preenchidos (Inserir/Atualizar):**  
  Se algum campo obrigatório (Nome, Descrição, Capacidade, Valor da Diária) não for preenchido, o sistema exibe uma mensagem de erro: "Preencha todos os campos."

- **FE2 – Nome duplicado (Inserir/Atualizar):**  
  Se o nome do tipo de quarto já existir (ignorando maiúsculas/minúsculas), o sistema exibe uma mensagem de erro: "O tipo de quarto '[nome]' já existe." ou "Já existe outro tipo de quarto com o nome '[nome]'."

- **FE3 – Capacidade inválida:**  
  Se a capacidade não for um inteiro positivo, o sistema lança ValueError: "Capacidade do tipo de quarto deve ser um inteiro positivo."

- **FE4 – Valor da diária inválido:**  
  Se o valor da diária não for um decimal positivo, o sistema lança ValueError: "Valor do adicional não pode ser negativo." (Nota: a validação menciona "adicional", mas aplica-se aqui).

- **FE5 – Erro geral:**  
  Em caso de erro inesperado durante inserção, atualização ou exclusão, o sistema exibe: "Erro ao [operação]: [mensagem do erro]".
