import os
from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import Atencion
from clinica import Clinica
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
def main():
    clinica = Clinica()
    # Doctores
    clinica.agregar_medico(Medico("M001", "Hugo Paredes", "Odontologia"))
    clinica.agregar_medico(Medico("M002", "Rosa Villanueva", "Dermatologia"))
    clinica.agregar_medico(Medico("M003", "Mateo Quispe", "Cardiologia"))
    clinica.agregar_medico(Medico("M004", "Valeria Cardenas", "Pediatria"))
    clinica.agregar_medico(Medico("M005", "Renzo Salazar", "Traumatologia"))
    clinica.agregar_medico(Medico("M006", "Camila Bustamante", "Ginecologia"))
    clinica.agregar_medico(Medico("M007", "Andres Cabrera", "Oftalmologia"))
    clinica.agregar_medico(Medico("M008", "Fabiola Rojas", "Neurologia"))
    clinica.agregar_medico(Medico("M009", "Sergio Palomino", "Psicologia"))
    clinica.agregar_medico(Medico("M010", "Elena Guerrero", "Medicina General"))
    motivos = ["Control general", "Dolor o molestia", "Fiebre o gripe", "Revision de examenes"]
    while True:
        limpiar_pantalla()
        try:
            print("==============================")
            print("      SISTEMA DE CLINICA      ")
            print("==============================")
            print(" 1. Registrar paciente")
            print(" 2. Generar cita")
            print(" 3. Atender cita")
            print(" 4. Cancelar cita")
            print(" 5. Historial de paciente")
            print(" 6. Ver doctores")
            print(" 7. Ver citas")
            print(" 8. Registrar doctor")
            print(" 0. Salir")
            print("==============================")
            opcion = input("Elige una opcion: ")
            print("==============================")
            if opcion == "1":
                codigo = input("Codigo del paciente: ")
                if clinica.codigo_existe(codigo):
                    raise ValueError("Ese codigo ya existe.")
                nombre = input("Nombre: ")
                edad_texto = input("Edad: ")
                if not edad_texto.isdigit():
                    raise ValueError("La edad debe ser un numero.")
                paciente = Paciente(codigo, nombre, int(edad_texto))
                if clinica.agregar_paciente(paciente):
                    print(f"Paciente registrado: {paciente.resumen()}")
                else:
                    raise ValueError("Datos de paciente no validos.")
            elif opcion == "2":
                codigo_paciente = input("Codigo del paciente: ")
                paciente = clinica.buscar_por_codigo(codigo_paciente)
                if not isinstance(paciente, Paciente):
                    raise ValueError("Paciente no encontrado.")
                print("--- Doctores ---")
                clinica.mostrar_medicos()
                especialidad = input("Especialidad (ej: Odontologia): ")
                medico = clinica.buscar_medico_por_especialidad(especialidad)
                if medico is None:
                    raise ValueError("No hay doctor con esa especialidad.")
                codigo = input("Codigo de la cita: ")
                if clinica.codigo_existe(codigo):
                    raise ValueError("Ese codigo ya existe.")
                fecha = input("Fecha (dd/mm/aaaa): ")
                cita = Cita(codigo, paciente, medico, fecha)
                if clinica.agregar_cita(cita):
                    print(f"Cita generada: {cita.resumen()}")
                else:
                    raise ValueError("No se pudo generar la cita.")
            elif opcion == "3":
                codigo_cita = input("Codigo de la cita: ")
                cita = clinica.buscar_por_codigo(codigo_cita)
                if not isinstance(cita, Cita):
                    raise ValueError("Cita no encontrada.")
                if cita.estado != "Pendiente":
                    raise ValueError(f"La cita ya esta {cita.estado}.")
                print("--- Motivos ---")
                for i in range(len(motivos)):
                    print(f"{i + 1}. {motivos[i]}")
                numero = input("Elige el motivo: ")
                if not numero.isdigit() or int(numero) < 1 or int(numero) > len(motivos):
                    raise ValueError("Motivo no valido.")
                motivo = motivos[int(numero) - 1]
                codigo = input("Codigo de la atencion: ")
                if clinica.codigo_existe(codigo):
                    raise ValueError("Ese codigo ya existe.")
                diagnostico = input("Diagnostico: ")
                tratamiento = input("Tratamiento: ")
                atencion = Atencion(codigo, cita, f"{motivo} - {diagnostico}", tratamiento)
                if clinica.registrar_atencion(atencion):
                    cita.estado = "Atendida"
                    print(f"Atencion registrada: {atencion.resumen()}")
                else:
                    raise ValueError("No se pudo registrar la atencion.")
            elif opcion == "4":
                codigo_cita = input("Codigo de la cita: ")
                cita = clinica.buscar_por_codigo(codigo_cita)
                if not isinstance(cita, Cita):
                    raise ValueError("Cita no encontrada.")
                if cita.estado != "Pendiente":
                    raise ValueError(f"La cita ya esta {cita.estado}.")
                cita.estado = "Cancelada"
                print(f"Cita cancelada: {cita.resumen()}")
            elif opcion == "5":
                codigo_paciente = input("Codigo del paciente: ")
                paciente = clinica.buscar_por_codigo(codigo_paciente)
                if not isinstance(paciente, Paciente):
                    raise ValueError("Paciente no encontrado.")
                atenciones = clinica.filtrar_atenciones_por_paciente(codigo_paciente)
                print(f"--- Historial de {paciente.nombre} ---")
                if len(atenciones) == 0:
                    print("Sin atenciones.")
                for atencion in atenciones:
                    print(atencion.resumen())
            elif opcion == "6":
                print("--- Doctores ---")
                clinica.mostrar_medicos()
            elif opcion == "7":
                print("--- Citas ---")
                clinica.mostrar_citas()
            elif opcion == "8":
                # Calcular el numero del siguiente doctor
                numero = 1
                while clinica.codigo_existe(f"M{numero:03d}"):
                    numero += 1
                codigo_esperado = f"M{numero:03d}"
                print("--- Registrar doctor ---")
                print(f"Este sera el doctor numero {numero}.")
                print(f"Ejemplo de codigo: {codigo_esperado}")
                print("Formato: la letra M en mayuscula + 3 numeros.")
                codigo = input("Codigo del doctor: ")
                while codigo != codigo_esperado:
                    print(f"Codigo incorrecto. Debes escribir {codigo_esperado}.")
                    codigo = input("Codigo del doctor: ")
                nombre = input("Nombre del doctor: ")
                while not nombre.strip():
                    print("El nombre no puede estar vacio.")
                    nombre = input("Nombre del doctor: ")
                especialidad = input("Especialidad del doctor: ")
                while not especialidad.strip():
                    print("La especialidad no puede estar vacia.")
                    especialidad = input("Especialidad del doctor: ")
                medico = Medico(codigo, nombre, especialidad)
                if clinica.agregar_medico(medico):
                    print(f"Doctor registrado: {medico.resumen()}")
                else:
                    raise ValueError("Datos de doctor no validos.")
            elif opcion == "0":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida")
        except ValueError as error:
            print(f"Error: {error}")
        input("Presiona Enter para continuar...")
main()
