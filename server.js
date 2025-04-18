const express = require('express');
const fs = require('fs');
const app = express();
const PORT = 3000;

// Middleware para permitir requisições de qualquer origem (CORS)
app.use(express.json());
app.use(express.static('public'));

// Rota para buscar profissionais por especialidade
app.get('/profissionais', (req, res) => {
  const especialidade = req.query.especialidade;

  fs.readFile('./profissionais.json', 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ erro: 'Erro ao ler o arquivo' });
    }

    const profissionais = JSON.parse(data);
    const resultado = profissionais.filter(prof => 
      prof.especialidade === especialidade && prof.disponivel
    );

    res.json(resultado);
  });
});

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
