def mark_contact_favorite(contatos: list, indice: int) -> None:
  indice_ajustado = indice - 1
  if indice_ajustado >= 0 and indice_ajustado < len(contatos):
    status = not contatos[indice_ajustado].get('favorito')
    flag_favorito = 'favorito' if status else 'desfavorito'
    contatos[indice_ajustado].update({'favorito': status})
    print(f'Contado marcado como {flag_favorito}')
  else: 
    print('Indice inválido, tente novamente!')