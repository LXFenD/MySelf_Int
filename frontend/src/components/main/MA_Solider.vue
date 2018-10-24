<template>
    <div class="slider" :style="{right:right}">
        <div class="slider-con" >
            <div class="slider-kuai" @click="show" :style="{left:lll}">
            </div>
          <div class="top">
            列表操作
          </div>
          <ul>
            <li>
                <span class="glyphicon glyphicon-text-width"></span> <router-link to="/bw/">撰写博客</router-link>
            </li>
          </ul>
        </div>
    </div>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "MA_Solider",
      data(){
          return{
            is_show:false,
            right:'-20%',
            lll:'-48px'
          }
      },
      mounted(){
          $(function () {
            var body = $('html,body')
          })
      },
      methods:{
          show(){
            if(this.is_show)
            {
              this.right = '-20%';
              this.is_show = false;
              this.lll='-48px'
            }else{
              this.right = '0%';
              this.is_show = true;
              this.lll='0px'
            }
          }
      }

    }
</script>

<style scoped>

    .slider{
      position: fixed;
      width: 20%;
      height: 600px;
      top: 100px;
      right: -20%;
      z-index: 88;
    }
  .slider-con{
    width: 100%;
    height: 100%;
    background:rgba(0,0,0,.5);
    position: relative;
  }
  .slider-kuai{
    position: absolute;
    width: 48px;
    height: 48px;
    background: url('../../assets/jjj.png');
    top:0;
    left: -48px;
  }
  .top{
    width: 100%;
    height: 48px;
    margin-right: 48px;
    line-height: 48px;
    text-align: center;
    font-size: 16px;
    color: white;
    border-bottom: 1px solid #fff;
  }
  .slider-con ul{
    margin-top: 10px;
    width: 100%;
    list-style-type: none;
  }
  .slider-con ul li{
    height: 48px;
    line-height: 48px;
    text-align: center;
    margin-bottom: 10px;
     border-bottom: 1px solid #000;
    color: white;
    cursor: pointer;
  }
  .slider-con ul li span{
    color: white;
  }
</style>
