
// title burger
document.addEventListener('DOMContentLoaded', function (){
    let Tburger = document.getElementById('Tburger')
    let TBmenu = document.getElementById('TBmenu')
    
    Tburger.addEventListener('click', function(){
        Tburger.classList.toggle('open')
        TBmenu.classList.toggle('open')
    })
});



// filtes menu hiden overflow
document.addEventListener("DOMContentLoaded", function () {
    const btns = document.querySelectorAll(".filter_menu p");


    btns.forEach(btn => {
        btn.addEventListener('click', function() {
            btn.parentNode.classList.toggle('open');
    })
    });
});


// автоматическое добавление p кнопки если если оверфлоу
var divElements = document.querySelectorAll('.filter_menu ul'); 
divElements.forEach(divElement => {
    if (divElement.scrollHeight > divElement.clientHeight) {
        var pElement = document.createElement('p');
        divElement.parentNode.appendChild(pElement);
    };
})
