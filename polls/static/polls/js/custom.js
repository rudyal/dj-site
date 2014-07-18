
// TODO: 
// http://themes.themeton.com/mana/blog/masonry-layout-left-sidebar/
//  2. Iron out formating
       // Need to load on break, then ensure smooth scrolling
       // Need to make pictures various sizes. w=width and h=height
//  2.5 make sidebar that doesnt move, has checkboxes and such
  // side bar and main are 2 seperate divs, their max widths should complement each other
  // have little fixed icon on screen when scrolling down
//  3. Insert Breakpoints
//  4. Build wireframe Mockup of Final - Add sidebar with tagging/categories
//          categories: current events, trends, color, length, etc
//  5. Build Illustrator Mockup

//$(document).ready(addItem);
//$(document).ready(getJSON);
var globalCount = 0;
var wclass = "w";

/*  
 *  This Function grabs JSON from URL and parses it,
 *    then inserts into HTML
*/

// How to do categories and filtering?
  // Make a second getJSON method that takes array, 
  // the array is a list of categories.

function getJSON() {
$.getJSON('/api/v1/pic/?format=json', function(data) {
        var output="<ul>";
        for (var i in data.objects) {
          //var pic = JSON.stringify();
          output+="<li>" + data.objects[i].date 
          + " " + "<img src=\"" + data.objects[i].picture + "\"height=\"42\" width=\"42\">"
          + "--" + data.objects[i].gender+"</li>";
        }
        output+="</ul>";
        //output=JSON.stringify(data.objects);
        document.getElementById("placeholder").innerHTML=output;

 });
}

function getItemElement2(count) {
  $.getJSON('/api/v1/pic/?format=json', function(data) {
        var elem = document.createElement('img');
        var picsrc = data.objects[count].picture;

          // Test Code
          // var item = "";
          // // item.className = 'is-loading';
          // var size = Math.random() * 3 + 1;
          // var width = Math.random() * 110 + 100;
          // width = Math.round( width * size );
          // var height = Math.round( 140 * size );
          // var rando = Math.ceil( Math.random() * 1000 );
          // var src = rando < 100 ? '//foo/broken-' + rando + '.jpg' :
          //   // use lorempixel for great random images
          //   'http://lorempixel.com/' + width + '/' + height + '/' + '?' + rando;
          // item += '<img class="item "  src="' + src + '" />';

          // My way
          // Get image dimensions from 
          // Test if image is appropriate for position
          // OR give appropriate css tag
          // OR give inline styling tag
          
          
          var w1class = getWclass();
          elem.className = 'item ' + w1class;

          elem.setAttribute("src", picsrc);
          console.log(elem);
          addItem(elem);
 });
}

function addItem(elem){
	var container = document.querySelector('.masonry');
	  var elems = [];
    var fragment = document.createDocumentFragment();
    fragment.appendChild( elem );
    elems.push( elem );
    container.appendChild( fragment );
}

function loadMore()
{
   console.log("More loaded");

   console.log(globalCount);
   for ( var i = 1; i < 10; i++ ) {
      getItemElement2(globalCount);
      globalCount += 1;
      console.log(globalCount);
    }
    $("body").append("<div>");
   $(window).bind('scroll', bindScroll);
 }

function bindScroll(){
   if($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
       $(window).unbind('scroll');
       loadMore();
   }
}

function getWclass(){
   if(wclass=="w" || wclass=="w7a"){
            wclass = "w1a";
            return "w1a";
          }else if(wclass=="w1a"){
            wclass = "w2a";
            return "w2a";
          }else if(wclass=="w2a"){
            wclass = "w3a";
            return "w3a";
          }else if(wclass=="w3a"){
            wclass = "w4a";
            return "w4a";
          }else if(wclass=="w4a"){
            wclass = "w5a";
            return "w5a";
          }else if(wclass=="w5a"){
            wclass = "w6a";
            return "w6a";
          }else if(wclass=="w6a"){
            wclass = "w7a";
            return "w7a";
          }else{
            return "w1a";
          }
}

$(function() {

  $('#mobilebars').click(function(){
    alert('hello ladie');
  });

});

$(window).scroll(function(){

  var navPos = $('.sidebar').position().top+$('.sidebar').outerHeight(true);
  var fixIT = $(this).scrollTop() >= navPos;
  var setPos = fixIT ? 'fixed' : 'relative' ;

  $('.sidebar').css({position: setPos});

}); 

$(window).scroll(bindScroll);



window.onload = function(){ 
      var menuLeft = document.getElementById( 'cbp-spmenu-s1' ),
      body = document.body,
      showLeft = document.getElementById( 'showLeft' );
       
      showLeft.onclick = function() {
        classie.toggle( this, 'active' );
        classie.toggle( body, 'cbp-spmenu-push-toright' );
        classie.toggle( menuLeft, 'cbp-spmenu-open' );
        disableOther( 'showLeft' );
      };
       
      function disableOther( button ) {
      if( button !== 'showLeft' ) {
      classie.toggle( showLeft, 'disabled' );
      }
      }
    };





//window.onload = function(){ 
var transitionProp = getStyleProperty('transition');
var transitionEndEvent = {
  WebkitTransition: 'webkitTransitionEnd',
  MozTransition: 'transitionend',
  OTransition: 'otransitionend',
  transition: 'transitionend'
}[ transitionProp ];

docReady( function() {

  var container = document.querySelector('.masonry');
  var msnry = new Masonry( container, {
    itemSelector: '.item',
    columnWidth: '.grid-sizer'
  });
});

//};