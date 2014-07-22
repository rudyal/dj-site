
// TODO: 

//  3. Insert Breakpoints
//  4. Build wireframe Mockup of Final - Add sidebar with tagging/categories
//          categories: current events, trends, color, length, etc
//  5. Build Illustrator Mockup

var globalCount = 0;
var wclass = "w";

// X - Make Category Checkbox
// X - Make jQuery listner for checkbox
// X - Make Ajax call to apporpriate URL.py
// Return Data from ajax call
// Figure how to use data to populate main content area
// Streamline categories - ensure multiple categories will work

// Make a switch statement to check what categories are check,
  // Then Call the appropiate functions or pass appropiate data

// Also When a category is clicked make sure that all items are removed and new ones inserted

// Fill landing page with content
docReady( function() {
      loadMore();
      loadMore();
      loadMore();
});

// CATEGORIES
// ONclick of categories - gets getajax
var someObj={};
someObj.catGranted=[];
someObj.catDenied=[];



docReady( function() {
  $("input:checkbox").change(function() {
    var someObj = {};
    someObj.catGranted = [];
    someObj.catDenied = [];

    $("input:checkbox").each(function() {
        if ($(this).is(":checked")) {
            someObj.catGranted.push($(this).attr("id"));
        } else {
            someObj.catDenied.push($(this).attr("id"));
        }
    });
    //Take Out current items
      $( ".item" ).remove();
      // Take to top of page
      $('html, body').animate({ scrollTop: 0 }, 0);
    //Fill with filtered items
      getAjax(someObj.catGranted);
    //alert("GRANTED: " + someObj.catGranted);
    //alert("DENIED: " + someObj.catDenied);
  });

});

var tag = "1";

// Gets json of categories
function getAjax(someOb){
  //Now we have an array of the categories!
  console.log("HERE -------------------   ---------------");
  
  someOb = [1,2];
  console.log(someOb);
  //Now we just need to parse the tags, assign variables, and put in get json method
  console.log({someOb:someOb});
  $.getJSON('/api/v1/pic/?', {
    'tags' : 2,
    //'tags' : {someOb:someOb},
    'tags' : 1,
    'format' : 'json',
  }, function(data) {
        // We have filtered JSON objects
        console.log(data);
        // We just need to populate main content with data
 });

}


//ON SCROLL
//On scroll at bottom of page, load more content, check categories here?
//Calls loadMore()
$(window).scroll(bindScroll);
function bindScroll(){
   if($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
       $(window).unbind('scroll');
       loadMore();
   }
}

// Calls getItemElement2
function loadMore()
{
   console.log("More loaded");

   console.log(globalCount);

   // TODO Check if category is checked
   for ( var i = 1; i < 10; i++ ) {
      getItemElement2(globalCount);
      globalCount += 1;
      console.log(globalCount);
    }
    $("body").append("<div>");
   $(window).bind('scroll', bindScroll);
 }

// Calls addItem, passes elements
function getItemElement2(count) {
  $.getJSON('/api/v1/pic/?format=json', function(data) {
        var elem = document.createElement('img');
        var picsrc = data.objects[count].picture;
          
          var w1class = getWclass();
          elem.className = 'item ' + w1class;

          elem.setAttribute("src", picsrc);
          console.log(elem);
          addItem(elem);
 });
}

// Adds elements to container
function addItem(elem){
  var container = document.querySelector('.masonry');
    var elems = [];
    var fragment = document.createDocumentFragment();
    fragment.appendChild( elem );
    elems.push( elem );
    container.appendChild( fragment );
}

// Assigns w class for .items - gives width and height
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

// Makes filter button fixed
$(window).scroll(function(){
  var navPos = $('.sidebar').position().top+$('.sidebar').outerHeight(true);
  var fixIT = $(this).scrollTop() >= navPos;
  var setPos = fixIT ? 'fixed' : 'relative' ;
  $('.sidebar').css({position: setPos});
}); 

// Toggle left menu
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



//Not really sure, used for mason width scale
//window.onload = function(){ 
var transitionProp = getStyleProperty('transition');
var transitionEndEvent = {
  WebkitTransition: 'webkitTransitionEnd',
  MozTransition: 'transitionend',
  OTransition: 'otransitionend',
  transition: 'transitionend'
}[ transitionProp ];


//Masonry stuff, makes width scale with page, i think
docReady( function() {

  var container = document.querySelector('.masonry');
  var msnry = new Masonry( container, {
    itemSelector: '.item',
    columnWidth: '.grid-sizer'
  });
});

//};