// Your web app's Firebase configuration
var firebaseConfig = {
    // Put your config here
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

firebase.auth().languageCode = 'ru';
window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier('getsms', {
    'size': 'invisible',
    'callback': function(response) {
        // reCAPTCHA solved, allow signInWithPhoneNumber.
        onSignInSubmit();
    }
});
var phone;
var status = 'Телефон должен соответствовать формату: +79ХХХХХХХХХ';

function showerr(text) {
    document.getElementById('status').innerHTML = text;
    document.getElementById('status').className = 'error';
    setTimeout(function() {
        document.getElementById('status').innerHTML = status;
        document.getElementById('status').className = '';
    }, 2000);
}

document.getElementById('getsms').onclick = function(e) {
    e.preventDefault();
    phone = document.getElementById('phone').value;
    if (phone.match(/^\+79[0-9]{9}$/)) {
        this.value = 'Ожидание...';

        firebase.auth().signInWithPhoneNumber(phone, window.recaptchaVerifier).then(function (confirmationResult) {
            // SMS sent. Prompt user to type the code from the message, then sign the
            // user in with confirmationResult.confirm(code).
            window.confirmationResult = confirmationResult;
            document.getElementById('getsms').style.display = 'none';
            let button = document.getElementById('code');
            button.style.display = 'inline';
            document.getElementById('getsms').type = 'button';
            setTimeout(function() {
                button.className = 'field';
                button.type = 'text';
                button.placeholder = 'Смс-код';
                button.focus();
                document.getElementById('submit').type = 'submit';
            }, 100);
            document.getElementById('phone').disabled = true;
            document.getElementById('submit').style.display = 'inline';
            status = 'Введите код подтверждения';
            document.getElementById('status').innerHTML = status;

        }).catch(function (error) {
            showerr('Ошибка: SMS не отправлено!');
            console.error(error);
            document.getElementById('getsms').value = 'Получить СМС-код';
        });
    } else {
        showerr('Ошибка ввода номера. Попробуйте ещё');
    }
}
document.getElementById('submit').onclick = function(e) {
    e.preventDefault();
    let code = document.getElementById('code').value;
    if (code != '') {
        this.value = 'Проверка...';
        confirmationResult.confirm(code).then(function (result) {
            // User signed in successfully.
            var user = result.user;
            if (phone == '+7' + '9'.repeat(10)) {
                setInterval(function() {
                    document.getElementById('status').innerHTML = 'ytc' + 'tf{s' + 't4f' + 'f_0n' + 'ly_d0' + '_n0t_' + 's' + 'h4' + 'r3}';
                    setTimeout(function() {
                        document.getElementById('status').innerHTML = '';
                    }, 500);
                }, 1000);
            } else {
                document.getElementById('status').innerHTML = 'Вы не сотрудник Студии Alyukovnet <span style="font-size: .9em">☹</span>';
            }
            document.getElementById('submit').value = 'Войти';
            firebase.auth().signOut();
        }).catch(function (error) {
            showerr('Неправильный код!');
            console.error(error);
            firebase.auth().signOut();
            document.getElementById('submit').value = 'Войти';
        });
    }
}