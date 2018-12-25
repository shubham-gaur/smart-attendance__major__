from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')
setup( 
    options={
        'py2exe': {
                'compressed': 2,
                'optimize': 2,
                'dist_dir': 'dist',  # Put .exe in dist/
                'xref': False,
                'skip_archive': False,
                'ascii': False,
                'custom_boot_script': '',
                #'unbuffered': True,  # Immediately flush output.
        }
    },
    zipfile=None,  # Put libs into .exe to save space.
    console = ['main.py'],
)
