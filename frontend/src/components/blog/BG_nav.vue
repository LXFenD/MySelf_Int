<template>
    <div class="nav">
        <div class="nav-bar">
            <div class="wrap-l">
              <div class="wrap-logo">
                <a href="" class="logo">

                </a>
              </div>
            </div>
            <div class="wrap-add">
                <div class="wrap-a-l">
                  <div class="wal-t">
                      <div class="weather">
                        <span></span>
                        <em>+8℃</em>
                      </div>
                  </div>
                  <div class="drop-b">
                    <em>London</em>
                    <div class="show-list">
                      <ul>
                        <li class="active-l">London</li>
                        <li>China</li>
                        <li>Medaia</li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="wrap-a-r">
                  <p>Central Bank Rate</p>
                  <p>
                    <span class="ss-l">
                      $32.32
                    </span>
                    <span class="ss-ll">
                        €28.23
                    </span>
                  </p>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    export default {
        name: "BG_nav"
    }
</script>

<style scoped>
      .nav{
        width: 100%;
        height: 70px;
        background: #303d4a;

      }
  .nav .nav-bar{
    width: 75%;
    height: 100%;
    margin: 0 auto;
  }

  .wrap-l{
    width: 20%;
    height: 78%;
    float: left;
  }
  .wrap-logo{
      width: 100%;
    height: 100%;
     padding-top: 18px;
  }
  .wrap-logo .logo{
    width: 80%;
    height: 75%;
    background-image: url("../../assets/BLOG/png-sprite/96dpi/sprite.png");
    background-repeat: no-repeat;
    background-position: 0 0 ;
    display: block;

  }
  .wrap-add{
    width: 30%;
    height: 100%;
    float: right;
  }
  .wrap-add::after{
    content: "";
    visibility: hidden;
    display: block;
    height: 0;
    clear: both;
  }
  .wrap-add .wrap-a-l{
    width: 48%;
    height: 100%;
    float: left;
  }
  .wrap-add .wrap-a-l .wal-t{
        width: 100%;
        height: 50%;

  }
  .wrap-add .wrap-a-l .wal-t .weather{
    width: 100%;
    text-align: center;
    height: 50%;
    padding-top: 10%;
  }
.wrap-add .wrap-a-l .wal-t .weather>em{
  color: white;
  font-size: 14px;
}
.wrap-add .wrap-a-l .drop-b{
  width: 100%;
  height: 50%;
  text-align: center;
  vertical-align: center;
}
.wrap-add .wrap-a-l .drop-b>em{
  color: white;
  font-size: 16px;
  position: relative;

}
.ss-l,.ss-ll{
  position: relative;
  font-size: 16px;
}
.ss-l{
  margin-left: -10px;
}
.ss-ll{
  margin-left: 13px;
}


.wrap-add .wrap-a-l .drop-b>em:before,.ss-l:before,.ss-ll:before{
  position: absolute;
  content: "";
  top: 20%;
  right: -15px;
  width: 9px;
  height: 9px;
  border-width: 2px;
  border-style: solid;
  border-color: transparent;
  /*border-top-color: transparent;*/
  transform: rotate(-45deg);
}

.ss-l:before,.ss-ll:before{
  right: -10px;
  width: 7px;
  height: 7px;
  margin: 2px;
}

.ss-l:before{
   border-left-color: crimson;
  border-bottom-color: crimson;
}

.ss-ll:before{
  transform: rotate(135deg);
  margin-top: 5px;
  right: -14px;
   border-left-color: darkolivegreen;
  border-bottom-color: darkolivegreen;
}
.wrap-add .wrap-a-l .drop-b>em:before{
  border-left-color: white;
  border-bottom-color: white;
}
.wrap-add .wrap-a-l .drop-b .show-list{
  width: 100%;
  text-align: center;
  margin-top: 15px;
   border-bottom: 1px solid #ccc;
  display: none;
  z-index: 999;
}
.wrap-add .wrap-a-l .drop-b .show-list>ul{
  list-style-type: none;
  padding: 0;
  z-index: 999;

}
.wrap-add .wrap-a-l .drop-b .show-list>ul>li{
  width: 100%;
  height: 40px;
  line-height: 40px;
  border-bottom: 1px solid #ccc;
  background: white;
  color: black;
  font-size: 15px;
}
.wrap-add .wrap-a-l:hover{
  background: #364452;
}
.wrap-add .wrap-a-l:hover .show-list{
  display: block;
}

.active-l{
   background: #3b6998!important;
   border-bottom: 1px solid #3b6998;
  color: white!important;
}

  .wrap-add .wrap-a-r{
    width: 48%;
    height: 100%;
    float: right;
        box-sizing: border-box;
  }
  .wrap-add .wrap-a-r>p{
    width: 100%;
    height: 50%;
    margin: 0;
    text-align: center;
    color: white;
  }
   .wrap-add .wrap-a-r>p:nth-of-type(1){
      padding-top: 15px;
   }
  .wrap-add .wrap-a-r>p>span{
    color: white;
  }
</style>
