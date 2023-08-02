$(function () {
    $(document).scroll(function () {
      var $nav = $("nav");
      $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
  });

// Initialize and add the map
function initMap() {
  // The location of the cabinet
  var cab = {lat: 44.426488, lng: 26.115333};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 15, center: cab});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: cab, map: map});
  }


function myFunction() {
  var x = document.getElementById("header_base");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
  console.log("work");
}

myFunction();