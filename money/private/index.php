<?php
    $success = false;
    $valid = false;
    $set = isset($_POST['email']);

    $senderName = 'Alyukovsky&Co';
    $senderMail = 'alyukovnet@yummytacos.me';

    if ($set) {
        $email = $_REQUEST['email'];

        $valid = filter_var($email, FILTER_VALIDATE_EMAIL);

        if ($valid) {
            $to = $_REQUEST['email'];
            $subject = '=?utf-8?b?' . base64_encode('Спонсирование Ваших Проектов') . '?=';

            $message = file_get_contents('mail.html');

            $headers = 'MIME-Version: 1.0' . "\r\n";
            $headers .= 'Content-type: text/html; charset=UTF-8' . "\r\n";
            $headers .= 'From: ' . '=?utf-8?b?' . base64_encode($senderName) . '?=' . ' <'.$senderMail.'>' . "\r\n";

            $success = mail($to, $subject, $message, $headers);
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Спонсирование Ваших Проектов</title>
</head>
<body>
    <style>
        @import url('https://fonts.googleapis.com/css?family=Roboto');
        html {
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
        }
        body {
            width: 100%;
            min-height: 100%;
            margin: 0;
            padding: 0;
            font-family: 'Roboto', sans-serif;
            font-size: 18px;
            color: black;
            display: flex;
            align-items: center;
            background: url("scroo.jpg") center center;
            -webkit-background-size: 400px;
            background-size: 400px;
        }
        h1 {
            font-size: 2em;
            font-weight: bold;
            margin: 15px;
            text-align: center;
        }
        p {
            margin: 15px;
        }
        article {
            width: 90%;
            max-width: 700px;
            margin: 0 auto;
            background: #fff;
        }
        form {
            margin: 15px;
            text-align: center;
        }
        form input {
            height: 35px;
            border: 1px solid #000;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            color: #000;
            background: #fff;
            -webkit-border-radius: 0;
            -moz-border-radius: 0;
            border-radius: 0;
            margin: 0;
            padding: 0 5px;
        }
        form input[type=email] {
            width: 80%;
            max-width: 300px;
        }
        form input[type=submit]:hover {
            background: #aaa;
            cursor: pointer;
        }
        .copyright {
            text-align: center;
            font-size: 0.8em;
            color: #333333;
        }
        .success {
            font-size: 0.9em;
            color: #00bb00;
        }
        .error {
            font-size: 0.9em;
            color: #bb0000;
        }
    </style>
    <article>
        <h1>Спонсирование Ваших Проектов</h1>
        <p>Установив рекламный баннер на Вашем сайте, вне зависимости от его посещаемости, вы получаете прибыль от просмотров и УДВОЕННУЮ прибыль за клики. Даже самый мелкий сайт должен нести доход!</p>
        <p>Оставьте свой email в форме ниже и мы в автоматическом режиме отправим Вам свежие условия сервиса и код встраимового элемента:</p>
        <form method="POST" action="/">
            <input type="email" name="email" required placeholder="pochta@pochta.pochta">
            <input type="submit" value="Получить">
            <?php
                if ($set) {
                    if ($success) {
                        echo '<p class="success">Сообщение отправлено на '.$email.'. Проверяйте почтовый ящик!</p>';
                    } else if (!$valid) {
                        echo '<p class="error">Либо ты хитрый взломщик, либо твой браузер не умеет отсеивать недействительные email :-(</p>';
                    } else {
                        echo '<p class="error">Ошибка при отправке сообщения на '.$email.'. Попробуйте снова!</p>';
                    }
                }
            ?>
        </form>
        <p class="copyright">© Alyukovsky&Co, 2018</p>
    </article>
</body>
</html>