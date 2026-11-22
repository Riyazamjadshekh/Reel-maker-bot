# reel-maker-bot - Claude se Auto Voice Over + Caption Banane Wala App
import os
import anthropic
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Render me CLAUDE_KEY naam se Key dalni hai
client = anthropic.Anthropic(api_key=os.environ.get("CLAUDE_KEY"))

HTML = """
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Reel Maker Bot</title>
<style>
body{font-family:Arial;padding:20px;background:#111;color:white}
input,button{width:100%;padding:15px;margin:10px 0;border-radius:10px;border:none;font-size:16px;box-sizing:border-box}
input{background:#222;color:white}
button{background:#FF0066;color:white;font-weight:bold}
.box{background:#222;padding:15px;border-radius:10px;white-space:pre-wrap;margin-top:15px;line-height:1.6}
h2{color:#FF0066}
.small{color:#aaa;font-size:13px}
</style>
</head>
<body>
<h2>🔥 Reel Maker Bot - Claude Auto</h2>
<p class="small">Topic dalo, Claude apne aap Voice Over + Caption
