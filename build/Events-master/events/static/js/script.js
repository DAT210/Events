

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
