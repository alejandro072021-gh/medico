class Clinica:
    def __init__(self):
        self._pacientes = []
        self._medicos = []
        self._citas = []
        self._historial = []

    # Verificar si un codigo ya existe
    def codigo_existe(self, codigo):
        return self.buscar_por_codigo(codigo) is not None

    # Agregar paciente
    def agregar_paciente(self, paciente):
        if not paciente.codigo or not paciente.nombre.strip():
            return False

        if not isinstance(paciente.edad, int) or isinstance(paciente.edad, bool) or paciente.edad <= 0:
            return False

        if self.codigo_existe(paciente.codigo):
            return False

        self._pacientes.append(paciente)
        return True

    # Agregar medico
    def agregar_medico(self, medico):
        if not medico.codigo or not medico.nombre.strip() or not medico.especialidad.strip():
            return False

        if self.codigo_existe(medico.codigo):
            return False

        self._medicos.append(medico)
        return True

    # Agregar cita
    def agregar_cita(self, cita):
        if not cita.codigo or not cita.fecha:
            return False

        if self.codigo_existe(cita.codigo):
            return False

        if cita.paciente not in self._pacientes:
            return False

        if cita.medico not in self._medicos:
            return False

        self._citas.append(cita)
        return True

    # RF03: Buscar por codigo
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

    # Programacion funcional: filtrar citas por paciente
    def filtrar_citas_por_paciente(self, codigo_paciente):
        return list(filter(
            lambda cita: cita.paciente.codigo == codigo_paciente,
            self._citas
        ))

    # RF05: Registrar atencion
    def registrar_atencion(self, atencion):
        if atencion.cita not in self._citas:
            return False

        if not atencion.codigo:
            return False

        if not atencion.diagnostico.strip() or not atencion.tratamiento.strip():
            return False

        if self.codigo_existe(atencion.codigo):
            return False

        if any(a.codigo == atencion.codigo for a in self._historial):
            return False

        self._historial.append(atencion)
        return True

    # Programacion funcional: filtrar atenciones por paciente
    def filtrar_atenciones_por_paciente(self, codigo_paciente):
        return list(filter(
            lambda atencion: atencion.cita.paciente.codigo == codigo_paciente,
            self._historial
        ))

    # Mostrar historial
    def mostrar_historial(self):
        for atencion in self._historial:
            print(atencion.resumen())
