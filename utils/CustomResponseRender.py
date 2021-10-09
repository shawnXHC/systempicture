from rest_framework.renderers import JSONRenderer


# 导入控制返回的JSON格式的类
class CustomRenderer(JSONRenderer):
    # 重构render方法
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # 如果是字典的话应该是返回的数据，会包含msg,code,status等字段必须抽离出来
        # print(renderer_context.get('response', None).status_code)
        try:
            msg = data.pop('msg')
            code = data.pop('code')
        except Exception as e:
            code = renderer_context.get('response', None).status_code
            if code>399:
                msg = "request has failed"
            else:
                msg = "request has success"
        ret = {
                'msg': msg,
                'code': code,
                'data': data
            }
        # 返回JSON数据
        return super().render(ret, accepted_media_type, renderer_context)
