/*-----------------------------------------------------------
* Template Name    : Oskar - Responsive Bootstrap 4 Landing Template
* Author           : CreataThemes
* Created          : dec 2018
*------------------------------------------------------------
*/



(function ($) {

    'use strict';

    function initStickyAdd() {
        $(window).on('scroll',function() {
            var scroll = $(window).scrollTop();

            if (scroll >= 50) {
                $(".sticky").addClass("stickyadd");
            } else {
                $(".sticky").removeClass("stickyadd");
            }
        });
    }
    function initSmoothNav() {
        $('.navbar-nav a').on('click', function(event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top - 0
            }, 1500, 'easeInOutExpo');
            event.preventDefault();
        });
    }
    function initScrollspy() {
        $("#navbarCollapse").scrollspy({
            offset:20
        });
    }

 
    function initPortfolio() {
        $(window).on('load', function() {
            var $container = $('.work-filter');
            var $filter = $('#menu-filter');
            $container.isotope({
                filter: '*',
                layoutMode: 'masonry',
                animationOptions: {
                    duration: 750,
                    easing: 'linear'
                }
            });

            $filter.find('a').on("click", function() {
                var selector = $(this).attr('data-filter');
                $filter.find('a').removeClass('active');
                $(this).addClass('active');
                $container.isotope({
                    filter: selector,
                    animationOptions: {
                        animationDuration: 750,
                        easing: 'linear',
                        queue: false,
                    }
                });
                return false;
            });
        });
    }



$(window).on('scroll',function(){
    if ($(this).scrollTop() > 100) {
        $('.back_top').fadeIn();
    } else {
        $('.back_top').fadeOut();
    }
}); 
$('.back_top').on('click',function(){
    $("html, body").animate({ scrollTop: 0 }, 1000);
    return false;
});

$('.img-zoom').magnificPopup({
    type: 'image',
    closeOnContentClick: true,
    mainClass: 'mfp-fade',
    gallery: {
        enabled: true,
        navigateByImgClick: true,
        preload: [0, 1]
    }
});
    
    function init() {
        initStickyAdd();
        initSmoothNav();
        initScrollspy();
        initPortfolio();
        
    }

    init();

})(jQuery);