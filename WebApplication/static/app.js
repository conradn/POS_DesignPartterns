const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            products: null,
            searchQuerry: '',
        }
    },

    mounted() {
        this.getProducts()
    },

    methods: {
        newProduct() {
            const form = document.querySelector('#newProductForm');

            const formData = new FormData(form);


            for (const pair of formData.entries()) {
                if (!pair[1] && pair[0] != 'id') {
                    toastr.success('Please fill the form', 'Info', { positionClass: 'toast-bottom-left' });
                    return;
                }
            }


            if (document.querySelector('#product-id').value.length > 0) {
                axios.post('/api/edit', formData)
                    .then(response => {
                        toastr.success(response.data.message, 'Info', { positionClass: 'toast-bottom-left' });
                        form.reset();

                        let addBtn = document.querySelector('.add-btn');
                        addBtn.innerHTML = 'Add Product'
                        this.getProducts()
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    });

            } else {
                axios.post('/api/add', formData)
                    .then(response => {
                        toastr.success(response.data.message, 'Info', { positionClass: 'toast-bottom-left' });
                        form.reset();
                        this.getProducts()
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    });

            }



        },

        getProducts() {
            axios.get('/api/products')
                .then(response => {
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error.response.data);
                });
        },

        searchProduct() {

            const formData = new FormData();
            formData.append('querry', this.searchQuerry)

            axios.post('/api/search', formData)

                .then(response => {
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error.response.data);
                });
        },

        editProduct(product) {

            let prodID = document.querySelector('#product-id');
            let prodName = document.querySelector('#product-name');
            let prodPrice = document.querySelector('#product-price');
            let prodQuantity = document.querySelector('#product-quantity');
            let addBtn = document.querySelector('.add-btn');

            prodID.value = product.id;
            prodName.value = product.name;
            prodPrice.value = product.price;
            prodQuantity.value = product.quantity;
            addBtn.innerHTML = 'Save Changes'
        },

        deleteProduct(id) {

            var confirmed = confirm('Are you sure you want to delete this product?');

            if (confirmed){
                axios.delete(`api/delete/${id}`)
                    .then(response => {
                        toastr.success('Deleted successfully', 'Info', { positionClass: 'toast-bottom-left' });
                        this.getProducts();
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    });
            }




        },

        addToCart(){

        }
    },



})

app.mount('#app')
