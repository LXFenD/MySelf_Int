<template>
    <div class="ms_content">
          <div class="ms_con_left">
          <h1 class="ms_h1_title">Your Favorite Source of Free sBootstrap Themes</h1>
          <p>Start Bootstrap can help you build better websites using the Bootstrap CSS framework!
            <br>
            <br>
              Just download your template and start going, no strings attached!</p>
            <a href="" class="btn btn-primary btn-hader">FIND MORE INFO</a>
          </div>
    </div>
</template>

<script>
    export default {
        name: "MS_Top"
    }
</script>

<style scoped>
 .ms_content{
    width: 100%;
    background: rgba(0,0,0,.001);
    margin: 0 auto;
    height: 850px;
    padding: 200px 150px 0 150px;
    background-image: url("../../assets/myself/showcase_bg.jpg");
    background-repeat: no-repeat;
    background-position: 50% top;
    background-size: cover;
    margin-top: 90px;
  }
  .btn-hader{
    border: 0;
    background: darkorange;
    padding: 10px 20px;
    border-radius: 0;
    color: black;
    font-weight: 300;
  }
  .btn-hader:hover{
    background: black;
    color: white;
  }
  .ms_con_left{
    width: 40%;
    text-align: right;
  }
   .ms_content .ms_con_left .ms_h1_title{
    width: 100%;
    text-align: right;
    font-size: 40px;
    font-weight: 700;
    text-transform: uppercase;
    color: #333;
  }

   .ms_content .ms_con_left p{
    font-weight: 300;
    font-size: 17px;
    text-align: right;
    padding: 0 0 0 20px;
    margin-bottom: 20px;
  }
</style>
