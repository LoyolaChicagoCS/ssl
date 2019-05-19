$(document).ready(function() {
  $(window).scroll(function(){
    if ($(this).scrollTop() > 2500) {
      $('.scrollToTop').fadeIn(500);
    } else {
      $('.scrollToTop').fadeOut(500);
    }
  });
});

$('.scrollToTop').click(function() {
  $('html, body').animate({scrollTop: 0}, 1000)
})
