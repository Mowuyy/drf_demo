from rest_framework.renderers import JSONRenderer as DRF_JSONRenderer


class JSONRender(DRF_JSONRenderer):
    """重写rest_framework框架的JSONRenderer类
       指定响应字符集
    """
    charset = "utf-8"
