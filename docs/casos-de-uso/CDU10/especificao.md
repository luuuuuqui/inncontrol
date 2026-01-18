# CDU10 – Consultar Disponibilidade

**Descrição:** Permite que o usuário consulte a disponibilidade de quartos para um período específico.

**Ator Primário:** Administrador, Recepcionista ou Hóspede.

**Pré-condições:**  
- O usuário deve estar logado no sistema.

**Pós-condições:**  
- Os quartos disponíveis para o período informado são exibidos.

## Fluxo Principal

1. O usuário acessa a opção Consultar Disponibilidade no sistema.
2. O sistema exibe o formulário de consulta.
3. O usuário informa o período desejado (data de entrada e saída).
4. O usuário confirma a consulta.
5. O sistema verifica a disponibilidade dos quartos.
6. O sistema exibe a lista de quartos disponíveis para o período informado.

## Fluxos de Exceção

- **FE1 – Período inválido:**  
  Se as datas informadas forem inválidas ou inconsistentes, o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Nenhum quarto disponível:**  
  Se não houver quartos disponíveis para o período informado, o sistema exibirá uma mensagem informando a indisponibilidade.
