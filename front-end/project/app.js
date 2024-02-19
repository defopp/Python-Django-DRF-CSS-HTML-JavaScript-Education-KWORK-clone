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






// amount menu toggle list
// ПОФИКСИТЬ
document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".menu_button");


    buttons.forEach(button => {
        button.addEventListener('click', event => {
            const parentDIV = button.parentNode
            parentDIV.classList.toggle('open');
            document.addEventListener('click', event => {
                parent = event.target.closest('div') 
    
                // Check if clicked element has a parent div with class 'active'
                if (!parent || !parent.classList.contains('open')) {
                    // Remove class from all parent divs
                    buttons.forEach(button => {
                        button.parentNode.classList.remove('open')});
                    // Remove event listener from the document
                    document.removeEventListener('click', clickOutsideDiv);
                };
            });
            event.stopPropagation();
        });
    });
});




// слайдер 1 //сделать слайдер
let offset = 0;
const sliderLine = document.querySelector('.slider_items')

document.querySelector(".next_sl_bt").addEventListener('click', function () {
    offset += 290;
    if (offset > 580) {
        offset = 0
    }
    sliderLine.style.left = -offset + 'px';
})

document.querySelector(".prev_sl_bt").addEventListener('click', function () {
    offset -= 290;
    if (offset < 0) {
        offset = 580
    }
    sliderLine.style.left = -offset + 'px';
})