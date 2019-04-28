- 问题描述：You called this URL via PUT, but the URL doesn't end in a slash and you have APPEND_SLASH set. Django can't redirect to the slash URL while maintaining PUT data. Change your form to point to 127.0.0.1:8000/books/8/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.  
    - 原因：域名未以 / 结尾，Django无法重定向至以 / 结尾的域名  
    - 解决：在域名最后加上 /



