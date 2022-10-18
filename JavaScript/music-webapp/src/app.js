const express = require('express');
const path = require('path');
const app = express();
const port = process.env.PORT || 5000;
const address = path.join(__dirname, "../public");
app.use(express.static(address));
  app.get("/*", (req ,res)=>{
    res.sendFile(path.join(__dirname,'../public/index.html'));
});
app.listen(port , () =>{

});