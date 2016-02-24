( function( $ ) {
$( document ).ready(function() {
$('#appmenu').prepend('<div id="menu-button">Menu</div>');
  $('#appmenu #menu-button').on('click', function(){
    var menu = $(this).next('ul');
    if (menu.hasClass('open')) {
      menu.removeClass('open');
    }
    else {
      menu.addClass('open');
    }
  });
});
} )( jQuery );