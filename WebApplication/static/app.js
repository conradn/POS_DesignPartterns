const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            products: null,
            searchQuerry: '',
            cart: null,
            total_amount: 0,
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
                    toastr.error('Please fill the form', '', { positionClass: 'toast-bottom-left' });
                    return;
                }
            }


            if (document.querySelector('#product-id').value.length > 0) {
                axios.post('/api/edit', formData)
                    .then(response => {
                        toastr.success(response.data.message, '', { positionClass: 'toast-bottom-left' });
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
                        toastr.success(response.data.message, '', { positionClass: 'toast-bottom-left' });
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

            if (confirmed) {
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

        addToCart() {

            const form = document.querySelector('#addProductToCartForm');

            const formData = new FormData(form);


            for (const pair of formData.entries()) {
                if (!pair[1] && pair[0] != 'id') {
                    toastr.error('Please fill the form', '', { positionClass: 'toast-bottom-left' });
                    return;
                }
            }

            axios.post('/api/add-to-cart', formData)

                .then(response => {
                    this.cart = response.data.products_in_cart;
                    this.total_amount = response.data.total_amount;
                    form.reset();
                })
                .catch(error => {
                    console.log(error.response.data);
                });
        },


        checkout() {

            if (this.total_amount == 0) {
                toastr.error('No products added yet!', '', { positionClass: 'toast-bottom-left' });
                return;
            }

            axios.get('/api/checkout')

                .then(response => {
                    toastr.success(response.data.message, '', { positionClass: 'toast-bottom-left' });
                    this.cart = null;
                    this.total_amount = 0;
                })
                .catch(error => {
                    console.log(error.response.data);
                });

        },

        getSales(){

        }
    },



})

app.mount('#app')
