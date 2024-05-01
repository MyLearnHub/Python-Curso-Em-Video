'use strict'

const switcher = document.querySelector('.btn');

switcher.addEventListener('click', function () {
    document.body.classList.toggle('dark-theme')

    var className = document.body.className;
    if (className == "light-theme") {
        console.log('Classe Atual:' + className);
        this.textContent = "Dark";
    } else {
        console.log('Classe Atual:' + className);
        this.textContent = "Light";
    }
})