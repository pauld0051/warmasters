$(function () {
  $('[data-toggle="popover"]').popover({ trigger: "hover" });
});

function getCharacterInfo() {
  $.ajax({
    url: "{% url 'game_profile' %}",
    method: "get",
    type: "json",
    data: { character_name: $("#{{ character_choice.name }}").val() },
  });
}
