import axios from 'axios'
import {Toast} from 'vant'



var instance = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  timeout: 6000,
});
instance.defaults.headers.post['Content_Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
/**
 * 提示信息
 * @param msg
 */
const tip = msg => {
  Toast({
    message: msg,
    duration: 1000,
    forbidClick: true
  })
};
/**
 * 错误信息提示
 * @param status
 * @param other
 */
const errorhander = (status, other) => {
  switch (status) {
    case 400:
      tip(other.data.message);
      break;
    case 500:
      tip(other.data.message);
      break;
    case 401:
      tip(other.data.message);
      break;
  }
};


/**
 * 响应拦截器
 */
instance.interceptors.response.use(
  res => res.status === 200 ? Promise.resolve(res) : Promise.reject(res),
  err => {
    const {Response} = err;
    if (Response) {
      errorhander(Response.status);
      return Promise.reject(Response)
    } else {
      console.log("sad");
      Toast({
        message:'失败',
        duration:1000,
        forbidClick:true
      })

    }
  }
);

export default instance;



