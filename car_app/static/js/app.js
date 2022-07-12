function getBrand(event){
    event.preventDefault()
    
    brandName = document.getElementById('brand_name');
    brandDetails = document.getElementById('brand_details');
    change = document.getElementById('hello')

    axios.post('/brand/new/', {
        brandName: brandName.value,
        brandDetails: brandDetails.value,
        extra_info: 'hello'
    })
    // .then((response =>{ 
    //     change.innerHTML = response.data.brandDetails
    // }))
}
