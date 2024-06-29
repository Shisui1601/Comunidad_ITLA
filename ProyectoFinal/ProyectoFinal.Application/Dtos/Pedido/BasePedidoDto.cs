using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProyectoLibrary.Application.Dtos.Pedido
{
    public class BasePedidoDto
    {
        public DateTime Fecha { get; set; }
        public int ClienteId { get; set; }
    }
}
