from modulos.add_contact import add_contact
from modulos.list_contact import list_contact
from modulos.edit_contact import edit_contact
from modulos.delete_contact import delete_contact
from modulos.mark_contact import mark_contact_favorite
from modulos.list_favorite_contact import list_favorites_contacts


contatos = []

while True: 
  print('\nMenu agenda')
  print('1. Adicionar um contato')
  print('2. Listar todos contatos')
  print('3. Editar contato')
  print('4. Marcar/Desmarcar contato favorito')
  print('5. Listar todos os contatos favorito')
  print('6. Deletar contato')
  print('7. Sair')

  data_input = input('Digite uma opcao do menu: ')

  match data_input:
    case '1': 
      add_contact(contatos)
    case '2': 
      list_contact(contatos)
    case '3': 
      list_contact(contatos)
      indice = int(input('Digite o indice do contato que queres atualizar: '))
      edit_contact(contatos, indice)
    case '4': 
      list_contact(contatos)
      indice = int(input('Digite o indice do contato que queres marcar ou desmarcar favorito: '))
      mark_contact_favorite(contatos, indice)
    case '5': 
      list_favorites_contacts(contatos)
    case '6': 
      list_contact(contatos)
      delete_contact(contatos)
    case '7': 
      break
    case _:
      print('Opção inválida, digite novamente por favor!')

