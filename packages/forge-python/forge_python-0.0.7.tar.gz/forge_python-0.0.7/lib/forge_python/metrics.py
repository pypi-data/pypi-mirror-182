

from rich.console import Console
from rich.table import Table

from time import sleep

console = Console()


def work_on_task(time=3):
    data = [1, 2, 3, 4, 5]

    with console.status("[bold green]Fetching data..."):
        while sleep(time):
            console.status("[bold green]Fetching data...")
            break

    console.log(f'[bold][red]Done!')


def create_financial_table():
    financial_summary = [
        {"name": 'CAPEX total', "value": 54_990_000, "unit": '$'},
        {"name": 'Operating cost / yr', "value": 30_374_000, "unit": '$'},
        {"name": 'Revenues / yr', "value": 41_067_000, "unit": '$'},
        {"name": 'Net profit / yr', "value": 10_693_000, "unit": '$'},
    ]

    table = Table(show_lines=False, title="Financial Summary")
    table.add_column("Penicilin-G Financial Summary",
                     no_wrap=True)
    table.add_column("value", style="cyan", justify="right")

    for item in financial_summary:
        value = item['value']
        unit = item['unit']
        if type(value) is not float:
            if (unit == '$'):
                table.add_row(item['name'], f"${value:,d}")
            else:
                table.add_row(item['name'], f"{value:,d} {item['unit']}")
        else:
            table.add_row(item['name'], f"{value} {item['unit']}")

    console = Console()
    console.print(table)


def create_raw_materials_table():

    raw_materials = [
        {"name": 'Acetone', "unit_cost": 1.500, "annual_amount": 473_342,
            "annual_cost": 710_013, "percent": 6.88},
        {"name": 'Air', "unit_cost": 0.000, "annual_amount": 104_832_791,
            "annual_cost": 0, "percent": 0.00},
        {"name": 'Butyl Acetate', "unit_cost": 1.500,
            "annual_amount": 275_158, "annual_cost": 412_737, "percent": 4.00},
        {"name": 'Glucose', "unit_cost": 0.500, "annual_amount": 6_729_107,
            "annual_cost": 3_364_554, "percent": 32.62},
        {"name": 'H2SO4 (10% w/w)', "unit_cost": 0.201,
         "annual_amount": 297_727, "annual_cost": 59_813, "percent": 0.58},
        {"name": 'H3PO4 5%', "unit_cost": 0.051, "annual_amount": 19_366_390,
            "annual_cost": 986_718, "percent": 9.57},
        {"name": 'Inno. Media', "unit_cost": 0.201,
            "annual_amount": 995, "annual_cost": 200, "percent": 0.00},
        {"name": 'NaOH (0.5 M)', "unit_cost": 0.030, "annual_amount": 17_759_192,
         "annual_cost": 539_531, "percent": 5.23},
        {"name": 'Pharmamedium', "unit_cost": 0.850, "annual_amount": 811_898,
            "annual_cost": 690_113, "percent": 6.69},
        {"name": 'Phenoxyacetic Acid', "unit_cost": 3.000, "annual_amount": 964_100,
            "annual_cost": 2_892_300, "percent": 28.04},
        {"name": 'Sodium Acetate', "unit_cost": 2.000,
            "annual_amount": 31_100, "annual_cost": 62_200, "percent": 0.60},
        {"name": 'Sodium Hydroxid', "unit_cost": 1.500,
            "annual_amount": 174_727, "annual_cost": 262_090, "percent": 2.54},
        {"name": 'Trace metals', "unit_cost": 0.500, "annual_amount": 421_920,
            "annual_cost": 210_960, "percent": 2.05},
        {"name": 'USP Water', "unit_cost": 5.000, "annual_amount": 16_856,
            "annual_cost": 84_279, "percent": 0.82},
        {"name": 'Water', "unit_cost": 1.000, "annual_amount": 38_722,
            "annual_cost": 38_722, "percent": 0.38},
    ]

    table = Table(show_lines=False,
                  title="Raw Material Costs for this Process")
    table.add_column("Raw material", justify="left")
    table.add_column("$/kg unit cost", justify="center")
    table.add_column("kg annual", justify="center")
    table.add_column("annual $ cost", justify="left", style="cyan")
    table.add_column("% of total", justify="right")

    for item in raw_materials:
        unit_cost = str(item['unit_cost'])
        annual_amount = item['annual_amount']
        annual_cost = item['annual_cost']
        percent = str(round(item['percent'], 1)) + '%'

        table.add_row(item['name'], unit_cost,
                      f"{annual_amount:,d}", f"${annual_cost:,d}", percent)

    console = Console()
    console.print(table)


def load_metrics():
    work_on_task(2)
    print('\n')
    create_raw_materials_table()
    work_on_task(4)
    print('\n')
    create_financial_table()
