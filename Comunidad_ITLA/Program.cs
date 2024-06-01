using System;

public class Miembrodelacomunidad{

    public string Nombre { get; set; }
    public int Edad { get; set;}

    public Miembrodelacomunidad(string nombre, int edad){

        Nombre = nombre;
        Edad = edad;
    }

    public virtual void Mostrarinformacion(){
        Console.WriteLine($"Nombre: {Nombre}, Edad: {Edad}");
    }
}


public class Empleado : Miembrodelacomunidad{

    public Empleado(string nombre, int edad) : base(nombre, edad) {}
}

public class Estudiante : Miembrodelacomunidad{

    public Estudiante(string nombre, int edad) : base(nombre, edad) {}
}

public class Exalumno : Miembrodelacomunidad{

    public Exalumno(string nombre, int edad) : base(nombre, edad) {}
}

public class Docente : Empleado{

    public Docente(string nombre, int edad) : base(nombre, edad) {}
}

public class Administrativo : Empleado{

    public Administrativo(string nombre, int edad) : base(nombre, edad) {}
}

public class Maestro : Docente{

    public Maestro(string nombre, int edad) : base(nombre, edad) {}
}

public class Administrador : Docente{

    public Administrador(string nombre, int edad) : base(nombre, edad) {}
}

class Program{

    static void Main(string[] args){

        List<Miembrodelacomunidad> miembros = new List<Miembrodelacomunidad>{

            new Empleado("Carlos", 35),
            new Estudiante("Jose", 30),
            new Exalumno("Manuel;", 23),
            new Docente("Michael", 25),
            new Administrativo("Edison", 20),
            new Maestro(" Maria", 26),
            new Administrador("Alisson", 28),

            };
            foreach (var miembro in miembros){
                miembro.Mostrarinformacion();
            }
    }
}