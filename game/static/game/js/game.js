$(function () {
  $('[data-toggle="popover"]').popover({ trigger: "hover" });
});

$("#sort-selector").change(function () {
  var selector = $(this);
  var currentUrl = new URL(window.location);

  var selectedVal = selector.val();
  if (selectedVal != "reset") {
    var sort = selectedVal.split("_")[0];
    var direction = selectedVal.split("_")[1];

    currentUrl.searchParams.set("sort", sort);
    currentUrl.searchParams.set("direction", direction);

    window.location.replace(currentUrl);
  } else {
    currentUrl.searchParams.delete("sort");
    currentUrl.searchParams.delete("direction");

    window.location.replace(currentUrl);
  }
});


function enableDelete(e) {
  let product_id = e.getAttribute("data");
  console.log(product_id);
  document.getElementById(`disabled_btn${product_id}`).disabled = !e.checked;
}