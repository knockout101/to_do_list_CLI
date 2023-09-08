from PIL import Image
import typer


FILE_PATH = "C:\\Users\\Maricela\\Desktop\\PythonProjects\\professional_website\\webapp\\myapp\\static\\images\\SI-icon(2).png"
DESTINATION = "C:\\Users\\Maricela\\Desktop\\"

app = typer.Typer()

@app.command()
def resize_image(file_path, new_name, format):
    img = Image.open(file_path)
    img = img.resize((30, 30), Image.Resampling.LANCZOS)
    img.save(f'{DESTINATION}{new_name}.{format.lower()}', format=format.lower())


@app.command()
def save_as_ico(file_path, name):
    img = Image.open(file_path).resize((75, 75), Image.Resampling.LANCZOS)
    img.save(name, format='ICO')


def get_img(file_path):
    return Image.open(file_path)

if __name__ == "__main__":
    app()





