class Clinica:
    def __init__(self):
        self._pacientes = []
        self._medicos = []
        self._citas = []
        self._historial = []

    #Agregar
    def agregar_paciente(self, paciente):
        self._pacientes.append(paciente)

    def agregar_medico(self, medico):
        self._medicos.append(medico)

    def agregar_cita(self, cita):
        self._citas.append(cita)

    #RF03: Buscar por codigo
    def buscar_por_codigo(self, codigo):
        for paciente in self._pacientes:
            if paciente.codigo == codigo:
                return paciente
        for medico in self._medicos:
            if medico.codigo == codigo:
                return medico
        for cita in self._citas:
            if cita.codigo == codigo:
                return cita
        return None

    #RF05: Registrar atencion
    def registrar_atencion(self, atencion):
        if atencion.cita not in self._citas:
            return False
        if atencion.diagnostico == "" or atencion.tratamiento == "":
            return False
        self._historial.append(atencion)
        return True

    def mostrar_historial(self):
        for atencion in self._historial:
            print(atencion.resumen())