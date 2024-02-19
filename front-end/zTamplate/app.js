document.addEventListener('DOMContentLoaded', function (){
    let burger = document.getElementById('burger')
    let menu2 = document.getElementById('burger_menu1')
    let menu3 = document.getElementById('burger_menu2')
    let menu1 = document.getElementById('burgerH')
    
    burger.addEventListener('click', function(){
        burger.classList.toggle('open')
        menu1.classList.toggle('open')
        menu2.classList.toggle('open')
        menu3.classList.toggle('open')
    })
});


// document.addEventListener("DOMContentLoaded", function () {
//     // const buttons = document.querySelectorAll(".footer_b_title");
//     const buttons = document.querySelectorAll(".footer_b_title");


//     buttons.forEach(button => {
//         button.addEventListener('click', function() {
//             button.classList.toggle('open');
//     })
// });
// });
// нужно сделать чтобы ивент лист работал только на тайтл, а открывал весь див


document.addEventListener("DOMContentLoaded", function () {
    // const buttons = document.querySelectorAll(".footer_b_title");
    const titles = document.querySelectorAll(".footer_b_title h4");


    titles.forEach(title => {
        title.addEventListener('click', function() {
            title.parentNode.classList.toggle('open');
    })
});
});
// Сделал