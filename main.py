from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import Atencion
from clinica import Clinica

clinica = Clinica()

paciente_01 = Paciente("P001","Juan",22)
medico_01 = Medico("M001","Oscar Torres","Cardiologia")
cita_01 = Cita("C001",paciente_01,medico_01, "04/11/2026")

clinica.agregar_paciente(paciente_01)
clinica.agregar_medico(medico_01)
clinica.agregar_cita(cita_01)

print(paciente_01.resumen())
print(medico_01.resumen())
print(cita_01.resumen())

#RF03: Buscar por codigo
encontrado = clinica.buscar_por_codigo("P001")
if encontrado is not None:
    print(f"Encontrado: {encontrado.resumen()}")
else:
    print("No se encontró el código P001")

no_encontrado = clinica.buscar_por_codigo("P999")
if no_encontrado is not None:
    print(f"Encontrado: {no_encontrado.resumen()}")
else:
    print("No se encontró el código P999")

#RF05: Registrar atencion
atencion_01 = Atencion("A001", cita_01, "Hipertension leve", "Dieta baja en sal")
if clinica.registrar_atencion(atencion_01):
    print(f"Atención registrada: {atencion_01.resumen()}")
else:
    print("No se pudo registrar la atención")

print("--- Historial ---")
clinica.mostrar_historial()