import Titulos
import Ingreso_Datos
import Operaciones_Basicas
import Operaciones_Avanzadas

def main():
    Titulos.mostrar_titulo("Operaciones Básicas")
    a = Ingreso_Datos.Metodo_LeerA()
    b = Ingreso_Datos.Metodo_LeerB()
    
    print(f"Suma: {Operaciones_Basicas.suma(a, b)}")
    print(f"Resta: {Operaciones_Basicas.resta(a, b)}")
    print(f"Multiplicación: {Operaciones_Basicas.multiplicacion(a, b)}")
    print(f"División: {Operaciones_Basicas.division(a, b)}")
    
    Titulos.mostrar_titulo("Operaciones Avanzadas")
    x = Ingreso_Datos.Metodo_Leer_a()
    
    print(f"Cuadrado: {Operaciones_Avanzadas.cuadrado(x)}")
    print(f"Cubo: {Operaciones_Avanzadas.cubo(x)}")

if __name__ == "__main__":
    main()
