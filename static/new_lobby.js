(function() {
    const signupForm = document.getElementById('signup')
    const pass1 = signupForm.querySelector('.passcode')
    const pass2 = signupForm.querySelector('.passcode2')
    const errorDiv = document.getElementById('error-message')
    const lobbyName = signupForm.querySelector('.group_name')
    const repMessage = document.getElementById('repeat-message')
    
    pass2.addEventListener("change", function(e) {
        if (pass1.value !== pass2.value) {
            errorDiv.style.display = 'block'
            pass2.value = ""
            e.preventDefault()
        } else {
            errorDiv.style.display = 'none'
        }
        
    })

    lobbyName.addEventListener("input", function(e) {
        if (lobbyName.value.includes("^")) {
            lobbyName.value =""
            repMessage.style.display = 'block'
        } else {
            repMessage.style.display = 'none'
        }
    })
})();

