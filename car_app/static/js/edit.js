function changeDetail(event, id){
    event.preventDefault()

    console.log(id)
    details = document.getElementById('new_detail')
   

    axios.post(`/brand/${id}/edit`, {
        details: details.value
    })

   

}