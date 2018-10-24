<template>
  <div class="ms_banner_img">
    <div class="left">
      <ul class="left-ul">
        <li class="left-li"><img src="../../assets/myself/2.jpg" alt=""></li>
        <li class="left-li"><img src="../../assets/myself/3.jpg" alt=""></li>
        <li class="left-li"><img src="../../assets/myself/4.jpg" alt=""></li>
      </ul>
    </div>
    <div class="right">
      <div class="right_con">
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
         <div class="right-boot">
              <div class="boot-ji" id="boot_left">
                <i class="fa fa-arrow-left"></i>
              </div>
                <div  class="boot-ji "  id="boot_right">
                <i class="fa fa-arrow-right"></i>
              </div>
      </div>
      </div>

    </div>
  </div>
</template>

<script>
  import $ from "jquery"

  class Banner {
    constructor() {
      this.left_ul = $(".left-ul");
      this.li_lists = this.left_ul.children('li');
      this.list_length = this.li_lists.length;
      this.index = 0;
      this.yd = 100;
      this.boot_left = $("#boot_left");
      this.boot_right = $("#boot_right")
    }

    init_Banner = () => {
      let first_li = this.li_lists.eq(0).clone();
      let last_li = this.li_lists.eq(this.list_length - 1).clone();
      this.left_ul.append(first_li);
      this.left_ul.prepend(last_li);
    };

    Banner_Animal = () => {
      var self = this;

        self.left_ul.animate({'left': '-' + self.index * self.yd + '%'}, 1000);

    };

    Banner_Loop = () =>{
      var self = this;
      setInterval(function () {
         if (self.index > self.list_length) {
          self.left_ul.css('left', '-100%');
          self.index = 0;
        }else {
          self.index++;
        }
        console.log(self.index);
        self.Banner_Animal()
      },6000)
    };


    Banner_Click = ()=>{
      var self = this;
      self.boot_left.click(function () {
          if (self.index > self.list_length) {
          self.left_ul.css('left', '-100%');
          self.index = 0;
          }else {
            self.index++;
          }
          console.log(self.index)
          self.Banner_Animal()
      });

      self.boot_right.click(function () {
        if (self.index === 0 ) {
          self.left_ul.css('left', '-'+self.list_length*self.yd+'%');
          self.index = self.list_length;
          }else {
            self.index--;
          }
          self.Banner_Animal()
      });
    }
  }

  export default {
    name: "MS_Banner_Img",
  data(){
      return{
        banner:null
      }
  },
    mounted() {
        this.banner = new Banner();
        this.banner.init_Banner();
        this.banner.Banner_Loop();
        // this.banner.Banner_Animal();
        this.banner.Banner_Click();
    },
  }
</script>

<style scoped>


  .right-boot{
    width: 100%;
    margin-top: 120px;
  }
  .right-boot .boot-ji{
    display: inline-block;
    padding: 6px 12px;
    margin-bottom: 0;
    font-size: 35px;
    font-weight: 400;
    line-height: 1.42857143;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    -ms-touch-action: manipulation;
    touch-action: manipulation;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-image: none;
    border: 1px solid transparent;
    border-radius: 4px;
  }
  .ms_banner_img {
    width: 100%;
    height: 800px;
  }

  .ms_banner_img:after {
    display: block;
    clear: both;
    content: "";
  }

  .left {
    width: 50%;
    height: 100%;
    background: #eeeeee;
    float: left;
    overflow: hidden;
    position: relative;
  }

  .left ul {
    padding: 0;
    list-style-type: none;
    width: 1000%;
    height: 100%;
    position: absolute;
  }

  .left ul li {
    float: left;
    width: 10%;
    height: 100%;
  }

  .left ul li img {
    width: 100%;
    height: 100%;
  }

  .right {
    width: 50%;
    height: 100%;
    /*background: #123213;*/
    float: right;
  }
   .right  .right_con{
     width: 100%;
     height: 100%;
     padding: 100px 60px;
   }
  .right  .right_con .content{
    width: 100%;
    margin-bottom: 30px;
  }

  .right  .right_con .content h1{
    font-size: 67px;
    font-weight: 700;
    color: #2c2c2c;
    text-transform: uppercase;
    letter-spacing: 2px;
    line-height: 70px;
  }
  .san-span{
    width: 100%;
    text-align: left;
  }
  .san-span span{
    border-left: none;
    border-bottom: 30px solid transparent;
    border-top: 30px solid #ff9e22;
    border-right: 30px solid transparent;
  }

  .p-content{
       font-size: 16px;
        font-weight: 300;
        line-height: 24px;
        color: #888;
  }
  .mmm{
    margin-top: 20px;
  }
</style>
