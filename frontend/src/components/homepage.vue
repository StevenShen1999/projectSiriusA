<template>
    <div id="homepage" class="container">
        <!--<p v-for="blog in blogs" v-bind:key="blog">{{ blog }}</p>-->
        <div class="card" v-for="blog in searchBlogs" v-bind:key="blog.id">
            <div class="card-header">
                <router-link v-bind:to="'/blog/' + blog.id" style="text-decoration: none; color: black;">{{ blog.title }}</router-link>
            </div>
            <div class="card-body">
                <p>{{ blog.content }}</p>
                <p class="card-text"><small class="text-muted">{{ blog.createdOn }}</small></p>
            </div>
        </div>
    </div>
</template>

<script>
import { bus } from '../main';
export default {
    data(){
        return {
            blogs: [],
            search: ''
        }
    },
    created(){
        this.fetchBlogs();
        this.timer = setInterval(this.fetchBlogs, 5000);
        bus.$on('searchDefined', (data) => {
            this.search = data;
        });
    },
    methods: {
        fetchBlogs() {
            this.$http.get('http://localhost:5000/blog/all').then((data) => {
                this.blogs = data.body;
            });
        }
    },
    computed: {
        searchBlogs: function(){
            return this.blogs.filter((blog) => {
                return blog.title.match(this.search);
            })
        }
    }
}
</script>

<style>
.card {
    margin: 10px;
}
</style>