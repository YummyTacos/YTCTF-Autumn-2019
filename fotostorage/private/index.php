<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>FOTOSTORAGE&trade;</title>
    <style>
        html, body {
            margin: 0;
            padding: 0;
        }

        h1, h2, p {
            margin: 0;
        }

        div, #file {
            display: block;
        }

        .center {
            display: flex;
            place-content: center;
            align-items: center;
            flex-direction: column;
        }

        .big {
            font-size: x-large;
        }

        .space-after {
            margin-bottom: 12px;
        }

        .red {
            color: red;
        }

        .green {
            color: green;
        }

        .muted {
            color: gray;
        }
    </style>
</head>
<body>

<h1 class="center space-after">FOTOSTORAGE&trade;</h1>
<p class="big center space-after">БЕСПЛАТНЫЙ сервис для отправки и безопасного хранения ваших фото</p>

<div class="center space-after">
    <h2>Наши преимущества:</h2>
    <div>
        <ul>
            <li>
                Отправьте нам ваше фото, получите ссылку и делитесь ей с друзьями!
            </li>
            <li>
                Мы используем криптографически безопасный генератор ссылок, поэтому ваши фото могут быть получены только
                по ссылке!
            </li>
            <li>
                Мы не заморачивались с дизайном, потому что все силы и деньги ушли на защиту ваших фото!
            </li>
            <li>
                We also speaking good English why what we can have foreign klients! Site at English coming soon!
            </li>
        </ul>
    </div>
</div>

<div class="center">
    <h2 class="space-after">Попробуйте!</h2>

    <form method="post" enctype="multipart/form-data">
        <label for="file">Выберите изображение (не более 1 Мб):</label>
        <input type="hidden" name="MAX_FILE_SIZE" value="1048576"/>
        <input class="space-after" id="file" type="file" name="fileToUpload" accept="image/*" required/>
        <div class="space-after">
            <p class="muted">Статус:</p>
            <?php
            function generateRandomString($length = 10)
            {
                $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_';
                $charactersLength = strlen($characters);
                $randomString = '';
                for ($i = 0; $i < $length; $i++) {
                    $randomString .= $characters[rand(0, $charactersLength - 1)];
                }
                return $randomString;
            }

            if (is_uploaded_file($_FILES['fileToUpload']['tmp_name'])) {
                if ($_FILES['fileToUpload']['size'] > 1048576) {
                    echo "<p class='red'>Файл слишком большой!</p>";
                    return;
                }
                $target_path = generateRandomString() . '/';
                if (!mkdir(getcwd() . '/' . $target_path, 0775, true)) {
                    echo "<p class='red'>Ошибка при обработке файла!</p>";
                    return;
                }
                $target_path .= generateRandomString();
                $target_path .= '.' . pathinfo($_FILES['fileToUpload']['name'], PATHINFO_EXTENSION);
                if (move_uploaded_file($_FILES['fileToUpload']['tmp_name'], $target_path)) {
                    echo "<p class='green'>Файл отправлен успешно! Ваш файл: <a href='$target_path'>" . basename($target_path) . "</a></p>";
                } else {
                    echo "<p class='red'>Файл не был принят</p>";
                }
            } else {
                echo "<p class='red'>Файл не был отправлен</p>";
            }
            ?>
        </div>
        <button type="submit">Загрузить!</button>
    </form>
</div>

</body>
</html>
