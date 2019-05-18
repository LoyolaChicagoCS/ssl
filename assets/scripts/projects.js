$(document).ready(function() {
  $('#learn-more').on('click', function() {
    $("#learn-more-expanded").slideToggle(500);
  });

  $(function() {
    $("#learn-more").click(function() {
      $(this).toggleClass('foo');
      $(this).text(function(i, text) {
        return text === "CLOSE" ? "LEARN MORE" : "CLOSE";
      })
    });
  })
});
