# reel-maker-bot - FREE - Gemini se Auto Voice Over + Caption
import os
import requests
from flask import Flask, request, render_template_string

app = Flask(__name__)

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
<h2>🔥 Reel Maker Bot - FREE Auto</h2>
<p class="small">Topic dalo, AI apne aap Voice Over + Caption + Description + Hashtag bana dega!</p>
<form method="POST">
<input name="topic" placeholder="Topic likho - jaise: 3 GitHub Repo" required>
<button type="submit">REEL BANAO 🚀</button>
</form>
{% if result %}
<h3>✅ Tumhari Reel Tayyar Hai!</h3>
<div class="box" id="resultBox">{{ result }}</div>
<button onclick="copyText()">COPY KARO 📋</button>
<script>
function copyText(){
  var t = document.getElementById('resultBox').innerText;
  navigator.clipboard.writeText(t);
  alert('Copy Ho Gaya! Ab CapCut me Paste Karo!');
}
</script>
{% endif %}
</body>
</html>
"""

PROMPT = """
You are a Professional Instagram Reels Creator.
Topic: {topic}

Give output in this EXACT format, in Hindi + English mix, simple language:

1. HOOK - 3 Options, 1 line each, very catchy

2. VOICE OVER SCRIPT - Ready to paste in CapCut Text to Speech
Format:
0-2s: Hook line
2-8s: Point 1
8-14s: Point 2
14-20s: Point 3
20-27s: Best kaunsa hai + reason
27-30s: CTA - Follow Karo + Comment Me Likho

3. ON-SCREEN TEXT - For each slide, short text

4. CAPTION - Ready to paste for Instagram, with emoji + CTA

5. DESCRIPTION - For Instagram + YouTube

6. HASHTAGS - 15 hashtags in one line

7. SONG - 2 trending song suggestions + Volume 15% tip

Keep it energetic, simple, 12 year old can understand.
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        topic = request.form.get("topic")
        api_key = os.environ.get("GEMINI_KEY")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        data = {"contents": [{"parts": [{"text": PROMPT.format(topic=topic)}]}]}
        r = requests.post(url, json=data)
        try:
            result = r.json()["candidates"][0]["content"]["parts"][0]["text"]
        except:
            result = "Error Aa Gaya! Key Sahi Se Dali Hai? Render me GEMINI_KEY Check Karo. Error: " + str(r.text[:500])
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
