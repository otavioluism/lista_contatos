def list_favorites_contacts(contatos: list) -> None:
  contatos_favorito = [contato for contato in contatos if contato.get('favorito')]
  if contatos_favorito: 
    print('Indice'.rjust(2) + 'Favorito'.rjust(15) + 'Nome'.rjust(18) + 'Telefone'.rjust(31) + 'Email'.rjust(30))
    for indice, contato in enumerate(contatos_favorito, start=1): 
      if contato.get('favorito'):
        favorito = 'X' if contato.get('favorito') else ' '
        nome_contato = contato.get('nome')
        telefone = contato.get('telefone')
        email = contato.get('email')
        print(f'{str(indice).rjust(1)}.' f'{'['.rjust(12)}'f'{favorito}]' + f'{str(nome_contato).rjust(30)}' + f'{str(telefone).rjust(26)}' + f'{str(email).rjust(47)}')
  else:
    print('Não possui contatos favorito!')
  return