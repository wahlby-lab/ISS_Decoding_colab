def tmap_to_colab (tmap_viewer, iframe=False, iframe_height=700):
  try:
    from google.colab import output
  except:
    return
  from IPython.display import clear_output
  clear_output(wait=True)
  if iframe:
    output.serve_kernel_port_as_iframe(tmap_viewer.server.port, path=tmap_viewer.image, height=iframe_height)
  else:
    output.serve_kernel_port_as_window(tmap_viewer.server.port, path=tmap_viewer.image)
