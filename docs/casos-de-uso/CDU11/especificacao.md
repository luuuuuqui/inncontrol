# CDU11 – Cancelar Reserva

**Descrição:** Permite que o usuário realize o cancelamento de uma reserva existente, alterando seu status e liberando a disponibilidade do quarto para o período.

**Ator Primário:** Administrador e Recepcionista.

**Pré-condições:** 
- O usuário deve estar logado no sistema.
- Deve existir uma reserva cadastrada no sistema.

**Pós-condições:** 
- O status da reserva é alterado para "Cancelada" e o quarto torna-se disponível para novas reservas no período correspondente.

## Fluxo Principal

1. O usuário acessa a opção "Reserva" no menu lateral.
2. O sistema exibe o painel de reservas e o usuário seleciona a aba "Atualizar".
3. O usuário seleciona a reserva que deseja cancelar na lista de seleção.
4. O usuário altera o campo de status da reserva para "Cancelada".
5. O usuário confirma a operação clicando no botão "Salvar Alterações".
6. O sistema valida a alteração e processa a atualização do status.
7. O sistema exibe uma mensagem de sucesso confirmando o cancelamento.

## Fluxos de Exceção

- **FE1 – Reserva não encontrada:** Se a reserva selecionada não puder ser recuperada para atualização, o sistema exibirá uma mensagem de erro informando que a reserva não foi encontrada.

- **FE2 – Erro no processamento:** Caso ocorra uma falha técnica durante a gravação da alteração, o sistema exibirá uma mensagem detalhando o erro ocorrido.