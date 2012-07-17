
# workflow

A tool to conceptually test out a user flow.

# Prerequisites

* [Python 2.7](http://www.python.org/download/)

# Try it out

Clone the repository and edit `cfg.cfg` to represent your flow states and transitions. Then run:

	python flow.py cfg.cfg out

This will generate an `out/` directory, with one html file for each state, with links between them representing each transition. Click around to test out your user flow.
