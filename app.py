# app.py
from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    global visit_count
    visit_count += 1

    # Server Console(개발자만 보임)
    print(f"방문자 #{visit_count}")
    print(f"접속 시간 : {datetime.now()}")
    print('=' * 50)

    current_time = datetime.now()

    return f'''
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>oldjlim</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }}
            .container {{
                text-align: center;
                padding: 2rem;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                backdrop-filter: blur(4px);
                border: 1px solid rgba(255, 255, 255, 0.18);
            }}
            h1 {{
                font-size: 2.5rem;
                margin: 0;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>안녕하세요. 
            <br>반갑습니다. 
            <br>재광입니다.
            <br>{current_time}
            <br>{visit_count}</h1>
        </div>
    </body>
    </html>
    '''

@app.route('/admin')
def admiin() : 
    print('admin')
    return f"""
    <h2>server information<h2>
    <p>visitor : {visit_count}</p>
    <p>server time : {datetime.now()}</p>
    <p><a href="/">return to home</a></p>
    """

if __name__ == '__main__':
    app.run(debug=True)