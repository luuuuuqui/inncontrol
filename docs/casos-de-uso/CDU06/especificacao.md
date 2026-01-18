# CDU06 – Excluir Quarto

**Descrição:** Permite que o administrador exclua um quarto do sistema, desde que não existam reservas ativas vinculadas a ele.

**Ator Primário:** Administrador.

**Pré-condições:**  
- O administrador deve estar logado no sistema.
- O quarto deve estar cadastrado no sistema.

**Pós-condições:**  
- O quarto é removido do sistema.

## Fluxo Principal

1. O administrador acessa a opção Excluir Quarto no sistema.
2. O sistema exibe a lista de quartos cadastrados.
3. O administrador seleciona o quarto que deseja excluir.
4. O sistema verifica se existem reservas ativas vinculadas ao quarto.
5. O sistema solicita a confirmação da exclusão.
6. O administrador confirma a exclusão.
7. O sistema remove o quarto do sistema e exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Quarto com reserva ativa:**  
  Se o quarto possuir reservas ativas, o sistema impedirá a exclusão e exibirá uma mensagem informando o motivo.

- **FE2 – Exclusão cancelada:**  
  Se o administrador cancelar a confirmação, o sistema não realizará a exclusão e retornará à lista de quartos.
