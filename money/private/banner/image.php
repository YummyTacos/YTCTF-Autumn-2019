<?
    $files = ["gigi.jpg", "rich.gif", "soda.gif", "uspel.gif", "makemoney.gif"];
    $file = $files[rand(0, 4)];
    if (isset($_GET['login']) && isset($_GET['password'])) {
        if ($_GET['login'] != '' && $_GET['password'] != '') {
            header('Flag: ytctf{th4nks_f0r_your_login_and_password}');
        }
    }
    if (file_exists($file))
    {
        header("Content-type: image/png");
        readfile($file);
    }
?>
