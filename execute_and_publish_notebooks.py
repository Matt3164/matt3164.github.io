import time
from pathlib import Path
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter, MarkdownExporter
from nbconvert.writers import FilesWriter

if __name__ == '__main__':

    notebook_pth = Path.cwd() / "notebooks"

    html_pth = Path.cwd() / "notebooks_md"

    html_pth.mkdir(exist_ok=True)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    # html_exporter = HTMLExporter()
    # html_exporter.template_file = 'full'

    html_exporter = MarkdownExporter()


    notebooks = list(
        filter(
            lambda x: not ("executed" in str(x)),
            notebook_pth.glob("*.ipynb"))
    )


    snippet_map_to_file = dict()

    for notebook in notebooks:
        print(f"Processing {notebook}")

        executed_notebook = notebook.with_suffix(".executed.ipynb")

        if not executed_notebook.exists():

            t = time.time()

            with open(str(notebook)) as f:
                nb = nbformat.read(f, as_version=4)

            ep.preprocess(nb, {'metadata': {'path': str(notebook_pth)}})

            print(f"Elapsed time : {time.time()-t}")

            with open(str(executed_notebook), "w") as f:
                nbformat.write(nb, f)

        # 3. Process the notebook we loaded earlier
        body, resources = html_exporter.from_filename(str(executed_notebook))

        writer = FilesWriter()
        writer.build_directory = str(html_pth)

        nb_name = executed_notebook.stem.split(".")[0]

        writer.write(body, resources, notebook_name=nb_name)


        snippet_map_to_file[nb_name] = Path("notebooks_md") / (str(nb_name)+".md")


    with open("snippets.md", "w") as f:
        f.write("# Snippets \n")
        for key, val in snippet_map_to_file.items():
            f.write(f"- [{key}]({str(val)}) \n")





