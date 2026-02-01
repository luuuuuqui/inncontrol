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
4. O administrador preenche os campos necessários (como Bloco e Número) ou seleciona o quarto na lista.
5. O administrador clica no botão correspondente à ação (Inserir, Salvar Alterações ou Excluir).
6. O sistema valida os dados fornecidos.
7. O sistema executa a operação solicitada.
8. O sistema exibe uma mensagem de sucesso e atualiza a lista de quartos.

## Fluxos de Exceção

- **FE1 – Dados inválidos:** Se o administrador não informar o bloco ou deixar campos obrigatórios vazios, o sistema exibirá uma mensagem de erro solicitando a informação.

- **FE2 – Dados repetidos:** Se o administrador tentar inserir ou atualizar um quarto com número e bloco que já existem no sistema, o sistema exibirá uma mensagem de erro informando o conflito.