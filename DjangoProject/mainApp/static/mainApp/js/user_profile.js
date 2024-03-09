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