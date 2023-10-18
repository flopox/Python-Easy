import secrets
import string

def crea_contraseñas(longitud):
    caracteres_especiales = []
    otros_caracteres = 'éâëøñìÛãØÁßÂðÎãàÏíÜÚàýÄÕÌÑÊÜðÀåÑîÚØýæûæÝòûõÉÇåÉÁöÔÉÖÚùÏìÃØèýÞúöÇ×ïñëáåéÅÌôÍêëðÄäøÕáÃóÜèÔï'
    otros_caracteres = list(set(otros_caracteres))
    todos_caracteres = caracteres_especiales + otros_caracteres

    cada_caracter_random = string.ascii_letters + string.digits + string.punctuation + ''.join(todos_caracteres)
    contraseña = "".join(secrets.choice(cada_caracter_random) for _ in range(longitud))
    return contraseña

nueva_contraseña = crea_contraseñas(10)
print("La contraseña fue creada exitosamente y es:", nueva_contraseña)
