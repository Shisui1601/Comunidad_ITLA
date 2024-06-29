using ProyectoLibrary.Domain.Base;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProyectoFinal.Domain.Entities
{
    public class Categoria: BaseEntity
    {
        public string Nombre { get; set; }
        public List<Libro> Libros { get; set; }
    }
}
