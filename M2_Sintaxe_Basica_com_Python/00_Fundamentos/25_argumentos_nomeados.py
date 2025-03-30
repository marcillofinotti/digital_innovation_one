def salvar_carros(marca, modelo, ano, placa):
    # salva carro no banco de dados ...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carros("Chevrolet", "Cruze", 2019, "ABC-1234")
salvar_carros(marca="Chevrolet", modelo="Cruze", ano=2019, placa="ABC-1234")
salvar_carros(**{"marca": "Chevrolet", "modelo": "Cruze", "ano": 2019, "placa": "ABC-1234"})