using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProyectoFinal.Domain.Entities
{
    internal class Categoria
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public List<Libro> Libros { get; set; }
    }
}
