from pathlib import Path
from dominio.alumno import Alumno


class AlumnosMatriculados:

    ruta_archivo: str = "alumnos.txt"

    @classmethod
    def matricular_alumno(cls, alumno: Alumno) -> None:

        try:
            archivo = Path(cls.ruta_archivo)
            with archivo.open("a", encoding="utf-8") as f:
                f.write(f"{alumno.nombre}\n")
            print(f"-> Alumno '{alumno.nombre}' matriculado correctamente.")
        except Exception as e:
            print(f"Error al matricular el alumno: {e}")

    @classmethod
    def listar_alumnos(cls) -> None:
        try:
            archivo = Path(cls.ruta_archivo)
            if not archivo.exists():
                print(f"El archivo '{cls.ruta_archivo}' no existe o no tiene alumnos registrados.")
                return

            lineas = [
                linea.strip()
                for linea in archivo.read_text(encoding="utf-8").splitlines()
                if linea.strip()
            ]

            if not lineas:
                print("No hay alumnos registrados en el archivo actualmente.")
                return

            print("ALUMNOS MATRICULADOS:")
            for indice, nombre in enumerate(lineas, start=1):
                alumno = Alumno(nombre)
                print(f"{indice}. {alumno}")
        except Exception as e:
            print(f"Error al listar los alumnos: {e}")

    @classmethod
    def eliminar_alumnos(cls) -> None:
        try:
            archivo = Path(cls.ruta_archivo)
            if archivo.exists():
                archivo.unlink()
                print(f"-> Archivo '{cls.ruta_archivo}' eliminado correctamente.")
            else:
                print(f"El archivo '{cls.ruta_archivo}' no existe, no hay nada que eliminar.")
        except Exception as e:
            print(f"Error al eliminar el archivo: {e}")
