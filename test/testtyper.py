import typer
import time

def main():
    #prenom = "Ekijones"
    #typer.secho(f"Bonjour {prenom}", fg=typer.colors.BLUE, bold=True)
    prenoms = ["pat", "nat", "eki", "michel", "jose", "naruto"]
    with typer.progressbar(prenoms) as progress:
        for prenom in progress:
            time.sleep(1)
    typer.echo("Fin du scrpit.")


if __name__ == "__main__": 
    typer.run(main)