# CDU06 – Manter Reserva

**Descrição:** Permite que o administrador gerencie as reservas no sistema, incluindo listar, inserir, atualizar e excluir reservas.

**Ator Primário:** Administrador.

**Pré-condições:**

- O usuário deve estar logado como administrador no sistema.
- Devem existir hóspedes e quartos cadastrados para criar reservas.

**Pós-condições:**

- As reservas estarão atualizadas no banco de dados conforme as operações realizadas.

## Fluxo Principal

### Listar Reservas

1. O administrador acessa a aba "Listar" na interface de gestão de reservas.
2. O sistema exibe uma tabela com todas as reservas cadastradas, incluindo ID, Hóspede, Quarto (Bloco e Número), Tipo de Quarto, Check-In, Check-Out, Diárias, Total (calculado com base no valor da diária do tipo de quarto) e Status (com ícones: ❔ Pendente, ✔️ Confirmado, ❌ Cancelado, ☑️ Finalizado).
3. Se não houver reservas, o sistema exibe uma mensagem informativa: "Nenhuma reserva encontrada."

### Inserir Reserva

1. O administrador acessa a aba "Inserir" na interface de gestão de reservas.
2. O sistema verifica se existem hóspedes e quartos cadastrados; caso contrário, exibe erro: "É necessário ter hóspedes e quartos cadastrados para criar uma reserva."
3. O administrador seleciona um hóspede no seletor (formato: ID - Nome).
4. O administrador seleciona um quarto no seletor (formato: Bloco - Nº Número - Tipo).
5. O administrador seleciona o período de estadia (Check-In e Check-Out) no date input, com mínimo a partir da data atual.
6. O administrador seleciona o status inicial: "Pendente" ou "Confirmado".
7. O administrador clica no botão "Inserir Reserva" (habilitado apenas se todos os campos estiverem preenchidos).
8. O sistema valida a disponibilidade do quarto no período e insere a reserva.
9. O sistema exibe uma mensagem de sucesso e recarrega a interface.

### Atualizar Reserva

1. O administrador acessa a aba "Atualizar" na interface de gestão de reservas.
2. O sistema exibe um seletor com as reservas existentes (formato: ID - Nome Hóspede - Bloco NºNúmero - Data Check-In - Diárias - Status).
3. O administrador seleciona uma reserva.
4. O sistema preenche os campos editáveis: Hóspede, Quarto, Período (Check-In/Check-Out), Status.
5. O administrador edita os campos desejados.
6. O administrador clica no botão "Salvar Alterações".
7. O sistema valida a disponibilidade do quarto no novo período (ignorando a própria reserva) e atualiza a reserva.
8. O sistema exibe uma mensagem de sucesso e recarrega a interface.

### Excluir Reserva

1. O administrador acessa a aba "Excluir" na interface de gestão de reservas.
2. O sistema exibe um seletor com as reservas existentes (formato: ID - Nome Hóspede - Bloco NºNúmero - Data Check-In - Diárias - Status).
3. O administrador seleciona uma reserva.
4. O administrador clica no botão "Excluir Reserva".
5. O sistema remove a reserva do banco de dados.
6. O sistema exibe uma mensagem de sucesso e recarrega a interface.

## Fluxos de Exceção

- **FE1 – Hóspedes ou quartos insuficientes (Inserir/Atualizar):**  
  Se não houver hóspedes ou quartos cadastrados, o sistema exibe erro: "É necessário ter hóspedes e quartos cadastrados para criar uma reserva."

- **FE2 – Campos obrigatórios não preenchidos (Inserir):**  
  Se hospede, quarto ou datas não forem selecionados, o botão "Inserir Reserva" fica desabilitado.

- **FE3 – Quarto indisponível (Inserir/Atualizar):**  
  Se o quarto já estiver reservado no período selecionado, o sistema lança ValueError: "Quarto indisponível! Já existe reserva de [data_inicial] a [data_final]."

- **FE4 – Datas inválidas:**  
  - Se data de check-in ou check-out for antes de 2026: "Data de Check-In/Check-Out não pode ser antes de 2026."  
  - Se check-in >= check-out: "A data de check-in não pode ser posterior à data de check-out." ou "A data de check-out não pode ser antes da data de check-in."  
  - Se formato inválido: "Data de Check-In/Check-Out inválida. [erro]"

- **FE5 – Status vazio:**  
  Se status for vazio, ValueError: "Status da reserva não pode ser vazio."

- **FE6 – Erro geral:**  
  Em caso de erro inesperado, o sistema exibe: "Erro ao [operação]: [mensagem do erro]".
