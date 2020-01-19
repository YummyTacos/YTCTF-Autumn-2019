var express = require('express');
var router = express.Router();
var admin = require("firebase-admin");
var serviceAccount = require("../private/serviceKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://anime-90901.firebaseio.com"
});

let db = admin.firestore();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index');
});

router.post('/getData', async function(req, res, next){
  let col = req.body.collection;
  let size = req.body.size;

  try {

    let temp = {}, data = {};
    await db.collection(col).get().then(snap => {
      snap.forEach(function(doc) {
        data = doc.data();
      })
    });

    for (let i = 0; i < size; i++){
      temp[i] = data[i];
      temp[`cool${temp[i]}`] = data[`cool${temp[i]}`];
      temp[`views${temp[i]}`] = data[`views${temp[i]}`]; 
    }
    res.send(temp);

  } catch(err) {
    res.status(400);
    res.send('Houston, we\'ve had a problem')
  }
})

module.exports = router;
