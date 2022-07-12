from calendar import c
from unittest import result
import mysql.connector


con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="RRHH"
)

cursor = con.cursor()

class FxSql():

    def validarClave(id_trabajador, clave):
        sql = "SELECT id_trabajador,clave,rol FROM trabajadores WHERE id_trabajador = %s"
        val = (id_trabajador,)
        cursor.execute(sql, val)
        resultado = cursor.fetchall()
        if resultado == []:
            return False
        else:
            clave_bd = resultado[0]
            rol = clave_bd[2]
            clave_bd = clave_bd[1]
            if clave_bd == clave:
                return rol
            else:
                return False

    def consultarPerfil(id_trabajador):
        sql = "SELECT trabajadores.id_trabajador, personas.rut, CONCAT(personas.primer_nombre,' ',personas.segundo_nombre,' ',personas.primer_apellido,' ',personas.segundo_apellido), personas.fecha_nacimiento, personas.sexo, trabajadores.telefono, trabajadores.direccion, trabajadores.fecha_ingreso, trabajadores.id_laborales, trabajadores.id_cargo FROM personas JOIN trabajadores ON trabajadores.rut = personas.rut where id_trabajador = %s"
        val = (id_trabajador,)
        cursor.execute(sql, val)
        resultado = cursor.fetchall()
        return resultado

    def listarCargas(id_trabajador):
        sql = "SELECT personas.rut,CONCAT(personas.primer_nombre,' ',personas.segundo_nombre,' ',personas.primer_apellido,' ',personas.segundo_apellido), personas.fecha_nacimiento, personas.sexo, cargas.relacion FROM personas JOIN cargas ON personas.rut = cargas.rut WHERE cargas.id_trabajador = %s"
        val = (id_trabajador,)
        cursor.execute(sql, val)
        resultado = cursor.fetchall()
        return resultado

    def listarContactos(id_trabajador):
        sql = "SELECT * FROM contactos WHERE id_trabajador = %s"
        val = (id_trabajador,)
        cursor.execute(sql, val)
        resultado = cursor.fetchall()
        return resultado

    def eliminarCarga(rut, id_trabajador):
        sql = "SELECT rut FROM cargas WHERE RUT = %s AND id_trabajador = %s"
        val = (rut, id_trabajador,)
        cursor.execute(sql, val)
        resultado = cursor.fetchall()
        if resultado == []:
            print("No existe dentro de los registros")
            return False
        else:
            sql = "DELETE FROM cargas WHERE rut = %s"
            val = (rut,)
            cursor.execute(sql, val)
            con.commit()
            sql = "DELETE FROM personas WHERE rut = %s"
            cursor.execute(sql, val)
            con.commit()
            print("Se ha eliminado la carga laboral", rut)

    def eliminarContactoNombre(nombre, id_trabajador):
        sql = "DELETE FROM contactos where nombre LIKE %s AND id_trabajador = %s"
        val = (nombre, id_trabajador,)
        cursor.execute(sql, val)
        con.commit()
        print("Se ha eliminado el contacto de emergencia")

    def listarCargos():
        sql = "SELECT * FROM cargos"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return resultado

    def listarDepartamenos():
        sql = "SELECT * FROM laborales"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return resultado

    def agregarCargo(id_cargo, nombre_cargo):
        sql = "INSERT INTO cargos (id_cargo,nombre_cargo) VALUES (%s,%s)"
        val = (id_cargo, nombre_cargo,)
        cursor.execute(sql, val)
        con.commit()

    def agregarDepartamento(id_laborales, area, departamento):
        sql = "INSERT INTO laborales (id_laborales,area,departamento) VALUES (%s,%s,%s)"
        val = (id_laborales, area, departamento,)
        cursor.execute(sql, val)
        con.commit()

    def borrarCargo(id_cargo):
        sql = "DELETE FROM cargos WHERE id_cargo = %s"
        val = (id_cargo,)
        cursor.execute(sql, val)
        con.commit()

    def borrarDepartamento(id_departamento):
        sql = "DELETE FROM laborales WHERE id_laborales = %s"
        val = (id_departamento,)
        cursor.execute(sql, val)
        con.commit()
        
    def agregarPersona(rut, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, sexo):
        sql = "INSERT INTO personas (rut,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,sexo) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (rut, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, sexo,)
        cursor.execute(sql, val)
        con.commit()

    def agregarTrabajador(rut, id_trabajador, estado, telefono, direccion, rol, clave, fecha_ingreso, id_laborales, id_cargo):
        sql = "INSERT INTO trabajadores (rut,id_trabajador,estado,telefono,direccion,rol,clave,fecha_ingreso,fecha_inactividad,id_laborales,id_cargo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,NULL,%s,%s)"
        val = (rut, id_trabajador, estado, telefono, direccion, rol, clave, fecha_ingreso, id_laborales, id_cargo,)
        cursor.execute(sql, val)
        con.commit()

    def agregarCargas(rut, id_trabajador, relacion):
        sql = "INSERT INTO cargas (rut,id_trabajador,relacion) VALUES (%s,%s,%s)"
        val = (rut, id_trabajador, relacion,)
        cursor.execute(sql, val)
        con.commit()

    def agregarContactos(nombre, relacion, numero1, numero2, id_trabajador):
        sql = "INSERT INTO contactos (nombre,relacion,numero1,numero2,id_trabajador) VALUES (%s,%s,%s,%s,%s)"
        val = (nombre, relacion, numero1, numero2, id_trabajador,)
        cursor.execute(sql, val)
        con.commit()

    def listarTrabajadores():
        sql = "SELECT trabajadores.id_trabajador, personas.rut, CONCAT(personas.primer_nombre,' ',personas.segundo_nombre,' ',personas.primer_apellido,' ',personas.segundo_apellido), personas.fecha_nacimiento, personas.sexo, trabajadores.telefono, trabajadores.direccion, trabajadores.fecha_ingreso, trabajadores.id_laborales, trabajadores.id_cargo, trabajadores.estado FROM personas JOIN trabajadores ON trabajadores.rut = personas.rut"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return resultado

    def modificarCargo(id_trabajador,cargo):
        sql = "UPDATE trabajadores SET id_cargo = %s WHERE id_trabajador = %s"
        val = (cargo,id_trabajador,)
        cursor.execute(sql, val)
        con.commit()

    def modificarDepartamento(id_trabajador,departamento):
        sql = "UPDATE trabajadores SET id_laborales = %s WHERE id_trabajador = %s"
        val = (departamento,id_trabajador,)
        cursor.execute(sql, val)
        con.commit()

    def actualizarDireccion(direccion,id_trabajador):
        sql = "UPDATE trabajadores SET direccion = %s WHERE id_trabajador = %s"
        val = (direccion,id_trabajador,)
        cursor.execute(sql, val)
        con.commit() 
    
    def actualizarTelefono(telefono, id_trabajador):
        sql = "UPDATE trabajadores SET telefono = %s WHERE id_trabajador = %s"
        val = (telefono,id_trabajador,)
        cursor.execute(sql, val)
        con.commit() 

    def actualizarNombre(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,id_trabajador):
        sql = "SELECT rut FROM trabajadores WHERE id_trabajador = %s"
        val = (id_trabajador,)
        cursor.execute(sql, val)
        resultado = cursor.fetchall()
        rut = resultado[0]
        rut = rut[0]
        sql = "UPDATE personas SET primer_nombre = %s , segundo_nombre = %s, primer_apellido = %s, segundo_apellido = %s WHERE rut = %s"
        val = (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,rut,)
        cursor.execute(sql, val)
        con.commit() 
    
    def existeRutEnTrbajadores(rut):
        sql = "SELECT rut FROM trabajadores where rut = %s"
        val = (rut,)
        cursor.execute(sql,val)
        resultado = cursor.fetchall()
        if resultado == []:
            return False
        else:
            return True

    def existeRutEnCargas(rut):
        sql = "SELECT rut FROM cargas where rut = %s"
        val = (rut,)
        cursor.execute(sql,val)
        resultado = cursor.fetchall()
        if resultado == []:
            return False
        else:
            return True



    


