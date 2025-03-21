from flask import Flask, render_template, send_from_directory, send_file
import os
import io
import zipfile

app = Flask(__name__, static_folder='assets', template_folder='.')
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download_project():
    # Create a BytesIO object to store the ZIP file
    memory_file = io.BytesIO()

    # Create the ZIP file
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add main files
        files_to_zip = [
            ('index.html', 'index.html'),
            ('main.py', 'main.py'),
            ('README.md', 'README.md'),
            ('assets/style.css', 'assets/style.css'),
        ]

        for file_path, zip_path in files_to_zip:
            if os.path.exists(file_path):
                zf.write(file_path, zip_path)

    # Move to the beginning of the BytesIO buffer
    memory_file.seek(0)

    return send_file(
        memory_file,
        mimetype='application/zip',
        as_attachment=True,
        download_name='hotel-dashboard.zip'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)