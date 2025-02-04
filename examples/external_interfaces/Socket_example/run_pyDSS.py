import click
import sys
import os

@click.command()
@click.option('--pydss_path',
              default=r'C:\Users\alatif\Desktop\PyDSS')
@click.option('--sim_path',
              default=r'C:\Users\alatif\Desktop\PyDSS\examples\External_interfacing_example\pyDSS_project\Scenarios')
@click.option('--sim_file',
              default=r'socket_interface.toml')
def run_pyDSS(pydss_path, sim_path, sim_file):
    sys.path.append(pydss_path)
    sys.path.append(os.path.join(pydss_path, 'PyDSS'))
    from pyDSS import instance as dssInstance
    a = dssInstance()
    a.run(os.path.join(sim_path, sim_file))

run_pyDSS()


