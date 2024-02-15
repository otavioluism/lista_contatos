def delete_contact(contatos: list) -> None: 
  if contatos: 
    indice = int(input('Digite o indice do contato que queres remover: '))
    indice_ajustado = indice - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
      contato = contatos[indice_ajustado]
      contatos.remove(contato)
      print(f'O contato do {contato.get('nome')} foi removido com sucesso!')
    else: 
      print('Indice inválido, tente novamente!')
  return