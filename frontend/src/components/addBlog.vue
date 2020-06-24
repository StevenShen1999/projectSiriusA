<template>
    <div class="container">
        <div id="addBlog" v-if="!success">
            <form @submit.prevent="quack">
                <div class="form-group">
                    <label for="formInput0">Blog Title</label>
                    <input type="text" id="formInput0" class="form-control" placeholder="Input the blog title" v-model.lazy="blog.title" @blur="checkInput" required/>
                </div>
                <div class="form-group">
                    <label for="formInput1">Blog Content</label>
                    <textarea id="formInput1" class="form-control" placeholder="Input the blog content" v-model.lazy="blog.content" @blur="checkInput" required/>
                </div>
                <button type="submit" class="btn btn-primary" style="display: block; margin: 0 auto;" :disabled="formError">Submit Blog</button>
            </form>
        </div>
        <div v-if="success">
            <h3>Blog successfully submitted</h3>
            <p>Automatically redirecting to home page in 3 seconds</p>
        </div>
        <div v-else-if="error">
            <div class="container">
                <h3 style="text-align: center; color: red;">Blog submittion not successful</h3>
                <p style="text-align: center; color: red;">Please try again</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            blog: {
                title: '',
                content: ''
            },
            success: false,
            error: false,
            formError: false
        }
    },
    methods: {
        quack(event){
            console.log("Posted")
            this.$http.post('http://localhost:5000/blog', {
                title: this.blog.title,
                content: this.blog.content
            }).then((data) => {
                this.success = true;
                setTimeout(() => {
                    this.$router.push({path: '/'});
                }, 3000);
            }).catch((data) => {
                console.log(data);
                this.error = true;
                //this.$router.push({path: '/add'});
            })
        },
        checkInput(event){
            if (!event.target.value){
                // Set some different conditions here
                this.formError = true
                this.$nextTick(() => event.target.setCustomValidity("Please don't leave this empty."))
            } else {
                this.formError = false
                this.$nextTick(() => event.target.setCustomValidity(""))
            }
        }
    }
}
</script>
