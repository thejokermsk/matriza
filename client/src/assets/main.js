$( document ).ready(function() {

  $('.mat-drawer-content').on('scroll', function($event) {

    $('.russia-company').css('left', -$('.mat-drawer-content').scrollLeft() + 30)
    // $('.company__times').css('top', -$('.mat-drawer-content').scrollTop() + 154)
  })

});
