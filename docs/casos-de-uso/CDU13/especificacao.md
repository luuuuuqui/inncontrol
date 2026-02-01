# CDU13 – Realizar Check-in

**Descrição:** Permite confirmar a entrada do hóspede no hotel, alterando o status da reserva para indicar que a estadia está em curso.

**Ator Primário:** Administrador e Recepcionista.

**Pré-condições:** 
- O usuário deve estar logado no sistema.
- Deve existir uma reserva cadastrada para o hóspede.

**Pós-condições:** 
- O status da reserva é atualizado para refletir o início da estadia.

## Fluxo Principal

1. O usuário acessa a opção "Reserva" no menu lateral.
2. O sistema exibe o painel de gerenciamento e o usuário seleciona a aba "Atualizar".
3. O usuário seleciona a reserva correspondente ao hóspede na lista de seleção.
4. O usuário altera o status da reserva para "Em andamento" (ou status equivalente).
5. O usuário confirma a operação clicando no botão "Salvar Alterações".
6. O sistema valida os dados e a persistência da informação.
7. O sistema exibe uma mensagem de sucesso confirmando a operação.

## Fluxos de Exceção

- **FE1 – Reserva não encontrada:** Se a reserva selecionada não puder ser carregada para atualização, o sistema exibirá uma mensagem de erro informando que o registro não foi encontrado.

- **FE2 – Erro na validação de datas:** Se as datas da reserva forem inconsistentes ou houver conflito de disponibilidade ao tentar salvar, o sistema impedirá a atualização e exibirá uma mensagem explicativa.