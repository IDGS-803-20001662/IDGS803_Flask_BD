from db import get_connection

'''
try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consultar_alumno()')
        resulset = cursor.fetchall()

        for row in resulset:
            print(row)
    
    connection.close()

except Exception as ex:
    print(ex)
'''
'''
try:
    connection = get_connection()
    with connection.cursor() as cursor:
    # la coma se usa para que lo tome como tupla
        cursor.execute('call consultar_alumno_id(%s)',(3,))
        resulset = cursor.fetchall()
        print(resulset)
    
    connection.close()

except Exception as ex:
    print(ex)
'''

try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call agregar_alumno(%s,%s,%s)',("Citlalli", "Martínez Medina", "citla@gmail.com"))
    connection.commit()
    connection.close()

except Exception as ex:
    print(ex)