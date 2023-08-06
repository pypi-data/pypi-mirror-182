from rich import print as rprint
from rich.console import Console
from rich.progress import track
from rich.progress import Progress

from time import sleep

console = Console()


def work_on_task(time=3):
    data = [1, 2, 3, 4, 5]

    with console.status("[bold green]Fetching data..."):
        while sleep(time):
            console.status("[bold green]Fetching data...")
            break

    console.log(f'[bold][red]Done!')


def merge_dicts(*dict_args):
    merged_dict = {}
    for dictionary in dict_args:
        merged_dict.update(dictionary)
    console.log(merged_dict, log_locals=True)

    return merged_dict


def process_data():
    for _ in track(range(100), description='[green]Processing data...'):
        sleep(0.02)


def progress_multiple_tasks():
    with Progress() as progress:

        task1 = progress.add_task("[red]Downloading...", total=100)
        task2 = progress.add_task("[green]Processing...", total=100)
        task3 = progress.add_task("[cyan]Installing...", total=100)

        while not progress.finished:
            progress.update(task1, advance=0.9)
            progress.update(task2, advance=0.6)
            progress.update(task3, advance=0.3)
            sleep(0.02)


def main():
    work_on_task()
    merge_dicts({'device_id': 904592}, {'temperature': 50})
    process_data()
    progress_multiple_tasks()
