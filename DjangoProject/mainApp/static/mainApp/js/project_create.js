
// drop menu
document.addEventListener("DOMContentLoaded", function () {

    const button = document.querySelector(".menu");

    button.addEventListener('click', function() {
    button.parentNode.classList.toggle('open');
    })  
});