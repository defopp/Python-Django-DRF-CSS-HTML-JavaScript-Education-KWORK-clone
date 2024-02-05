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
    const titles = document.querySelectorAll(".footer_b_title h4");


    titles.forEach(title => {
        title.addEventListener('click', function() {
            title.parentNode.classList.toggle('open');
    })
});
});
// Сделал







// слайдер 1
let offset = 0;
const sliderLine = document.querySelector('.thirdblock_stickers')

document.querySelector(".next_sl_bt").addEventListener('click', function () {
    offset += 576;
    if (offset > 1152) {
        offset = 0
    }
    sliderLine.style.left = -offset + 'px';
})

document.querySelector(".prev_sl_bt").addEventListener('click', function () {
    offset -= 576;
    if (offset < 0) {
        offset = 1152
    }
    sliderLine.style.left = -offset + 'px';
})


// слайдер 2
let offset1 = 0;
const sliderLine1 = document.querySelector('.thirdblock_stickers1')

document.querySelector(".next_sl_bt1").addEventListener('click', function () {
    offset1 += 576;
    if (offset1 > 1152) {
        offset1 = 0
    }
    sliderLine1.style.left = -offset1 + 'px';
})

document.querySelector(".prev_sl_bt1").addEventListener('click', function () {
    offset1 -= 576;
    if (offset1 < 0) {
        offset1 = 1152
    }
    sliderLine1.style.left = -offset1 + 'px';
})
// Оптимизировать. 3 и 4 блок





// 7 блок 
document.addEventListener("DOMContentLoaded", function () {
    const titles = document.querySelectorAll(".seventh_menu h3");


    titles.forEach(title => {
        title.addEventListener('click', function() {
            title.parentNode.classList.toggle('open');
    })
});
});