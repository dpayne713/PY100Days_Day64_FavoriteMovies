document.addEventListener("click", function(event){

    if (event.target.classList.contains('delete-button')) {
        let id = event.target.dataset.id
        location.assign("/delete/" + id)
    }

    if (event.target.classList.contains('update-button')) {
        event.preventDefault()
        let id = event.target.dataset.id
        update(id)

    }

    // if (event.target.id === "search") {
    //     openModal()
    // }
    if (event.target.classList.contains('closeModal')) {
        closeModal()
    }

})

// SEARCH MODAL FUNCTIONALITY


function openModal() {
    document.getElementById("myModal").style.display = "block"
    document.getElementById("myModal").classList.add("show")
}
function closeModal() {
    document.getElementById("myModal").style.display = "none"
    document.getElementById("myModal").classList.remove("show")
}

// UPDATE MODAL FUNCTIONALITY

function update(id){
    fetch('/update/'+id)
    .then(function (response) {
        switch (response.status) {
            // status "OK"
            case 200:
                return response.text();
            // status "Not Found"
            case 404:
                throw response;
        }
    })
    .then(function (template) {
        document.getElementById("updateModalBody")
            .innerHTML = template;
        openModal()
        })

}
