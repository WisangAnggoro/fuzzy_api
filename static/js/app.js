var inputs = {};

function getInputs() {
  inputs['speed'] = $('#speed').val();
  inputs['distance'] = $('#distance').val();
}

$(document).ready(function(){

  $('#calc').click(function(){
    getInputs();
    $('td#speed').text(inputs['speed']);
    $('td#distance').text(inputs['distance']);
    $.ajax({
        url: '/',
        type: 'POST',
        data: JSON.stringify(inputs),
        contentType: 'application/json',
        success: function(data) {
            console.log('Wysłano dane wejsciowe');
            $('.result-plot').html(data[0])
            $('#power').text(data[1].toFixed(2))},
        error: function(data) {
            console.log('Dane nie zostaly wyslane.');
            alert("Zla wartosc! Predkosc od 1 do 19, Dystans od 1 do 99!")
        }
    }); 
  });
});
