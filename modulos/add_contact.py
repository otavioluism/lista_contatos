def add_contact(contatos: list) -> None: 
  nome_contato = input('Digite o nome do contato que deseja adicionar: ')
  telefone = input('Digite o número: ')
  email = input('Digite o email: ')
  contato = {'nome': nome_contato, 'email': email, 'telefone': telefone, 'favorito': False}
  contatos.append(contato)
  print(f'O contato {nome_contato} foi adicionado com sucesso!')
  return 
