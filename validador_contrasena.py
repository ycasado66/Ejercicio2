def validar_contrasena(contrasena):
    """
    Valida que la contraseña cumpla con los siguientes requisitos:
    - Mínimo 8 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    """
    if len(contrasena) < 8:
        return False
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_minuscula = any(c.islower() for c in contrasena)
    tiene_numero = any(c.isdigit() for c in contrasena)
    return tiene_mayuscula and tiene_minuscula and tiene_numero

# Ejemplo de uso
if __name__ == "__main__":
    contrasena = input("Introduce una contraseña: ")
    if validar_contrasena(contrasena):
        print("Contraseña válida.")
    else:
        print("Contraseña inválida. Debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.")
