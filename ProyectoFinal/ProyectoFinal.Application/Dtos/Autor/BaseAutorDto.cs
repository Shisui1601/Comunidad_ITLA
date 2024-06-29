using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProyectoLibrary.Application.Dtos.Autor
{
    public class BaseCategoriaDto
    {
        public string Nombre { get; set; }
        public List<Libro> Libros { get; set; }
    }
}
