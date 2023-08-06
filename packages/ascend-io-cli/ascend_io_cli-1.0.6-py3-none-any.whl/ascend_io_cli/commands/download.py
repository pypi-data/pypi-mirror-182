import concurrent
import logging
import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

import typer
from ascend.sdk.render import TEMPLATES_V2, download_component, download_data_service, download_dataflow
from google.protobuf.json_format import MessageToDict

from ascend_io_cli.support import get_client, print_response

app = typer.Typer(help='Download local images of data services, dataflows, and components', no_args_is_help=True)


def _configure_write_dir(write_dir: Path, unique: bool) -> Path:
  write_dir = write_dir.resolve().joinpath(f'{datetime.now().strftime("%Y%m%d%H%M%S") if unique else ""}')
  if not os.path.exists(write_dir):
    os.makedirs(write_dir, exist_ok=True)
  return write_dir


def _clean_write_dir(write_dir: Path, purge: bool):
  """The purge option will also remove the .git folder"""
  if write_dir and write_dir.exists():
    if purge:
      shutil.rmtree(write_dir)
    else:
      for ls_dir in filter((lambda d: d != '.git'), os.listdir(write_dir)):
        target = write_dir.joinpath(str(ls_dir))
        if target.is_dir():
          shutil.rmtree(target)
        elif target.is_file():
          os.remove(target)
        else:
          logging.debug(f'clean target was neither a file or a directory: {target}')


@app.command()
def data_service(
    ctx: typer.Context,
    data_service: str = typer.Argument(None, help='Data Service id to download', show_default=False),
    base_dir: str = typer.Option('./ascend', help='Base directory to write the service and flows'),
    omit_data_service_dir: bool = typer.Option(False, help='Omit the data-service folder from the directory structure if downloading a single data service'),
    purge: bool = typer.Option(False, help='Include deleting .git and other data'),
    unique: bool = typer.Option(False, help='Create unique base directory'),
    template_dir: str = typer.Option(TEMPLATES_V2, '--template_dir', show_default=False),
):
  """Download service or all services (default). The default layout will be '<base-dir>/<data-service-name>' """
  client = get_client(ctx)

  omit_data_service_dir = False if data_service is None else omit_data_service_dir

  def _download_service(ds):
    calc_base_dir = Path(base_dir).resolve()
    calc_base_dir = calc_base_dir if omit_data_service_dir else calc_base_dir.joinpath(ds.id)
    calc_base_dir = _configure_write_dir(calc_base_dir, unique)
    _clean_write_dir(calc_base_dir, purge)
    download_data_service(client=client, data_service_id=ds.id, resource_base_path=str(calc_base_dir), template_dir=template_dir)
    return ds

  futures = []
  with ThreadPoolExecutor(max_workers=ctx.obj.workers) as executor:
    for svc in client.list_data_services().data:
      if not data_service or (data_service and data_service == svc.id):
        futures.append(executor.submit(_download_service, svc))

  results = []
  for future in concurrent.futures.as_completed(futures):
    result = future.result(10)
    logging.debug(f'downloaded {result.id}')
    results.append(MessageToDict(result))
  print_response(ctx, results)


@app.command()
def dataflow(
    ctx: typer.Context,
    data_service: str = typer.Argument(..., help='Data Service id containing dataflow to download', show_default=False),
    dataflow: str = typer.Argument(..., help='Dataflow id to download', show_default=False),
    base_dir: str = typer.Option('./ascend', help='Base directory to write the data service and flow'),
    omit_data_service_dir: bool = typer.Option(False, help='Omit the data-service folder from the directory structure'),
    omit_dataflow_dir: bool = typer.Option(False, help='Omit the dataflow folder from the directory structure'),
    purge: bool = typer.Option(False, help='Include deleting .git and other data'),
    unique: bool = typer.Option(False, help='Create unique base directory'),
    template_dir: str = typer.Option(TEMPLATES_V2, '--template_dir', show_default=False),
):
  """Download a dataflow into a local directory. The default layout will be '<base-dir>/<data-service-name>/<dataflow-name>' """
  client = get_client(ctx)

  flow_obj = client.get_dataflow(data_service_id=data_service, dataflow_id=dataflow).data
  if flow_obj:
    resource_base_path = Path(base_dir).resolve()
    if not omit_data_service_dir:
      resource_base_path = resource_base_path.joinpath(data_service)
    if not omit_dataflow_dir:
      resource_base_path = resource_base_path.joinpath(dataflow)

    resource_base_path = _configure_write_dir(resource_base_path, unique)
    _clean_write_dir(resource_base_path, purge)

    download_dataflow(client, data_service_id=data_service, dataflow_id=flow_obj.id, resource_base_path=str(resource_base_path), template_dir=template_dir)

  print_response(ctx, MessageToDict(flow_obj))


@app.command()
def component(
    ctx: typer.Context,
    data_service: str = typer.Argument(..., help='Data Service id with component to download', show_default=False),
    dataflow: str = typer.Argument(..., help='Dataflow id with component to download', show_default=False),
    component: str = typer.Argument(..., help='Component id to download', show_default=False),
    base_dir: str = typer.Option('./ascend', help='Base directory to write to'),
    omit_data_service_dir: bool = typer.Option(False, help='Omit the data-service folder from the directory structure'),
    omit_dataflow_dir: bool = typer.Option(False, help='Omit the dataflow folder from the directory structure'),
    omit_component_dir: bool = typer.Option(False, help='Omit the component folder from the directory structure'),
    purge: bool = typer.Option(False, help='Include deleting .git and other data'),
    unique: bool = typer.Option(False, help='Create unique base directory'),
    template_dir: str = typer.Option(TEMPLATES_V2, '--template_dir', show_default=False),
):
  """Download an individual component into a local directory. The default layout will be '<base-dir>/<data-service-name>/<dataflow-name>/components' """
  client = get_client(ctx)

  components = client.list_dataflow_components(data_service_id=data_service, dataflow_id=dataflow).data
  target_component = list(filter(lambda c: c.id == component, components))
  resource_base_path = Path(base_dir).resolve()
  if not omit_data_service_dir:
    resource_base_path = resource_base_path.joinpath(data_service)
  if not omit_dataflow_dir:
    resource_base_path = resource_base_path.joinpath(dataflow)
  if not omit_component_dir:
    resource_base_path = resource_base_path.joinpath('components')
  resource_base_path = _configure_write_dir(resource_base_path, unique)
  _clean_write_dir(resource_base_path, purge)

  download_component(client,
                     data_service_id=data_service,
                     dataflow_id=dataflow,
                     component_id=component,
                     resource_base_path=str(resource_base_path),
                     template_dir=template_dir)

  print_response(ctx, MessageToDict(target_component[0] if len(target_component) else {}))
