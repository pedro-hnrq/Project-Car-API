from drf_spectacular.openapi import AutoSchema

class CustomAutoSchema(AutoSchema):
    def get_tags(self, path, method):
        if 'token' in path:
            return ['Auth']
        if 'brands' in path:
            return ['Brands']
        if 'cars' in path:
            return ['Cars']
        return super().get_tags(path, method)
