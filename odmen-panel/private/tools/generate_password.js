const bcrypt = require('bcrypt');
const saltRounds = 5;
const password = 'ytctf{*}'; // please make passwords 12 or less characters
bcrypt.hash(password, saltRounds, function(err, hash) {
    if (err) throw err;
    process.stdout.write(hash);
});