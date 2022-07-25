#!/bin/bash
curl -X POST http://localhost:5000/api/timeline_post -d \
'name=Star&email=starxie7827@gmail.com&content=Testing random endpoints.'
curl http://localhost:5000/api/timeline_post
