<template>
    <div class="container">
        <div id="addBlog" v-if="!success">
            <form>
                <div class="form-group">
                    <label for="formInput0">Blog Title</label>
                    <input type="text" id="formInput0" class="form-control" placeholder="Input the blog title" v-model.lazy="blog.title">
                </div>
                <div class="form-group">
                    <label for="formInput1">Blog Content</label>
                    <textarea id="formInput1" class="form-control" placeholder="Input the blog content" v-model.lazy="blog.content"></textarea>
                </div>
            </form>
            <button class="btn btn-primary" v-on:click="quack" style="display: block; margin: 0 auto;">Submit Blog</button>
        </div>
        <div v-if="success">
            <h3>Blog successfully submitted</h3>
            <p>Automatically redirecting to home page in 3 seconds</p>
        </div>
        <div v-if="error">
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
            error: false
        }
    },
    methods: {
        quack(){
            console.log(this.blog);
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
                this.$router.push({path: '/add'});
            })

            //this.$router.push({path: '/'});
        }
    }
}
</script>
