$(window).on('load', function () {
  'use strict';

  $(
    '.wrapper, .chat-list, .messages-line, .suggestions-inner, .nott-list .nott-inner, .pf-gallery '
  ).mCustomScrollbar({
    axis:"y",
    theme:'dark',
    integer: 100,
    setLeft: 0,
    scrollbarPosition:'inside'
  });

  $('.skill-tags').mCustomScrollbar({
    axis:"x",
    theme:'dark',
    integer: 100,
    setLeft: 0,
    scrollbarPosition:'outside'
  });
  //  ============= SIGNIN SWITCH TAB FUNCTIONALITY =========

  $('.tab-feed ul li').on('click', function () {
    var tab_id = $(this).attr('data-tab');
    $('.tab-feed ul li').removeClass('active');
    $('.product-feed-tab').removeClass('current');
    $(this).addClass('active animated fadeIn');
    $('#' + tab_id).addClass('current animated fadeIn');
    return false;
  });

  //  ============= OVERVIEW EDIT FUNCTION =========

  $('.overview-open').on('click', function () {
    $('#overview-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#overview-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============= EXPERIENCE EDIT FUNCTION =========

  $('.exp-bx-open').on('click', function () {
    $('#experience-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#experience-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============= EDUCATION EDIT FUNCTION =========

  $('.ed-box-open').on('click', function () {
    $('#education-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#education-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============= LOCATION EDIT FUNCTION =========

  $('.lct-box-open').on('click', function () {
    $('#location-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#location-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============= SKILLS EDIT FUNCTION =========

  $('.skills-open').on('click', function () {
    $('#skills-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#skills-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });


  //  ============= Post Image Sider =========

  $('.post-slider').owlCarousel({
    items: 1,
    nav: true,
    dots: false,
    loop: false,
    margin: 50,
    smartSpeed: 1200
  });

  //  ============= ESTABLISH EDIT FUNCTION =========

  $('.esp-bx-open').on('click', function () {
    $('#establish-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#establish-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============= CREATE PORTFOLIO FUNCTION =========

  $('.portfolio-btn > a').on('click', function () {
    $('#create-portfolio').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#create-portfolio').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============= EMPLOYEE EDIT FUNCTION =========

  $('.emp-open').on('click', function () {
    $('#total-employes').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#total-employes').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  =============== Ask a Question Popup ============

  $('.ask-question').on('click', function () {
    $('#question-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#question-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============== ChatBox ==============

  $('.chat-mg').on('click', function () {
    $(this).next('.conversation-box').toggleClass('active');
    return false;
  });
  $('.close-chat').on('click', function () {
    $('.conversation-box').removeClass('active');
    return false;
  });

  //  ================== Edit Options Function =================

  $('.ed-opts-open').on('click', function () {
    $(this).next('.ed-options').toggleClass('active');
    return false;
  });

  // ============== Menu Script =============

  $('.menu-btn > a').on('click', function () {
    $('nav').toggleClass('active');
    return false;
  });

  //  ============ Notifications Open =============

  $('.not-box-open').on('click', function () {
    $('#message').hide();
    $('.user-account-settingss').hide();
    $(this).next('#notification').toggle();
  });

  //  ============ Messages Open =============

  $('.not-box-openm').on('click', function () {
    $('#notification').hide();
    $('.user-account-settingss').hide();
    $(this).next('#message').toggle();
  });

  // ============= User Account Setting Open ===========

  $('.user-info').click(function () {
    $('.user-account-settingss').slideToggle('fast');
    $('#message').not($(this).next('#message')).slideUp();
    $('#notification').not($(this).next('#notification')).slideUp();
    // Animation complete.
  });

  //  ============= FORUM LINKS MOBILE MENU FUNCTION =========

  $('.forum-links-btn > a').on('click', function () {
    $('.forum-links').toggleClass('active');
    return false;
  });
  $('html').on('click', function () {
    $('.forum-links').removeClass('active');
  });
  $('.forum-links-btn > a, .forum-links').on('click', function () {
    e.stopPropagation();
  });
});
