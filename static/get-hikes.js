$.get(('/hike_search_result'),(data) => {
    alert(data)
}); 



// function hike_search_result(trails) {
//     $("#hike_trails").html;
// }

// function showhikes(evt) {
//     evt.preventDefault();

//     let url = "/result_hikes";
//     let formData = {"hike_trails": $("field").val()};

//     $.get(url, formData, replaceForecast);
// }

// $("#hike_trail").on('submit', showhikes)

$(document).ready(function(){
    $('#tra').on('change', function() {
        var trail_id = $(this).val();
//         fetch('/result_hikes?difficulty=' + difficulty)
// .then(....)
        fetch('/' + difficulty).then(function(data) {
            // this console.log is me testing to see what data returns
            console.log(trail_id,trail_name,summary);
        });
    });
});