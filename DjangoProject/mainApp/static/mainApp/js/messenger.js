document.addEventListener('DOMContentLoaded', function (){
    let burger = document.getElementById('burger_chat')
    let menu = document.querySelector('.menu_container')
    let menu_back = document.querySelector('.background_mcss')

    burger.addEventListener('click', function(){
        burger.classList.toggle('open')
        menu.classList.toggle('open')
        menu_back.classList.toggle('open')
    })
    
    menu_back.addEventListener('click', function(){
        burger.classList.toggle('open')
        menu_back.classList.toggle('open')
        menu.classList.toggle('open')
    })
})