import sys
from pathlib import Path

# Asegurar que el directorio raíz del proyecto esté en el sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from dominio.alumno import Alumno
from servicio.alumnos_matriculados import AlumnosMatriculados


def menu() -> None:
    """
    Función principal que implementa el flujo y menú del sistema de matrículas.
    Responsabilidades:
    Contiene un menú con 4 opciones:
    1) Matricular alumno
    2) Listar alumnos
    3) Eliminar archivo de alumnos
    4) Salir
    """
    opcion = None

    while opcion != "4":
        print("\n" + "=" * 40)
        print("    SISTEMA DE MATRÍCULAS DE ALUMNOS    ")
        print("=" * 40)
        print("1) Matricular alumno")
        print("2) Listar alumnos")
        print("3) Eliminar archivo de alumnos")
        print("4) Salir")
        print("=" * 40)

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre del alumno a matricular: ").strip()
            if nombre:
                alumno = Alumno(nombre)
                AlumnosMatriculados.matricular_alumno(alumno)
            else:
                print("El nombre del alumno no puede estar vacío.")

        elif opcion == "2":
            AlumnosMatriculados.listar_alumnos()

        elif opcion == "3":
            confirmacion = input(
                "¿Está seguro de que desea eliminar el archivo de alumnos? (s/n): "
            ).strip().lower()
            if confirmacion in ("s", "si", "sí", "y", "yes"):
                AlumnosMatriculados.eliminar_alumnos()
            else:
                print("Operación cancelada.")

        elif opcion == "4":
            print("\nSaliendo del programa. ¡Hasta pronto!")

        else:
            print("Opción inválida. Por favor, seleccione un número entre 1 y 4.")


if __name__ == "__main__":
    try:
        menu()
    except (KeyboardInterrupt, EOFError):
        print("\n\nPrograma interrumpido por el usuario. Saliendo...")
