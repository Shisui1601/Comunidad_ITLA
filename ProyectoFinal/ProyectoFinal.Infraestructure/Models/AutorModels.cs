﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProyectoLibrary.Infraestructure.Models
{
    public class AutorModels
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public List<Libro> Libros { get; set; }
    }
}
