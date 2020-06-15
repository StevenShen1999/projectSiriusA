<template>
    <div id="container">
        <div id="singleBlog" v-if="!error">
            <h1>{{ blog.title }}</h1>
            <p>{{ blog.content }}</p>
            <h5>{{ blog.createdOn }}</h5>
        </div>
        <div v-else-if="error">
            <h1 style="text-align: center; color: red;">No such blog</h1>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            id: this.$route.params.id,
            blog: {},
            error: false
        }
    }, 
    created() {
        this.$http.get('http://localhost:5000/blog?id=' + this.id).then((data) => {
            this.blog = data.body;
        }).catch((data) => {
            console.log("No such blog");
            console.log(data);
            this.error = true;
        });
    }
}
</script>

<style>
#container{
    width: 80%;
    margin: 0 auto;
}
</style>