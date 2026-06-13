import os


def ensure_directory_exists(
    directory_path
):

    if not os.path.exists(
        directory_path
    ):
        os.makedirs(
            directory_path
        )


def get_pdf_files(
    folder_path
):

    files = []

    for file in os.listdir(
        folder_path
    ):

        if file.lower().endswith(
            ".pdf"
        ):
            files.append(file)

    return files


def format_sources(
    sources
):

    return "\n".join(
        f"• {source}"
        for source in sources
    )