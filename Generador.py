from pyswip import Prolog
from datetime import datetime
import tempfile
import os

class GeneradorHorarios:
    def __init__(self):
        self.prolog = Prolog()
        self.inicializar_base_conocimiento()
    
    def inicializar_base_conocimiento(self):
        conocimiento = """
        % =======================
        % HECHOS
        % =======================

        clase(ai_fundamentos, juan, 2).
        clase(prolog_avanzado, maria, 1).
        clase(ml_basico, juan, 3).
        clase(vision_artificial, pedro, 2).

        franja(lunes_8_10).
        franja(lunes_10_12).
        franja(martes_8_10).
        franja(martes_10_12).
        franja(miercoles_8_10).

        aula(a101).
        aula(a102).

        no_disponible(juan, lunes_10_12).
        no_disponible(maria, martes_8_10).
        no_disponible(pedro, miercoles_8_10).

        % =======================
        % MOTOR PRINCIPAL
        % =======================

        horario_valido(Horario) :-
            findall(clase(Clase, Profesor, Duracion),
                    clase(Clase, Profesor, Duracion),
                    Clases),
            generar_asignaciones(Clases, [], Horario),
            verificar_restricciones_globales(Horario).

        % =======================
        % GENERADOR
        % =======================

        generar_asignaciones([], Horario, Horario).

        generar_asignaciones([clase(Clase, Profesor, _)|Resto], Parcial, Final) :-
            franja(Franja),
            \\+ no_disponible(Profesor, Franja),
            aula(Aula),
            Asig = asignacion(Clase, Franja, Aula),
            verificar_restricciones_locales(Asig, Parcial),
            generar_asignaciones(Resto, [Asig|Parcial], Final).

        % =======================
        % REGLAS LOCALES
        % =======================

        verificar_restricciones_locales(Asignacion, HorarioParcial) :-
            Asignacion = asignacion(ClaseN, FranjaN, AulaN),
            clase(ClaseN, ProfesorN, _),
            \\+ (
                member(asignacion(ClaseE, FranjaE, AulaE), HorarioParcial),
                clase(ClaseE, ProfesorE, _),
                (
                  (ProfesorN = ProfesorE, FranjaN = FranjaE)
                  ;
                  (AulaN = AulaE, FranjaN = FranjaE)
                )
            ).

        % =======================
        % REGLAS GLOBALES
        % =======================

        verificar_restricciones_globales(Horario) :-
            findall(Clase, clase(Clase, _, _), Todas),
            findall(Clase, member(asignacion(Clase, _, _), Horario), Asignadas),
            msort(Todas, TodasOrd),
            msort(Asignadas, AsigOrd),
            TodasOrd = AsigOrd.
        """

        with tempfile.NamedTemporaryFile(mode='w', suffix='.pl', delete=False) as f:
            f.write(conocimiento)
            ruta = f.name

        self.prolog.consult(ruta)
        os.unlink(ruta)

    def generar_horario(self):
        resultados = list(self.prolog.query("horario_valido(H)"))
        if resultados:
            return self.procesar(resultados[0]["H"])
        return None

    def procesar(self, horario_prolog):
        salida = []

        for a in horario_prolog:
            # a viene como texto desde Prolog → parsear
            texto = str(a)  # asignacion(ai_fundamentos,lunes_8_10,a101)
            limpio = texto.replace("asignacion(", "").replace(")", "")
            clase, franja, aula = limpio.split(",")

            info = list(self.prolog.query(f"clase({clase}, P, D)"))[0]

            salida.append({
                "clase": clase,
                "profesor": str(info["P"]),
                "duracion": info["D"],
                "franja": franja,
                "aula": aula,
                "dia": franja.split("_")[0],
                "hora_inicio": franja.split("_")[1],
                "hora_fin": franja.split("_")[2]
            })

        return salida

class GeneradorHorarios:
    def __init__(self):
        self.prolog = Prolog()
        self.inicializar_base_conocimiento()
    
    def inicializar_base_conocimiento(self):
        conocimiento = """
        % =======================
        % HECHOS
        % =======================

        clase(ai_fundamentos, juan, 2).
        clase(prolog_avanzado, maria, 1).
        clase(ml_basico, juan, 3).
        clase(vision_artificial, pedro, 2).

        franja(lunes_8_10).
        franja(lunes_10_12).
        franja(martes_8_10).
        franja(martes_10_12).
        franja(miercoles_8_10).

        aula(a101).
        aula(a102).

        no_disponible(juan, lunes_10_12).
        no_disponible(maria, martes_8_10).
        no_disponible(pedro, miercoles_8_10).

        % =======================
        % MOTOR PRINCIPAL
        % =======================

        horario_valido(Horario) :-
            findall(clase(Clase, Profesor, Duracion),
                    clase(Clase, Profesor, Duracion),
                    Clases),
            generar_asignaciones(Clases, [], Horario),
            verificar_restricciones_globales(Horario).

        % =======================
        % GENERADOR
        % =======================

        generar_asignaciones([], Horario, Horario).

        generar_asignaciones([clase(Clase, Profesor, _)|Resto], Parcial, Final) :-
            franja(Franja),
            \\+ no_disponible(Profesor, Franja),
            aula(Aula),
            Asig = asignacion(Clase, Franja, Aula),
            verificar_restricciones_locales(Asig, Parcial),
            generar_asignaciones(Resto, [Asig|Parcial], Final).

        % =======================
        % REGLAS LOCALES
        % =======================

        verificar_restricciones_locales(Asignacion, HorarioParcial) :-
            Asignacion = asignacion(ClaseN, FranjaN, AulaN),
            clase(ClaseN, ProfesorN, _),
            \\+ (
                member(asignacion(ClaseE, FranjaE, AulaE), HorarioParcial),
                clase(ClaseE, ProfesorE, _),
                (
                  (ProfesorN = ProfesorE, FranjaN = FranjaE)
                  ;
                  (AulaN = AulaE, FranjaN = FranjaE)
                )
            ).

        % =======================
        % REGLAS GLOBALES
        % =======================

        verificar_restricciones_globales(Horario) :-
            findall(Clase, clase(Clase, _, _), Todas),
            findall(Clase, member(asignacion(Clase, _, _), Horario), Asignadas),
            msort(Todas, TodasOrd),
            msort(Asignadas, AsigOrd),
            TodasOrd = AsigOrd.
        """

        with tempfile.NamedTemporaryFile(mode='w', suffix='.pl', delete=False) as f:
            f.write(conocimiento)
            ruta = f.name

        self.prolog.consult(ruta)
        os.unlink(ruta)

    def generar_horario(self):
        resultados = list(self.prolog.query("horario_valido(H)"))
        if resultados:
            return self.procesar(resultados[0]["H"])
        return None

    def procesar(self, horario_prolog):
        salida = []

        for a in horario_prolog:
            # a viene como texto desde Prolog → parsear
            texto = str(a)  # asignacion(ai_fundamentos,lunes_8_10,a101)
            limpio = texto.replace("asignacion(", "").replace(")", "")
            clase, franja, aula = limpio.split(",")

            info = list(self.prolog.query(f"clase({clase}, P, D)"))[0]

            salida.append({
                "clase": clase,
                "profesor": str(info["P"]),
                "duracion": info["D"],
                "franja": franja,
                "aula": aula,
                "dia": franja.split("_")[0],
                "hora_inicio": franja.split("_")[1],
                "hora_fin": franja.split("_")[2]
            })

        return salida
