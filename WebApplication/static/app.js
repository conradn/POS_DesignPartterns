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

            $('#newProductModal').modal('hide')

            const formData = new FormData(form);

            for (const pair of formData.entries()) {
                if (!pair[1]) {
                    toastr.success('Please fill the form', 'Info', { positionClass: 'toast-bottom-left' });
                    return;
                }
            }

            axios.post('/api/add', formData)
                .then(response => {
                    toastr.success(response.data.message, 'Info', { positionClass: 'toast-bottom-left' });
                    this.getProducts()
                })
                .catch(error => {
                    console.log(error.response.data);
                });


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
            formData.append('querry',this.searchQuerry)

            axios.post('/api/search',formData)

                .then(response => {
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error.response.data);
                });
        }
    },



})

app.mount('#app')
