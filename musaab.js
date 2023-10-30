const express = require('express');
const app = express();
app.get('/', function(req, res) {
res.send('Welcome');
});
app.get('/hii', function(req, res) {
res.send('Thankyou');
});
app.listen(3000);
console.log("Server running on port 3000");