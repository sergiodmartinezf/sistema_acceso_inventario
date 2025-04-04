from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

# Create your views here.

def Inicio_app(request):
    sql1 ="""
    SELECT * 
    FROM test_app_tabla1
    ORDER BY id ASC;
    """
    cursor = connection.cursor()
    cursor.execute(sql1)

    datos_tabla1=cursor.fetchall()

    sql2 = """
    SELECT COUNT(*) 
    FROM test_app_tabla1;
    """
    cursor = connection.cursor()
    cursor.execute(sql2)
    cantidad_tabla1 = cursor.fetchone()

    return render(request, 'HTML/inicio.html',{'datos_tabla1': datos_tabla1, 'cantidad_tabla1': cantidad_tabla1[0]})

def pagina_actualizar_datos(request):
    registro_id = int(request.GET.get('registro_id'))

    sql = """
    SELECT * 
    FROM test_app_tabla1 
    WHERE id=%s;
    """

    cursor = connection.cursor()
    cursor.execute(sql, [registro_id])
    datos_tabla1_actualizar = cursor.fetchone()

    print(datos_tabla1_actualizar)
    return render(request, 'HTML/actualizar.html',{'datos_tabla1_actualizar': datos_tabla1_actualizar})

def ingresar_datos(request):
    if request.method == 'POST':
        dato1 = request.POST.get('dato1')
        dato2 = request.POST.get('dato2')

        sql = """
        INSERT INTO test_app_tabla1 (dato1, dato2) 
        VALUES (%s, %s);
        """

        cursor = connection.cursor()
        cursor.execute(sql, [dato1, dato2])

        #connection.commit()

        return HttpResponse("ingresado exitosamente") 

    return HttpResponse("Método no permitido")

def borrar_datos(request):
    if request.method == 'POST':
        registro_id = int(request.POST.get('registro_id'))

        sql = 'DELETE FROM test_app_tabla1 WHERE id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [registro_id])

        #connection.commit()

        return HttpResponse("borrado exitosamente") 

    return HttpResponse("Método no permitido")

def actualizar_datos(request):
    if request.method == 'POST':
        registro_id = int(request.POST.get('registro_id'))
        dato1 = int(request.POST.get('dato1'))
        dato2 = request.POST.get('dato2')

        sql = """
        UPDATE test_app_tabla1
        SET dato1=%s, dato2=%s
        WHERE id=%s;
        """

        cursor = connection.cursor()
        cursor.execute(sql, [dato1, dato2, registro_id])

        #connection.commit()

        return HttpResponse("ingresado exitosamente") 

    return HttpResponse("Método no permitido")
