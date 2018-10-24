<template>
    <div class="ms_banner">
          <div class="banner-left">
            <div class="left-content padd_content">
              <div class="con-top">
                  <h1>
                      Right Picture Slide
                  </h1>
                <span></span>
              </div>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Vos autem cum perspicuis dubia debeatis illustrare,
                dubiis perspicua conamini tollere.
                Atque his de rebus et splendida est eorum et oratio.</p>
              <p>
                Sed eum qui audiebant, quoad poterant, defendebant
                sententiam suam. Hoc est non dividere, sed frangere.
                Facile est hoc.
              </p>
            </div>

          </div>
          <div class="banner-cont">
            <div class="content-l">
              <div class="title">
                  <h3>Sawie</h3>
              </div>
              <p class="p-content">orem ipsum dolor sit amet, consectetur adipiscing elit.
                Donec lobortis dignissim nunc ut cursus. Ut dapibus a gravida pretium.
                Curabitur ultricies viverra.
                Morbi vulputate quis metus dignissim,
                vitae scelerisque felis ultricies vitae.</p>
              <p class="p-content"> consequat metus vitae, dapibus neque.
                Mauris justo massa, semper sed tempor at,
                blandit sit amet eros.
                Maecenas placerat ac urna in.</p>
              <ul>
                <li><a href="">
                  <i class="fa fa-facebook"></i>
                </a></li>
                <li><a href=""><i class="fa fa-github"></i></a></li>
                <li><a href=""><i class="fa fa-google-plus"></i></a></li>
                <li><a href=""><i class="fa fa-instagram"></i></a></li>
              </ul>
            </div>
          </div>
          <div class="banner-right">
            <!--<img src="../../../assets/1.jpg" alt="">-->
          </div>
    </div>
</template>

<script>

    export default {
        name: "MS_Banner"
    }
</script>

<style scoped>

  @media screen and  (max-width: 1280px){
    .banner-right{
      display: none;
    }
    .banner-cont{
      width: 50%;
    }
    .banner-left{
      width: 50%;
    }
  }
  .ms_banner{
    width: 100%;
    overflow: hidden;
  }
  .ms_banner:after{
    display: block;
    visibility: hidden;
    content: "";
    height: 0;
    clear: both;
  }
  .banner-left{
    width: 35%;
    height: 100%;
    background: #fff;
    float: left;

     }

  .banner-cont{
    width: 25%;
    height: 100%;
    background: black;
    float: left;
    overflow: hidden;
     }
  .banner-right{
    width: 40%;
    height: 853px;
    /*background: brown;*/
    float: right;
    background: url("../../assets/myself/1.jpg") no-repeat;
    background-size: cover;
    background-position:center center;

     }

  .con-top{
    width: 100%;
  }
  .left-content{
    width: 100%;
    height: 100%;
    padding: 100px 99px;
    text-align: right;
  }
  .padd_content{
    padding: 100px 99px;
  }
  .left-content h1{
    font-size: 50px;
    font-weight: 700;
    text-transform: uppercase;
    color: #333;
    margin-bottom: 30px;
  }
  .left-content span{
    border-left: 30px solid transparent;
    border-bottom: 30px solid transparent;
    border-top: 30px solid #ff9e22;
    border-right: none;
  }

  .left-content p {
        margin-bottom: 20px;
        /*color: #ccc;*/
        font-size: 16px;
        font-weight: 300;
        line-height: 24px;
        color: #888;
  }
  .p-content{
       font-size: 16px;
        font-weight: 300;
        line-height: 24px;
        color: #888;
  }
  .content-l{
    background: #2c2c2c;
    padding: 70px 49px;
    text-align: center;

  }
  .content-l .title {
    margin-bottom: 50px;
  }
  .content-l .title h3{
    font-size: 60px;
    font-weight: 800;
    color: #ff9e22;
    text-transform: uppercase;
    font-family: 'Gloria Hallelujah', sans-serif;
    letter-spacing: 3px;

  }
  .content-l p {

    margin-bottom: 10px;
    font-size: 17px;
    padding: 20px;
    box-sizing: border-box;
  }
  .content-l  ul {
    padding: 0;
    list-style-type: none;
    width: 100%;
    text-align: center;
  }
  .content-l  ul li{
    display: inline-block;
    margin: 10px;
    font-size: inherit;
    text-rendering: auto;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 1px solid #ccc;
    vertical-align: center;
    line-height: 57px;
    margin-top: 105px;
  }
 .content-l  ul li i{
   margin-left: -1px;
   font-size: 25px;
   color: white;
 }
</style>
