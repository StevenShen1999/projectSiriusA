from namespaces.blog import api
from flask_restplus import fields

blogCreationDetails = api.model("For creating a blog post",
    {
        "title": fields.String(required=True, example="First Blog HURRA"),
        "content": fields.String(required=True, example="Dont know what i will write")
    }
)