from flask import Flask
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def current_datetime():
    current_date = datetime.now().strftime("%d/%m/%Y")
    current_time = datetime.now().strftime("%H:%M:%S")
    html_content = f"""
        <table border="1">
            <tr>
                <td>Сегодня:</td>
                <td>{current_date}</td>
            </tr>
            <tr>
                <td>Текущее время:</td>
                <td>{current_time}</td>
            </tr>
        </table>
        """
    return html_content



if __name__ == '__main__':
    app.run()