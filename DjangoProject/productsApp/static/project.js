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