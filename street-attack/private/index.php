<?
    $ans = '';
    if (isset($_GET['lat']) && isset($_GET['lng']) && isset($_GET['token'])) {
        $token = $_GET['token'];

        $ans = 'Bad token';
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_HTTPHEADER, array("authorization: $token"));
        curl_setopt($ch, CURLOPT_URL, "https://api.ctf.yummytacos.me/currentTeam");
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $data = curl_exec($ch);
        $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        if ($http_code == 200) {
            $team = json_decode($data)->name;
            $ans = 'Bad coordinates';
            $lat = $_GET['lat'];
            $lng = $_GET['lng'];
            if (is_numeric($lat) && is_numeric($lng)) {
                $lat = (float) $lat;
                $lng = (float) $lng;
                $ans = 'Wrong coordinates';
                if ($lat >= 59.8489 && $lat <= 59.8495 && $lng >= 30.328 && $lng <= 30.3293) {
                    $ans = 'ytctf{Saint-Petersburg_aka_g0r0d-n4-n3v3}';
                }
                $file = 'useFIFaB8cQRBdbu.log';
                $f = fopen($file,'a');
                fwrite($f, "$team $lat $lng\n");
                fclose($f);
            }
        }
    }
?>
<!DOCTYPE html>
<html>
<head>
    <title>Checker</title>
    <meta charset="utf8">
</head>
<body>
    <h1>Checker</h1>
    <form method="GET" action="">
        <p>Latitude: <input type="number" name="lat" step=0.0001></p>
        <p>Longitude: <input type="number" name="lng" step=0.0001></p>
        <p>Authorization token: <input type="text" name="token"></p>
        <p><input type="submit" value="Submit"></p>
    </form>
    <p>Answer: <? echo $ans ?></p>
    <p><b>Don't brute coordinates! We are logging your requests.</b></p>
</body>
</html>