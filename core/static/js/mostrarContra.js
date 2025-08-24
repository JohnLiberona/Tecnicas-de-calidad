const passwordFields = document.querySelectorAll("input[type='password']"),
      icon = document.querySelector(".pass-icon"),
      openEye = icon.getAttribute("data-open"),
      closeEye = icon.getAttribute("data-close");
      
icon.addEventListener("click", e => {
    passwordFields.forEach(password => {
        if (password.type === "password") {
            password.type = "text";
        } else {
            password.type = "password";
        }
    });

    if (passwordFields[0].type === "password") {
        icon.src = closeEye;
    } else {
        icon.src = openEye;
    }
});
