(function() {

    const main_form = document.getElementById('main-form')
    let people = document.querySelectorAll("div[id^='person']")
    const add_people = document.getElementById('add-person')
    const remove_person = document.getElementById('del-person')
    const send_button = document.getElementById('send-draws')
    const control_form = document.getElementById('control-form')
    const error_message = document.getElementById('error-message')

    // event listeners  

    main_form.oninput = (() => {
        if (main_form.checkValidity()) {
            main_form.submit()
        } else {
            error_message.style.display = "block"
        }
        
    })

    add_people.addEventListener("click", function(e) {
        add_person()
    })

    remove_person.addEventListener("click", function(e) {
        del_person()
        if (main_form.checkValidity()) {
            main_form.submit()
        }
    })

    send_button.addEventListener("click", function(e) {
        control_form.innerHTML += '<p>generating draws and sending emails</p>'
        setTimeout(function() {
            control_form.submit()
        },1000)
    })

    function add_person() {
        const currentPeople = document.querySelectorAll("div[id^='person']")
        const newDiv = document.createElement('div')
        newDiv.id = `person-${currentPeople.length+1}`
        newDiv.innerHTML = `
            <input name="person${currentPeople.length+1}-name" class="person${currentPeople.length+1}-name" type="name" placeholder="name ${currentPeople.length+1}" required>
            <input name="person${currentPeople.length+1}-email" class="person${currentPeople.length+1}-email" type="email" placeholder="email ${currentPeople.length+1}" required>
            <input name="person${currentPeople.length+1}-address" class="person${currentPeople.length+1}-address" type="text" placeholder="address ${currentPeople.length+1}" required> 
        `
        main_form.appendChild(newDiv)
    }



    function del_person() {
        people = document.querySelectorAll("div[id^='person']")
        person = document.getElementById(`person-${people.length}`)
        main_form.removeChild(person)
    }

    function getNameInDiv(div_name) {
        return div_name.querySelector("input[type=name]").value
    }

})()