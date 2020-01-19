let openings = [
    "https://openings.moe/video/JoJoNoKimyouNaBouken-OP01-NCBD.mp4",
    "https://openings.moe/video/JoJoNoKimyouNaBouken-OP02-NCBD.mp4",
    "https://openings.moe/video/JoJoNoKimyouNaBouken%EF%BC%9AStardustCrusaders-OP01-NCBD.mp4",
    "https://openings.moe/video/JoJoNoKimyouNaBouken%EF%BC%9AStardustCrusaders-BattleInEgypt-OP01a-NCBD.mp4",
    "https://openings.moe/video/JoJoNoKimyouNaBouken%EF%BC%9AStardustCrusaders-BattleInEgypt-ED01-NCBD.mp4",
    "https://openings.moe/video/JoJoNoKimyouNaBouken%EF%BC%9AStardustCrusaders-ED02-NCBD.mp4",
    "https://openings.moe/video/JoJoNoKimyouNaBouken-ED01a-NCBD.mp4",
]

let characters = {
    "Jotaro Kujo": "https://vignette.wikia.nocookie.net/jjba/images/0/01/JotaroProfile.png/revision/latest/scale-to-width-down/270?cb=20190117103858",
    "Giorno Giovanna": "https://vignette.wikia.nocookie.net/jjba/images/5/55/GiornoProfile.png/revision/latest/scale-to-width-down/341?cb=20190119135508",
    "Joseph Joestar": "https://vignette.wikia.nocookie.net/jjba/images/f/fc/Joseph_Infobox.jpg/revision/latest/scale-to-width-down/270?cb=20190628200225",
    "Jolyne Cujoh": "https://vignette.wikia.nocookie.net/jjba/images/e/eb/JolyneProfile.png/revision/latest/scale-to-width-down/273?cb=20190321182247",
    "Josuke Higashikata": "https://vignette.wikia.nocookie.net/jjba/images/c/c5/JosukeProfile.png/revision/latest?cb=20190117181938",
    "Josuke Higashikata": "https://vignette.wikia.nocookie.net/jjba/images/a/aa/Josuke_jojolion_crop.png/revision/latest/scale-to-width-down/700?cb=20190504143842",
    "Johnny Joestar": "https://vignette.wikia.nocookie.net/jjba/images/d/d9/Johnny_Joestar_Part_7.jpg/revision/latest/scale-to-width-down/350?cb=20181104035833",
    "Jonathan Joestar": "https://vignette.wikia.nocookie.net/jjba/images/4/45/JonathanInfobox.png/revision/latest/scale-to-width-down/333?cb=20190117181842"
}

function unmute(){
    console.log('unmuted');
    let vid = document.querySelector('video');
    if(vid.muted){
        document.querySelector('video').muted = false;
        document.querySelector('#click').remove();
    }
}

window.onload = function() {
    let videlem = document.createElement("video"),
        sourceMP4 = document.createElement("source"); 
    sourceMP4.type = "video/mp4";
    sourceMP4.src = openings[~~(Math.random()*openings.length)];
    videlem.autoplay = "autoplay";
    videlem.loop = "loop";
    videlem.muted = "true";
    videlem.appendChild(sourceMP4);
    document.querySelector('body').prepend(videlem);

    let keys = Object.keys(characters),
        cter = keys[~~(Math.random()*keys.length)];
        image = document.createElement("img");
    image.src = characters[cter];
    document.querySelector('#character').append(image);

    document.querySelector('#character h2').innerHTML = cter;
}