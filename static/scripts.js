document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            alert("Form submitted. Searching for restaurants...");
            form.submit();
        });
    }
});
