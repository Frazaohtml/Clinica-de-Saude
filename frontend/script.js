const profissionais = require('./profissionais.json');  

function buscarDisponibilidade(especialidade) {
  const resultado = profissionais.filter(prof => prof.especialidade === especialidade);
  return resultado;
}

console.log(buscarDisponibilidade("Cardiologia"));  
