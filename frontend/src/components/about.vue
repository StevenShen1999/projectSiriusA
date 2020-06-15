<template>
    <div id="aboutMe">
        <div class="container-md">
            <h1>Hello there</h1>
            <p>{{ about }}</p>
            <p><a v-bind:href="link">{{link}}</a></p>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            about: "Hello, this website was created as the very first frontend project I've tried. I will keep on updating this as long as I am still learning more with regards to Vue.",
            link: "https://github.com/StevenShen1999/projectSiriusA"
        }
    }
}
</script>

<style>
#aboutMe{
    width: 80%;
    margin: 0 auto;
}
</style>