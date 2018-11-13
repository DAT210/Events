

function displayEvent(event_id) {
    var event = document.getElementById(event_id)
    if ( event.style.display != "none") {
        event.style.display = "none";
        return;
    }

    var elements = document.getElementsByClassName("hidden")
    for (var i = 0; i < elements.length; i++){
        elements[i].style.display = "none";
    }

    document.getElementById(event_id).style.display = "";
  
}

function previewFile(){
    var preview = document.querySelector('img'); //selects the query named img
    var file    = document.querySelector('input[type=file]').files[0]; //sames as here
    var reader  = new FileReader();

    reader.onloadend = function () {
        preview.src = reader.result;
    }

    if (file) {
        reader.readAsDataURL(file); //reads the data as a URL
    } else {
        preview.src = "";
    }
}
