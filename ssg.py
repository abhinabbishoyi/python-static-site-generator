import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest,
    }
    myobj = Site(**config)

    myobj.build()


typer.run(main)
