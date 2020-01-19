var firebaseConfig = {
    apiKey: "AIzaSyBJASVoTVXrzngJd2tFaKmY-KdqspZ8QRQ",
    authDomain: "anime-90901.firebaseapp.com",
    databaseURL: "https://anime-90901.firebaseio.com",
    projectId: "anime-90901",
    storageBucket: "anime-90901.appspot.com",
    messagingSenderId: "157197715810",
    appId: "1:157197715810:web:123e8d08b85e7f16"
};

firebase.initializeApp(firebaseConfig);

var db = firebase.firestore();
const size = 130;

var data = {};

function update(){
    let m1 = ~~(Math.random()*size);
    let m2 = ~~(Math.random()*size);
    while(m1 === m2)
        m2 = ~~(Math.random()*size);
    app.update(data[m1], data[m2], data[`cool${data[m1]}`], data[`cool${data[m2]}`], data[`views${data[m1]}`], data[`views${data[m2]}`]);
}


function updateCool(who){
    let obj = {};
    if (who == 'first'){
        obj[`cool${app.n1}`] = app.cool1 + 1;
        data[`cool${app.n1}`] += 1;
    }
    else {
        obj[`cool${app.n2}`] = app.cool1 + 1;
        data[`cool${app.n2}`] += 1;
    }
    data[`views${app.n1}`] += 1;
    data[`views${app.n2}`] += 1;
    obj[`views${app.n1}`] = data[`views${app.n1}`];
    obj[`views${app.n2}`] = data[`views${app.n2}`];
    obj[`cool${app.n1}`] = data[`cool${app.n1}`];
    obj[`cool${app.n2}`] = data[`cool${app.n2}`];
    db.collection("anime").doc("XZjHOzeBiPwhBLSu8LSy").update(obj);
    update();
}

//vue part
var app = new Vue({
    el: '#main',
    data: {
        link1: 'https://you-anime.ru/anime-images/characters/0.jpg',
        link2: 'https://you-anime.ru/anime-images/characters/0.jpg',
        n1: 1,
        n2: 2,
        cool1: 0,
        cool2: 0,
        first: false,
        second: false,
        loaded: false,
        message: 'Загружаем аниме'
    },
    methods: {
        update: function (n1, n2, c1, c2, v1, v2) {
            this.link1 = `https://you-anime.ru/anime-images/characters/${n1}.jpg`;
            this.link2 = `https://you-anime.ru/anime-images/characters/${n2}.jpg`;
            if (v1 == 0) v1 = 1;
            if (v2 == 0) v2 = 1;
            this.cool1 = Math.floor(100 * (c1 / v1));
            this.cool2 = Math.floor(100 * (c2 / v2));
            this.n1 = n1;
            this.n2 = n2;
        },
        winner1: function(){
            this.first = true;
            this.cool1 = Math.floor(100 * ((data[`cool${this.n1}`] + 1) / (data[`views${this.n1}`] + 1)));
            this.cool2 = Math.floor(100 * ((data[`cool${this.n2}`]) / (data[`views${this.n2}`] + 1)));
            setTimeout(() => {
                updateCool('first', this.n1, this.n2);
                this.first = false;
            }, 1000);
        },
        winner2: function(){
            this.second = true;
            this.cool1 = Math.floor(100 * ((data[`cool${this.n1}`]) / (data[`views${this.n1}`] + 1)));
            this.cool2 = Math.floor(100 * ((data[`cool${this.n2}`] + 1) / (data[`views${this.n2}`] + 1)));
            setTimeout(() => {
                updateCool('second', this.n1, this.n2);
                this.second = false;
            }, 1000);
        },
        getData: async function(name, size) {
            let ans;
            await axios.post('/getData', {
                collection: name,
                size: size
            }).then(response => {
                ans = response.data;
            })
            .catch(error => ans = error);
            return ans;
        }
    }
})


window.onload = async function(){
    data = await app.getData('anime', size);
    app.message = 'Обновляем показатели крутости';
    setTimeout(function(){
        app.loaded = true;
        update();
    }, 1500) 
}