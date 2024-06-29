using ProyectoLibrary.Domain.Base;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProyectoFinal.Domain.Entities
{
    public class Cliente: BaseEntity
    {
        public string Nombre { get; set; }
        public string Direccion { get; set; }
        public string Email { get; set; }
    }
}
