(function() {

    const main_form = document.getElementById('main-form')
    let people = document.querySelectorAll("div[id^='person']")
    const add_people = document.getElementById('add-person')
    const remove_person = document.getElementById('del-person')
    const send_button = document.getElementById('send-draws')
    const control_form = document.getElementById('control-form')

    // event listeners 

    add_people.addEventListener("click", function(e) {
        add_person()
    })

    remove_person.addEventListener("click", function(e) {
        del_person()
    })

    send_button.addEventListener("click", function(e) {
        control_form.innerHTML += '<p>generating draws and sending emails</p>'
        setTimeout(function() {
            control_form.submit()
        },1000)
    })

    function add_person() {
        people = document.querySelectorAll("div[id^='person']")
        main_form.innerHTML += `<div id="person-${people.length+1}">
    <input name="person${people.length+1}-name" class="person${people.length+1}-name" type="name" placeholder="name ${people.length+1}" required>
    <input name="person${people.length+1}-email" class="person${people.length+1}-email" type="email" placeholder="email ${people.length+1}" required>
    <input name="person${people.length+1}-address" class="person${people.length+1}-address" type="text" placeholder="address ${people.length+1}" required> 
</div>`
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