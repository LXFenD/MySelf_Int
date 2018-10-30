<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
   import $ from 'jquery'

   $(function () {
    $('#app').css('height',$(window).height()+'px')
  });

export default {
  name: 'App',
  // components:{
  //   BG_nav
  // }

}
</script>

<style>

body{font-size: 15px;font-family: "Helvetica Neue",  Helvetica, Arial, sans-serif;line-height:1.25;
background: #eee!important;
}
*{margin: 0; padding: 0; border: 0;text-decoration:none ;  list-style: none;color: #666;hyphens: auto;
overflow-wrap: break-word;}
p,h1,h2,h3,h4,h5,h6{font-weight: normal;font-style: normal}
input,textarea,select,option {outline: none;}
ul,li {margin: 0;padding: 0;}
p{font-size: 16px;
        font-weight: 300;
        color: #888;}
  a{
    color: #888;
    font-size: 14px;
    text-decoration: none;
  }
</style>
