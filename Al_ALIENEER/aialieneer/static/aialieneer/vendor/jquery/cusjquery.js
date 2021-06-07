//////////////////////////       Custome Jquery       //////////////////////////

////////  Display All Courses  ////////

<script>

$(document).ready(function(){
    {/* Display COURSES Courses */}
  $("#courses").click(function(){
    $("#courses").show();
    $("#dl").hide();
    $("#cv").hide();
    $("#nlp").hide();
    $("#cpp").hide();
    $("#ml").hide();
  });

  {/* Display ML Courses */}
  $("#ml").click(function(){
    $("#ml").show();
    $("#dl").hide();
    $("cv").hide();
    $("nlp").hide();
    $("cpp").hide();
    $("courses").hide();
  });

  {/* Display DL Courses */}
  $("#dl").click(function(){
    $("#dl").show();
    $("#ml").hide();
    $("cv").hide();
    $("nlp").hide();
    $("cpp").hide();
    $("courses").hide();
  });

  {/* Display CV Courses */}
  $("#cv").click(function(){
    $("#cv").show();
    $("#ml").hide();
    $("dl").hide();
    $("nlp").hide();
    $("cpp").hide();
    $("courses").hide();
  });

  {/* Display NLP Courses */}
  $("#nlp").click(function(){
    $("#nlp").show();
    $("#ml").hide();
    $("dl").hide();
    $("cv").hide();
    $("cpp").hide();
    $("courses").hide();
  });

  {/* Display CPP Courses */}
  $("#cpp").click(function(){
    $("#cpp").show();
    $("#ml").hide();
    $("dl").hide();
    $("cv").hide();
    $("nlp").hide();
    $("courses").hide();
  });
  
});

</script>

///////////////////////////////////////