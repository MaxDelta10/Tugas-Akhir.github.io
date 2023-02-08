$("#predict_button").click(function(){
  var message = $("message").val();
  $.ajax({
    type: "POST",
    url: "/predict",
    data: {message: message},
    success: function(result){
      $("#result").html(result);
    }
  });
});
