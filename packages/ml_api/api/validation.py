from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json

class InvalidInputError(Exception):
    """Invalid model input"""

#if any syntax error will be noticed in fields
SYNTAX_ERROR_FIELD_MAP = {}


class CHDDataRequestSchema(Schema):
    male = fields.Integer(allow_none=True)
    age = fields.Integer(allow_none=True)
    currentsmoker = fields.Integer(allow_none=True)
    cigsperday = fields.Integer(allow_none=True)
    prevalenthyp = fields.Integer(allow_none=True)
    diabetes = fields.Integer(allow_none=True)
    sysbp = fields.Integer(allow_none=True)
    diabp = fields.Integer(allow_none=True)
    heartrate = fields.Integer(allow_none=True)
    bmi = fields.Integer(allow_none=True)
    bpmeds = fields.Integer(allow_none=True)
    prevalentstroke = fields.Integer(allow_none=True)
    totchol = fields.Integer(allow_none=True)
    glucose = fields.Integer(allow_none=True)
    education = fields.Integer(allow_none=True)

def _filter_error_rows(errors: dict,
                        validated_input: t.List[dict]
                        ) -> t.List[dict]:
    """Remove input rows with errors"""

    indexes = errors.keys()
    for index in sorted(indexes, reverse=True):
        if not isinstance(index, int):
            pass
        else:
            for key in errors[index].keys():
                if key in validated_input[0].keys():
                    del validated_input[0][key]

    return validated_input


def validate_inputs(input_data):
    """Check model inputs against schema"""
    # many=True to allow passing in a List
    schema = CHDDataRequestSchema(many=True)

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
