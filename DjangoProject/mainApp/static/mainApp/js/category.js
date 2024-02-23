document.addEventListener('DOMContentLoaded', function (){
    let Tburger = document.getElementById('Tburger')
    let TBmenu = document.getElementById('TBmenu')
    
    Tburger.addEventListener('click', function(){
        Tburger.classList.toggle('open')
        TBmenu.classList.toggle('open')
    })
});