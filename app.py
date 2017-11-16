# -*- coding: utf-8 -*-

import falcon
from ann_resource import AnnResource 



api = falcon.API()
api.add_route('/ann', AnnResource())
