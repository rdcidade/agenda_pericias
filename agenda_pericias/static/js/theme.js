document.addEventListener("DOMContentLoaded", function() {
    const toggleThemeBtn = document.getElementById("toggle-theme");
    const body = document.body;

    // Verifica tema salvo anteriormente
    let theme = localStorage.getItem("theme") || "light";
    applyTheme(theme);

    toggleThemeBtn.addEventListener("click", function() {
        theme = theme === "light" ? "dark" : "light";
        applyTheme(theme);
        localStorage.setItem("theme", theme);
    });

    function applyTheme(theme) {
        if (theme === "dark") {
            body.classList.add("dark-mode");
            body.classList.remove("light-mode");
            toggleThemeBtn.textContent = "☀️";
        } else {
            body.classList.add("light-mode");
            body.classList.remove("dark-mode");
            toggleThemeBtn.textContent = "🌙";
        }
    }
});
