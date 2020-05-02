from marshmallow import Schema, fields, validate, post_load
import random
from datetime import datetime
import pytz
from models.blogs import Blogs
from uuid import uuid4

class BlogCreationSchema(Schema):
    title = fields.String(required=True, allow_none=False)
    content = fields.String(required=True, allow_none=False)

    @post_load
    def makeNote(self, data, **kwargs):
        return Blogs(id=str(uuid4().hex), title=data['title'],
            content=data['content'], createdon=datetime.utcnow())

class BlogPollingSchema(Schema):
    fromTime = fields.AwareDateTime(required=True, allow_none=False)
    toTime = fields.AwareDateTime(required=True, allow_none=False)