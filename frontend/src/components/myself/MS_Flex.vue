<template>
  <div class="Ms_Flex">
    <ul>
      <li>
        <img src="../../assets/myself/10.jpg" alt="">
        <div class="ms_ab">
          <h3>图片</h3>
          <p>很好看</p>
        </div>
        <div class="ms_se">
          <ul class="ms_ul_s">
            <li>
              <a href=""> <i class="fa fa-link"></i></a>
            </li>
            <li><a href=""> <i class="fa fa-search"></i></a></li>
          </ul>
        </div>
      </li>
      <li><img src="../../assets/myself/11.jpg" alt="">
        <div class="ms_ab">
          <h3>图片</h3>
          <p>很好看</p>
        </div>
        <div class="ms_se">
          <ul class="ms_ul_s">
            <li>
              <a href="javascript:void(0)"> <i class="fa fa-link"></i></a>
            </li>
            <li><a href="javascript:void(0)"><i class="fa fa-search"></i></a></li>
          </ul>
        </div>
      </li>
      <li><img src="../../assets/myself/12.jpg" alt="">
        <div class="ms_ab">
          <h3>图片</h3>
          <p>很好看</p>
        </div>
        <div class="ms_se">
          <ul class="ms_ul_s">
            <li>
              <a href="javascript:void(0)"> <i class="fa fa-link"></i></a>
            </li>
            <li><a href="javascript:void(0)"> <i class="fa fa-search"></i></a></li>
          </ul>
        </div>
      </li>
      <li><img src="../../assets/myself/13.jpg" alt="">
        <div class="ms_ab">
          <h3>图片</h3>
          <p>很好看</p>
        </div>
        <div class="ms_se">
          <ul class="ms_ul_s">
            <li>
              <a href="javascript:void(0)"> <i class="fa fa-link"></i></a>
            </li>
            <li><a href="javascript:void(0)"> <i class="fa fa-search"></i></a></li>
          </ul>
        </div>
      </li>
      <li><img src="../../assets/myself/14.jpg" alt="">
        <div class="ms_ab">
          <h3>图片</h3>
          <p>很好看</p>
        </div>
        <div class="ms_se">
          <ul class="ms_ul_s">
            <li>
              <a href="javascript:void(0)"> <i class="fa fa-link"></i></a>
            </li>
            <li><a href="javascript:void(0)"> <i class="fa fa-search"></i></a></li>
          </ul>
        </div>
      </li>
      <li><img src="../../assets/myself/15.jpg" alt="">
        <div class="ms_ab">
          <h3>图片</h3>
          <p>很好看</p>
        </div>
        <div class="ms_se">
          <ul class="ms_ul_s">
            <li>
              <a href=""> <i class="fa fa-link"></i></a>
            </li>
            <li><a href="javascript:void(0)"> <i class="fa fa-search"></i></a></li>
          </ul>
        </div>
      </li>
      <li><img src="../../assets/myself/16.jpg" alt="">
        <div class="ms_ab">
          <h3>图片</h3>
          <p>很好看</p>
        </div>
        <div class="ms_se">
          <ul class="ms_ul_s">
            <li>
              <a href="javascript:void(0)"> <i class="fa fa-link"></i></a>
            </li>
            <li><a href="javascript:void(0)"> <i class="fa fa-search"></i></a></li>
          </ul>
        </div>
      </li>
      <li><img src="../../assets/myself/17.jpg" alt="">
        <div class="ms_ab">
          <h3>图片</h3>
          <p>很好看</p>
        </div>
        <div class="ms_se">
          <ul class="ms_ul_s">
            <li>
              <a href="javascript:void(0)"> <i class="fa fa-link"></i></a>
            </li>
            <li><a href="javascript:void(0)"> <i class="fa fa-search"></i></a></li>
          </ul>
        </div>
      </li>
    </ul>

  </div>
</template>

<script>
  import $ from 'jquery'
  $(function () {
    var ms_f_c = $('<div class="ms_f_c"></div>');
    var ms_f_c_img = $('<div class="ms_f_c_img"></div>');
    var img = $('<img src="">');
    $('.fa-search').click(function (e) {
      var pp = $(this).parents('.ms_se').parent('li').children('img').attr('src')
      console.log(pp)
      $('.Ms_Flex').prepend(ms_f_c);
      ms_f_c.append(ms_f_c_img);
        $('.ms_f_c').css({
            'position':'absolute',
            'width':'100%',
            'height':'100%',
            'z-index':'99',
            'top':'0',
            'left':'0',
            'background':'rgba(0,0,0,.5)'
    });
      $('.ms_f_c_img').css({
        'width':'20%',
        'height':'40%',
        'margin':'0 auto',
        'background':'#324252',
        'margin-top':'15%'
      })
      ms_f_c_img.append(img)
      $('.ms_f_c_img img').attr('src',pp).css({
        'width':'100%',
        'height':'100%',
      })

    });
    ms_f_c.click(function () {
      ms_f_c_img.remove();
      $(this).remove();
    })
  });
  export default {
    name: "MS_Flex",
    created(){

    }
  }
</script>

<style scoped>
  .Ms_Flex {
    width: 100%;
    position: relative;
  }

  .Ms_Flex ul {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
  }

  .Ms_Flex ul li {
    flex-basis: 24%;

    flex-grow: 1;
    width: 24%;
    height: 500px;
    overflow: hidden;
    position: relative;
  }

  .Ms_Flex ul li img {
    width: 100%;
    height: 100%;
  }

  .Ms_Flex ul li:hover img {
    transform: scale(1.1);
    transition: all .5s ease-out .1s;
  }

  .Ms_Flex ul li:hover .ms_ul_s {
    display: block;
  }

  .Ms_Flex ul li:hover .ms_ab {
    display: none;
  }

  .ms_ab {
    width: 100%;
    height: 100px;
    color: white;
    position: absolute;
    top: calc(50% - 50px);
    text-align: center;
    /*display: none;*/
  }

  .ms_ab p {
    color: white;
    font-size: 16px;
  }

  .ms_se {
    width: 100%;
    height: 100px;
    text-align: center;
    line-height: 100px;
    position: absolute;
    top: calc(50% - 50px);
  }

  .ms_se ul {
    padding: 0;
    height: 100%;
    list-style-type: none;
    display: none;

  }

  .ms_se ul li {
    float: left;
    width: 50%;
    height: 100%;
    font-size: 30px;
    text-align: center;
    line-height: 100px;
  }

  .ms_se ul li a i {
    color: sandybrown;
  }

  .ms_se ul li a {
    display: inline-block;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: white;
    line-height: 50px;
    text-align: center;
  }

  .ms_se ul li:nth-of-type(1) {
    text-align: right;
    padding-right: 15px;
  }

  .ms_se ul li:nth-of-type(2) {
    text-align: left;
    padding-left: 15px;
  }

</style>
