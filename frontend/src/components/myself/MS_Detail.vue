<template>
  <div class="ms_detail">
    <div class="detail_left">
      <div class="d_l_l">
        <div class="content">
          <h1>
            We Are <br>Creative <br>Team
          </h1>
        </div>
        <div class="san-span">
          <span></span>
        </div>
        <p class="p-content mmm">Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          Aliquam viverra convallis auctor. Sed accumsan libero quis mi commodo et suscipit enim lacinia.
          Morbi rutrum vulputate est sed faucibus.consectetur adipiscing elit.
          Aliquam viverra convallis auctor.
          Sed accumsan libero quis mi commodo et suscipit enim lacinia.</p>
        <p class="p-content mmm">Dapibus neque. Mauris justo massa, semper sed tempor at, blandit sit amet eros.
          sMaecenas placerat ac urna in</p>
      </div>
      <div class="d_l_r">

      </div>
    </div>
    <div class="detail_right">
      <div class="d_r_t">
        <h1>Hubert</h1>
      </div>
      <p class="p-content">Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Vos autem cum perspicuis dubia debeatis illustrare.</p>
      <div class="d_r_list">
        <ul >
          <li>
            <p>Adobe Dreamweaver:</p>
            <div class="progress">
              <div class="progress-bar"><span>70%</span></div>
            </div>
          </li>
          <li><p>Adobe Dreamweaver:</p>
            <div class="progress">
              <div class="progress-bar"><span>70%</span></div>
            </div>
          </li>
          <li><p>Adobe Dreamweaver:</p>
            <div class="progress">
              <div class="progress-bar"><span>70%</span></div>
            </div>
          </li>
          <li><p>Adobe Dreamweaver:</p>
            <div class="progress">
              <div class="progress-bar"><span>70%</span></div>
            </div>
          </li>
          <li><p>Adobe Dreamweaver:</p>
            <div class="progress">
              <div class="progress-bar"><span>70%</span></div>
            </div>
          </li>
        </ul>
      </div>
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
</template>

<script>
  export default {
    name: "MS_Detail",
    created(){

    }
  }
</script>

<style scoped>
  .ms_detail {
    width: 100%;
    height: 900px;
  }

  .ms_detail .detail_left {
    width: 65%;
    height: 100%;
    float: left;
    background: white;
    overflow: hidden;
  }

  .ms_detail .detail_left .d_l_l {
    width: 50%;
    height: 100%;
    text-align: right;
    padding: 60px 40px;
    float: left;
  }

  .ms_detail .detail_left .d_l_r {
    width: 50%;
    height: 100%;
    background: url("../../assets/myself/business.png") no-repeat;
    background-size: 97% 100%;
    background-position: 0 0;
    overflow: hidden;
    float: right;
  }

  .ms_detail .detail_right {
    width: 35%;
    height: 100%;
    float: left;
    background: #2c2c2c;
    padding: 60px 100px;
  }

  .content {

    width: 100%;
    margin-bottom: 30px;
  }

  .content h1 {
    font-size: 67px;
    font-weight: 700;
    color: #2c2c2c;
    text-transform: uppercase;
    letter-spacing: 2px;
    line-height: 70px;
  }

  .san-span {
    width: 100%;
    text-align: right;
  }

  .san-span span {
    border-left: 30px solid transparent;
    border-bottom: 30px solid transparent;
    border-top: 30px solid #ff9e22;
    border-right: none;
  }

  .p-content {
    font-size: 16px;
    font-weight: 300;
    line-height: 24px;
    color: #888;
  }

  .mmm {
    margin-top: 20px;
  }

  .d_r_t h1 {
    margin-top: 50px;
    font-size: 60px;
    font-weight: 800;
    color: #ff9e22;
    text-transform: uppercase;
    font-family: 'Gloria Hallelujah', sans-serif;
    letter-spacing: 3px;

  }

  .p-content {
    font-size: 16px;
    font-weight: 300;
    line-height: 24px;
    color: #888;
    margin-top: 40px;
    margin-bottom: 40px;
  }

  .progress {
    width: 100%;
    height: 15px;
    background: black;

  }

  .progress-bar {
    width: 75%;
    height: 100%;
    background: crimson;
    line-height: 15px;

  }

  .progress-bar span {
    color: white;
  }
  .detail_right>ul {
    padding: 0;
    list-style-type: none;
    width: 100%;
    text-align: center;
  }
  .detail_right>ul>li{
    display: inline-block;
    margin: 10px;
    font-size: 30px;
    text-rendering: auto;
    width: 50px;
    height: 50px;
    color: white;
    border-radius: 50%;
    border: 1px solid #ccc;
    vertical-align: center;
    line-height: 50px;
    margin-top: 105px;
  }
 .detail_right>ul>li>a>i{
   margin-left: -1px;
   color: white;
 }

</style>
