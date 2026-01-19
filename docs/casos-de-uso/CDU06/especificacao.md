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
2. O sistema exibe uma tabela com todas as reservas cadastradas, incluindo ID, Hóspede, Quarto (Bloco e Número), Tipo de Quarto, Check-In, Check-Out, Diárias, Total (calculado com base no valor da diária do tipo de quarto) e Status (Pendente, Confirmado, Cancelado, Finalizado).
3. Se não houver reservas, o sistema exibe uma mensagem informativa: "Nenhuma reserva encontrada."

### Operações de Gerenciamento

Para inserir, atualizar ou excluir reservas:

1. O administrador faz as alterações necessárias nos campos ou seleciona a reserva.
2. O administrador clica no botão correspondente à ação (Inserir Reserva, Salvar Alterações ou Excluir Reserva).
3. O sistema valida os dados fornecidos e a disponibilidade do quarto.
4. Se válido, o sistema executa a operação no banco de dados e exibe uma mensagem de sucesso.
5. O sistema recarrega a interface.

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
