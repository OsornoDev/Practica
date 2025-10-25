from app import saludo

def test_saludo():
    assert saludo("Eduardo") == "Hola Eduardo!"
    assert saludo() == "Hola Mundo!"
