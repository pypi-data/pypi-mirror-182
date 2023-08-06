# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['svgfontembed']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'fonttools[woff]>=4.38.0,<5.0.0',
 'httpx>=0.23.1,<0.24.0',
 'loguru>=0.6.0,<0.7.0',
 'parsel>=1.7.0,<2.0.0',
 'rich>=12.6.0,<13.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['svgfontembed = svgfontembed.svgfontembed:app']}

setup_kwargs = {
    'name': 'svgfontembed',
    'version': '0.1.1',
    'description': '',
    'long_description': "# svgfontembed\n\nsvgfontembed is a Python CLI tool that allows you to embed fonts in SVG files, ensuring that the text in your images is displayed correctly even without internet access or if the linked font is no longer available. This is also good for privacy, as font downloads can be used for tracking purposes.\n\n## How it works\n\nsvgfontembed takes an SVG file as input and replaces any fonts that are fetched via a link with an embedded font, stripped down to only the subset of characters used within the text in the SVG. It does this by downloading the linked font and generating a base64 WOFF2 string, which is then used to replace the link in the SVG file. If an unused font is included and the `--keep-unused` option is not used, it is removed altogether.\n\nThe benefit of this is that the resulting SVG file will be self-contained and can be opened and displayed correctly on any device, even if the original font is no longer available. Additionally, the embedded font will only contain the characters that are actually used in the SVG, resulting in a smaller overall file size.\n\nIt's worth noting that the embedded font will not be cached by the browser, so if many SVG files use the same font, it may be more economical to just have the browser download the original font (though it will no longer be available offline).\n\n**Reminder:** Please be sure to observe the license of any fonts you use with this tool.\n\n## Installation\n\nsvgfontembed is available on PyPI. The recommended install method is to use `pipx`:\n\n```bash\npipx install svgfontembed\n```\n\nIt can can be installed with pip:\n\n```bash\npip install svgfontembed\n```\n\n## Usage\n\nTo use svgfontembed, simply install it using pip and run the following command:\n\n```bash\nsvgfontembed INPUT_SVG [OUTPUT_SVG] [--inplace] [--overwrite] [--keep-unused]\n```\n\n\nThis will process the input SVG file and save the resulting file with embedded fonts to the specified output file. If `--inplace` is used, the input file will be overwritten with the output. If `--overwrite` is used, any existing files will be overwritten. If `--keep-unused` is used, fonts that are not used in the SVG will not be removed.\n\n## Examples\n\nHere are some examples of how you might use svgfontembed:\n\n```bash\n# Process input.svg and save to output.svg\nsvgfontembed input.svg output.svg\n\n# Process input.svg and save to the current working directory\nsvgfontembed input.svg\n\n# Process input.svg and overwrite it with the output\nsvgfontembed input.svg --inplace\n\n# Process input.svg and save to output.svg, overwriting any existing files\nsvgfontembed input.svg output.svg --overwrite\n\n# Process input.svg and save to output.svg, keeping unused fonts in the output\nsvgfontembed input.svg output.svg --keep-unused\n```\n\n![example output with embedded font](test_files/example_light_subset.svg)\n\n## License\n\nsvgfontembed is licensed under the MIT license. See the LICENSE file for more details.\n\nTo-Do\n\n- Clean up code and dependencies\n- Test on more files (currently only files output from Excalidrawn have been tested)\n- Load fonts which are already present as embedded base64 and strip unused characters\n",
    'author': 'Pedro Batista',
    'author_email': 'pedrovhb@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
