
// drop menu
document.addEventListener("DOMContentLoaded", function () {

    const button = document.querySelector(".menu");

    button.addEventListener('click', function() {
    button.parentNode.classList.toggle('open');
    })  
});



// логика интупа категории
document.querySelectorAll('.detcat').forEach(detailcat =>
    detailcat.addEventListener('click', function(e) {
      var input = document.querySelector('.categoryinput');
      input.value = detailcat.value;
      document.querySelector(".menu").parentNode.classList.remove('open');
    })
  );