import streamlit as st
from streamlit_labelstudio import st_labelstudio
from pathlib import Path

st.set_page_config(layout='wide')

config_folder = Path("examples/examples/image_polygons")

with open(config_folder/"config.xml","r") as f:
  config = f.read()


interfaces = [
  "panel",
  "update",
  "controls",
  "side-column",
  "completions:menu",
  "completions:add-new",
  "completions:delete",
  "predictions:menu",
],

user = {
  'pk': 1,
  'firstName': "James",
  'lastName': "Dean"
},

task = {
  'completions': [],
  'predictions': [],
  'id': 1,
  'data': {
    'image': "https://htx-misc.s3.amazonaws.com/opensource/label-studio/examples/images/nick-owuor-astro-nic-visuals-wDifg5xc9Z4-unsplash.jpg"
  }
}

results_raw = st_labelstudio(config, interfaces, user, task)
print(results_raw)

if results_raw is not None:
  areas = [v for k, v in results_raw['areas'].items()]


  results = []
  for a in areas:
    results.append({
      'id':a['id'],
      'label':a['results'][0]['value']['polygonlabels'][0],
      'points':a['points'],
    })

  for result in results:
    st.header(f'{result["label"]}: ({result["id"]})')
    st.table(result['points'])
