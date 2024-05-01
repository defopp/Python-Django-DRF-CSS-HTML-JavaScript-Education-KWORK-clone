

// IN PROGRESS
// class Slider {

//     constructor () {
//         this.offset = 0;
//     };

//     start () {

//         this.sliderLine = document.querySelector('.slider_items');
//         document.querySelector(".next_sl_bt").addEventListener('click', function () {
//             this.offset += 290;
//             if (this.offset > 580) {
//                 this.offset = 0
//             }
//             this.sliderLine.style.left = -this.offset + 'px';
//         });

//         document.querySelector(".prev_sl_bt").addEventListener('click', function () {
//             this.offset -= 290;
//             if (this.offset < 0) {
//                 this.offset = 580
//             }
//             this.sliderLine.style.left = -this.offset + 'px';
//         });

//     }
// }

// const a = new Slider()
// a.start()



GARBAGE
слайдер 1 //сделать слайдер
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


// class Slider {
//     constructor() {
//         this.offset = 0;
//     }

//     start() {
//         this.sliderLine = document.querySelector('.slider_items');

//         document.querySelector(".next_sl_bt").addEventListener('click', () => {
//             this.offset += 290;
//             if (this.offset > 580) {
//                 this.offset = 0;
//             }
//             this.sliderLine.style.left = -this.offset + 'px';
//         });

//         document.querySelector(".prev_sl_bt").addEventListener('click', () => {
//             this.offset -= 290;
//             if (this.offset < 0) {
//                 this.offset = 580;
//             }
//             this.sliderLine.style.left = -this.offset + 'px';
//         });
//     }
// }

// const a = new Slider();
// a.start();