import typing

from rest_framework.serializers import ModelSerializer


INT_MAX = 2147483647
MUST_REQUIRED = "该字段是必填项"


def set_attrs_with_value(attrs: typing.Dict, keys: typing.List[str], value: typing.Any):
    """
    set_attrs_with_value: 对应的字段至value
    """
    for key in keys:
        attrs[key] = value
    return attrs


class CreatorOrUpdatorModelSerializer(ModelSerializer):
    """
    CreatorOrUpdatorModelSerializer
    """

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data["creator_id"] = user.id
        validated_data["update_id"] = user.id
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        user = self.context.get('request').user
        validated_data["update_id"] = user.id
        instance = super().update(instance, validated_data)
        return instance
