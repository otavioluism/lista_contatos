def edit_contact(contatos: list, indice: int) -> None:
  indice_ajustado = indice - 1
  if indice_ajustado >= 0 and indice_ajustado < len(contatos):
    print('Caso não quiser editar alguma informação, só click enter')
    nome_editado = input('Digite o novo nome: ')
    telefone_editado = input('Digite o novo telefone: ')
    email_editado = input('Digite o novo email: ')
    if nome_editado:
      contatos[indice_ajustado].update({'nome': nome_editado})
      mensagem = ['Nome editado.']
    if telefone_editado:
      contatos[indice_ajustado].update({'telefone': telefone_editado})
      mensagem.append('Telefone editado.')
    if email_editado: 
      contatos[indice_ajustado].update({'email': email_editado})
      mensagem.append('Email editado.')
    print(' '.join(mensagem)) 
  else: 
    print('Indice inválido, tente novamente!')