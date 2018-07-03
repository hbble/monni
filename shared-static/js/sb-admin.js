(function($) {
    "use strict"; // Start of use strict

    // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
    $('body.fixed-nav .navbar-sidenav, body.fixed-nav .sidenav-toggler, body.fixed-nav .navbar-collapse').on('mousewheel DOMMouseScroll', function(e) {
        var e0 = e.originalEvent,
            delta = e0.wheelDelta || -e0.detail;
        this.scrollTop += (delta < 0 ? 1 : -1) * 30;
        e.preventDefault();
    });
    // Scroll to top button appear
    $(document).scroll(function() {
        var scrollDistance = $(this).scrollTop();
        if (scrollDistance > 100) {
            $('.scroll-to-top').fadeIn();
        } else {
            $('.scroll-to-top').fadeOut();
        }
    });
    // Configure tooltips globally
    $('[data-toggle="tooltip"]').tooltip()
    // Smooth scrolling using jQuery easing
    $(document).on('click', 'a.scroll-to-top', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top)
        }, 1000, 'easeInOutExpo');
        event.preventDefault();
    });
  
})(jQuery); // End of use strict

//enabling form input
function makeEditable(id){
    "use strict";
    $( document ).ready(function(event) {
        $('#edit-cat-'+id).prop('disabled', false);
        $('#edit-amount-'+id).prop('disabled', false);
        $('#btn-enable-form-'+id).removeAttr('onclick');
        $('#btn-enable-form-'+id).prop('id', 'btn-save-form-'+id);
        $('#btn-save-form-'+id).html(gettext('Save'));
        $('#btn-save-form-'+id).prop('type', 'submit');
    });
}

$('#deleteModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var id = button.data("id")
    var form = $('#del-form')
    var action = form.data("action").replace('/0/', '/'+id+'/')
    form.removeAttr('data-action')
    form.attr('action', action)

    console.log(id)
})


function preDelete(id){
    "use strict";
    $( document ).ready(function(event) {
        console.log("Delete clicked")
    });
  }
