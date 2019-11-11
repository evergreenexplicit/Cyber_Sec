const https = require('https')
const fs = require('fs')


const options = {
  key: fs.readFileSync('xprivkeyA.pem'),
  cert: fs.readFileSync('xcertA.crt')
}
console.log("Starting...");
https.createServer(options, (req, res) => {
  res.write("hello world");
  res.end();
}).listen(3000);
