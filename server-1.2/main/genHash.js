const bcrypt = require('bcrypt');
const password = 'maple_yt2024';

bcrypt.hash(password, 10, (err, hash) => {
    if (err) {
        console.error(err);
    } else {
        console.log(hash);
    }
});