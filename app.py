from flask import Flask, render_template_string

app = Flask(__name__)

html = """

<!DOCTYPE html>
<html>
<head>
<title>For My Princess</title>

<style>

body{
margin:0;
height:100vh;
background:linear-gradient(135deg,#ff4d6d,#ff758f,#ff8fa3);
display:flex;
justify-content:center;
align-items:center;
flex-direction:column;
font-family:Arial;
overflow:hidden;
color:white;
}

h1{
font-size:50px;
margin-bottom:40px;
text-shadow:0 0 20px rgba(0,0,0,0.3);
}

/* floating hearts */

.bg-hearts span{
position:absolute;
color:white;
font-size:20px;
animation:float 8s linear infinite;
opacity:0.6;
}

@keyframes float{
0%{transform:translateY(100vh)}
100%{transform:translateY(-10vh)}
}

/* heart container */

.heart-container{
position:relative;
width:400px;
height:350px;
animation:rotate 12s linear infinite;
}

@keyframes rotate{
100%{transform:rotate(360deg)}
}

/* sorry text */

.word{
position:absolute;
font-size:18px;
font-weight:bold;
color:white;
text-shadow:0 0 10px rgba(0,0,0,0.4);
}

</style>

</head>

<body>

<h1>For My Princess ❤️</h1>

<div class="heart-container">

<span class="word" style="left:190px;top:40px;">SORRY</span>
<span class="word" style="left:240px;top:60px;">SORRY</span>
<span class="word" style="left:280px;top:100px;">SORRY</span>
<span class="word" style="left:300px;top:150px;">SORRY</span>
<span class="word" style="left:280px;top:200px;">SORRY</span>
<span class="word" style="left:240px;top:240px;">SORRY</span>
<span class="word" style="left:200px;top:270px;">SORRY</span>

<span class="word" style="left:150px;top:240px;">SORRY</span>
<span class="word" style="left:110px;top:200px;">SORRY</span>
<span class="word" style="left:90px;top:150px;">SORRY</span>
<span class="word" style="left:110px;top:100px;">SORRY</span>
<span class="word" style="left:150px;top:60px;">SORRY</span>

</div>

<div class="bg-hearts">
<span style="left:5%">❤️</span>
<span style="left:15%">❤️</span>
<span style="left:25%">❤️</span>
<span style="left:35%">❤️</span>
<span style="left:45%">❤️</span>
<span style="left:55%">❤️</span>
<span style="left:65%">❤️</span>
<span style="left:75%">❤️</span>
<span style="left:85%">❤️</span>
<span style="left:95%">❤️</span>
</div>

</body>
</html>

"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)

