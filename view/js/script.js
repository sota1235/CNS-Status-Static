var ajax = new Ajax('http://web.sfc.keio.ac.jp/~#{your_login_name}/#{printer}/json.php');
var place = [
  "ITC事務室入り口横(壁側)",
  "ITC 入り口横左",
  "ITC 入り口横右",
  "メディアセンター右",
  "メディアセンター左",
  "λ11左",
  "λ11右",
  "λ21",
  "λ18",
  "O17",
  "I18",
  "E17",
  "K18",
  "K教室棟2階",
  "I教室棟2階"
]

ajax.on_get = function(data){
  /* parse */
  var json = $.parseJSON(data);
  var date = json['date'];
  var p_status = json['status'];

  /* remove table */
  $('tbody tr').remove();

  /* insert into table */
  for(var i=0;i<p_status.length;i++){
    var $tr = $('<tr></tr>');
    var judge = [25, 50, 50]; // トレイ1,2,3の警告基準

    $tr.append($('<td></td>').text(place[i]));
    for(var j=0;j<3;j++){
      /* メール本文がエラーの際、そのまま表示するよう処理 */
      var re = /^\d+%$/;
      if(!re.test(p_status[i][j])) {
        $tr.append($('<td colspan="3"></td>')
            .css("background-color", "#FF8080")
            .css("color", "#FFFFFF")
            .text('Error: 元のメール本文を確認してください'));
        break;
      }

      if(Number(p_status[i][j].slice(0, -1)) <= judge[j]){
        $tr.append($('<td></td>')
            .css("background-color","#FF8080")
            .css("color", "#FFFFFF")
            .text(p_status[i][j]));
      } else {
        $tr.append($('<td></td>')
            .text(p_status[i][j]));
      }
    }
    $('tbody').append($tr);
  }
  $('#date').text(date);
}

$(function() {
  ajax.get();
});
