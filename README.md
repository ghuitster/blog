# blog
My personal blog hosted at https://blog.davidmbarley.com

### Installing building tools
Ensure python3, pip, and virtualenv are installed

Then, in the root of this repo:

`virtualenv virtualenv/`

`source virtualenv/bin/activate`

`python -m pip install "pelican[markdown]"`

### Seeing build locally
Run `pelican -r -l` from the root of this repo

Then visit http://localhost:8000

### Building for production
Run `pelican content -s publishconf.py`

Put everything in `output/` into the web server
