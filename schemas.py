from marshmallow import Schema, validate, fields


class CurrentSchema(Schema):
    id = fields.Integer(dump_only=True)
    currency = fields.String(validate=[
        validate.Length(max=3)])
    price = fields.String(validate=[
        validate.Length(max=20)])
    date = fields.DateTime()
