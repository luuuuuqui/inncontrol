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

### Operações de Gerenciamento

Para inserir, atualizar ou excluir tipos de quarto:

1. O administrador faz as alterações necessárias nos campos ou seleciona o tipo de quarto.
2. O administrador clica no botão correspondente à ação (Inserir, Salvar Alterações ou Excluir).
3. O sistema valida os dados fornecidos.
4. Se válido, o sistema executa a operação no banco de dados e exibe uma mensagem de sucesso.
5. O sistema recarrega a interface.

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
