<template>
    <div id="navbar">
        <nav class="navbar navbar-expand-md navbar-light">
        <a class="navbar-brand">
            <router-link to="/about">Shen</router-link>
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item" v-bind:class="{ active:active }">
                    <a class="nav-link">
                        <router-link to="/" exact class="routerLinks">Home</router-link>
                    </a>
                </li>
                <li class="nav-item" v-bind:class="{ active:active }">
                    <a class="nav-link">
                        <router-link to="/add" exact class="routerLinks">Add Blog</router-link>
                    </a>
                </li>
            </ul>
            <form class="form-inline my-2 my-lg-0">
                <input v-model="searchTerm" class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                <button v-on:click.prevent="submitSearch" class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
            </form>
        </div>
        </nav>
    </div>
</template>

<script>
import { bus } from '../main';
export default {
    data(){
        return {
            searchTerm: '',
            active: true
        };
    }, 
    methods: {
        submitSearch(){
            bus.$emit('searchDefined', this.searchTerm);
            // TODO: Fix search not working if we are not on the main page
            //this.$router.push({path: '/'});
        }
    }
}
</script>

<style>
#navbar {
    background: lightgrey;
}

.navbar {
    margin: 0 10%;
}

.router-link-active {
    text-decoration: none;
    color: black;
}

.router-link-active:hover {
    text-decoration: none;
    color: black;
}

.routerLinks{
    text-decoration: none;
    color: black;
}

.routerLinks:hover {
    text-decoration: none;
    color: black;
}

</style>