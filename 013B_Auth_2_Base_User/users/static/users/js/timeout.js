let element = document.querySelector(".alert");
let element2 = document.querySelector("#welcome");

element &&
  setTimeout(function () {
    element.style.display = "none";
  }, 3000);

element2 &&
  setTimeout(function () {
    element2.style.display = "none";
  }, 3000);
