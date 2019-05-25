- 问题描述：You called this URL via PUT, but the URL doesn't end in a slash and you have APPEND_SLASH set. Django can't redirect to the slash URL while maintaining PUT data. Change your form to point to 127.0.0.1:8000/books/8/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.  
    - 原因：域名未以 / 结尾，Django无法重定向至以 / 结尾的域名  
    - 解决：在域名最后加上 /

- 问题描述：ie浏览器获取json数据，出现中文乱码
    - 原因：响应中未设置字符集编码格式
    - 解决：重写JSONRenderer类，设置charset = 'utf-8'

- 问题描述：编写APIView详情页时报错，booktest.models.DoesNotExist: BookInfo matching query does not exist
    - 原因：根据pk查询模型类时，未做异常处理，导致rest_framework框架异常渲染时报错
    - 解决：跟模型类交互时异常处理