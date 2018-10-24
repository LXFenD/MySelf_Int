<template>
    <div class="content">
        <div class="left-content">
          <Blog_Write_Left></Blog_Write_Left>
        </div>
        <div class="right-content">
          <Blog_Write_Right></Blog_Write_Right>
        </div>
    </div>
</template>

<script>
  import Blog_Write_Left from '../../blog/blog-write/blog-write-left'
  import Blog_Write_Right from '../../blog/blog-write/blog-write-right'

    export default {
        name: "Content",
      components:{
          Blog_Write_Left,
          Blog_Write_Right
      }
    }
</script>

<style scoped>

  @media screen and (max-width: 375px) {
    .content {
      width: 300px;
      background: gainsboro;
      margin: 0 auto;
      color: antiquewhite;
    }
  }

  @media screen and (max-width: 750px) and (min-width: 375px) {
    .content {
      width: 600px;
      background: gainsboro;
      margin: 0 auto;
      color: antiquewhite;
    }
  }
  @media screen and (max-width: 1280px) and (min-width: 750px ) {
    .content {
      width: 800px;
      background: gainsboro;
      margin: 0 auto;
      color: antiquewhite;
    }
  }

  @media screen and (min-width: 1280px) {
    .content {
      width: 1280px;
      background: rgba(255, 255, 255, 0.4);
      margin: 0 auto;
      color: antiquewhite;
    }
  }

  .content {
    border-radius: 15px;
    box-sizing: border-box;
    overflow: hidden;
    padding: 10px;
    margin-top: 70px;
  }
.content:after{
  content: '';
  display: block;
  visibility: hidden;
  height: 0;
  clear: both;
}
  .content .left-content{
    width: 15%;
    float: left;

  }
  .content .right-content{
    width: 84%;
    float: right;
  }



</style>
