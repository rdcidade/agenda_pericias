// static/js/fontsize.js

document.addEventListener("DOMContentLoaded", function() {
    const increaseBtn = document.getElementById("increase-font");
    const decreaseBtn = document.getElementById("decrease-font");
    const root = document.documentElement;

    // Tamanho base inicial (em pixels)
    let fontSize = parseFloat(localStorage.getItem("fontSize")) || 16;

    // Aplica o tamanho salvo no localStorage
    root.style.fontSize = fontSize + "px";

    increaseBtn.addEventListener("click", function() {
        if (fontSize < 24) { // limite máximo
            fontSize += 1;
            root.style.fontSize = fontSize + "px";
            localStorage.setItem("fontSize", fontSize);
        }
    });

    decreaseBtn.addEventListener("click", function() {
        if (fontSize > 12) { // limite mínimo
            fontSize -= 1;
            root.style.fontSize = fontSize + "px";
            localStorage.setItem("fontSize", fontSize);
        }
    });
});
