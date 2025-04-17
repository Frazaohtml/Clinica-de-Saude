
const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname)));
app.use(express.json());

const PORT = 5000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on port ${PORT}`);
});
