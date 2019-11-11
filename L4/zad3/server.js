const https = require('https')
const fs = require('fs')
const path = require('path')
const express = require('express')


const options = {
  key: fs.readFileSync('3privkeyA.pem'),
  cert: fs.readFileSync('3certA.crt')
}

const app = express()
app.use(express.urlencoded({extended:true}))

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'))
})

app.post("/hack", (req, res) => {

  res.send(`  Padłeś ofiarą hakowańska, ID: ${req.body.username}, Hasło: ${req.body.password}`);
})

https.createServer(options, app).listen(443, () => console.log('app is listening (https)'))
app.listen(80, () => console.log('app is listening (http)'))

