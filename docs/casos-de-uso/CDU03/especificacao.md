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

### Operações de Gerenciamento

Para inserir, atualizar ou excluir quartos:

1. O administrador faz as alterações necessárias nos campos ou seleciona o quarto.
2. O administrador clica no botão correspondente à ação (Inserir, Salvar Alterações ou Excluir).
3. O sistema valida os dados fornecidos.
4. Se válido, o sistema executa a operação no banco de dados e exibe uma mensagem de sucesso.
5. O sistema atualiza a lista de quartos.

## Fluxos De Exceção

- **FE1 – Dados inválidos:**  
  Se o administrador não informar o bloco, o sistema exibirá uma mensagem de erro.

- **FE2 – Dados repetidos:**  
  Se o administrador tentar inserir ou atualizar um quarto com número e bloco já existentes, o sistema exibirá uma mensagem de erro avisando que já existe um quarto com o mesmo número no bloco.
