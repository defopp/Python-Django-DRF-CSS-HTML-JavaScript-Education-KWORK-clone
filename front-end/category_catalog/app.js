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





// log logic// log logic// log logic// log logic// log logic// log logic// log logic
// log logic// log logic// log logic// log logic// log logic// log logic// log logic
// log logic// log logic// log logic// log logic// log logic// log logic// log logic
// log logic// log logic// log logic// log logic// log logic// log logic// log logic
const body = document.querySelector("body")
// hide log div by click outside the auth_container
function hideLogDiv(event) {
    if (authcont.contains(event.target)) {
        console.log('click in the div')
    }
    else {
        console.log('click outside the div')
        closeLogDiv(authdiv, regdiv, signindiv, authcont)
        document.removeEventListener('click', hideLogDiv)
    }
}

// close/open
function closeLogDiv(authdiv, regdiv, signindiv,authcont){
    authcont.style.transform = 'scale(0)'

    setTimeout(function(){
        authdiv.style.display = "none";
        regdiv.style.display = "none";
        signindiv.style.display = "none";
        body.style.overflow = 'scroll'
    }, 100)
}

function openSignIn(authdiv, regdiv, signindiv,authcont){
    authdiv.style.display = "flex";
    regdiv.style.display = "none";
    signindiv.style.display = "flex";
    
    console.log('open sign in');

    body.style.overflow = 'hidden';
    
    setTimeout(function(){
        authcont.style.transform = 'scale(1)'
    }, 100)
    
    setTimeout(function(){
        document.addEventListener('click', hideLogDiv);
    }, 1000)
}

function openSignUp(authdiv, regdiv, signindiv,authcont){
    authdiv.style.display = "flex";
    regdiv.style.display = "flex";
    signindiv.style.display = "none";

    console.log('open sign up');
    
    body.style.overflow = 'hidden';

    setTimeout(function(){
        authcont.style.transform = 'scale(1)'
    }, 100)

    setTimeout(function(){
        document.addEventListener('click', hideLogDiv);
    }, 1000)
}

// buttons and divs
const SignUpButtons = document.querySelectorAll('#signup')
const SignInButtons = document.querySelectorAll('#signin')

const authdiv = document.querySelector('.authdiv')
const authcont = document.querySelector('.auth_container')
const regdiv = document.querySelector('.regdiv')
const signindiv = document.querySelector('.signindiv')

// buttons logic
SignUpButtons.forEach(button => {
    button.addEventListener('click', function () {
        openSignUp(authdiv, regdiv, signindiv, authcont);
    })
});    

SignInButtons.forEach(button => {
    button.addEventListener('click', function () {
        openSignIn(authdiv, regdiv, signindiv, authcont)
    })
});       



// log logic// log logic// log logic// log logic// log logic// log logic// log logic
// log logic// log logic// log logic// log logic// log logic// log logic// log logic
// log logic// log logic// log logic// log logic// log logic// log logic// log logic
// log logic// log logic// log logic// log logic// log logic// log logic// log logic




























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


