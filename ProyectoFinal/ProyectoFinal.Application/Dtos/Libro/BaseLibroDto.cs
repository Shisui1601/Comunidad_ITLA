using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProyectoLibrary.Application.Dtos.Libro
{
    public class BaseLibroDto
    {
        public string Titulo { get; set; }
        public string Autor { get; set; }
        public decimal Precio { get; set; }
        public int CantidadEnInventario { get; set; }
        public int CategoriaId { get; set; }
    }
}
