from flask import Flask, make_response, request, render_template
import sys
import types
from package_01.module_01.submodule_001 import file_01_001

app = Flask(__name__)


@app.route('/')
def home():
    list_routes = []
    list_routes.append(('all_libraries','All modules'))
    list_routes.append(('libraries_with_file','Modules with attribute __file__'))
    list_routes.append(('user_defined_libraries','User defined libraries'))
    list_routes.append(('add_numpy','Add library numpy and recompute libraries'))
    list_routes.append(('current_imports','Current import libraries'))
    return render_template('home.html', list_routes=list_routes)

@app.route('/libraries_with_file')
def libraries_with_file():
    sys_modules = sys.modules.copy()
    loaded_libraries = [(module_name, module.__file__) for module_name, module in sys_modules.items() if hasattr(module, '__file__')]
    loaded_libraries = sorted(loaded_libraries, key=lambda x: x[0])
    total = len(loaded_libraries)
    return render_template('libraries.html', loaded_libraries=loaded_libraries, total = total)

@app.route('/all_libraries')
def all_libraries():
    sys_modules = sys.modules.copy()
    loaded_libraries = []
    for module_name, module in sys_modules.items():
        if hasattr(module, '__file__'):
            loaded_libraries.append((module_name, module.__file__))
        else:
            loaded_libraries.append((module_name, None))
    loaded_libraries = sorted(loaded_libraries, key=lambda x: x[0])
    total = len(loaded_libraries)
    return render_template('libraries.html', loaded_libraries=loaded_libraries, total = total)

@app.route('/user_defined_libraries')
def user_defined_libraries():
    sys_modules = sys.modules.copy()
    loaded_libraries = []
    for module_name, module in sys_modules.items():
        if hasattr(module, '__file__'):
            if not module.__file__.startswith("/usr/local/lib/python3.7/"):
                loaded_libraries.append((module_name, module.__file__))
    loaded_libraries = sorted(loaded_libraries, key=lambda x: x[0])
    total = len(loaded_libraries)
    return render_template('libraries.html', loaded_libraries=loaded_libraries, total = total)

def list_imported_libraries():
    sys_modules = sys.modules.copy()
    dict_libraries = {}
    dict_libraries["libraries"] = []
    dict_libraries["total_libraries"] = 0
    for module_name, module in sys_modules.items():
        if hasattr(module, '__file__'):
            # print(f"Library: {module_name}, File: {module.__file__}")
            dict_libraries["libraries"].append({"Library": f"{module_name}", "File": f"{module.__file__}"})
            dict_libraries["total_libraries"] += 1
    dict_libraries["libraries"] = sorted(dict_libraries["libraries"], key=lambda x: x["Library"])
    return dict_libraries

@app.route('/libraries')
def get_imported_libraries():
    dict_libraries = {}
    #    for lib in sys.modules['__main__.__builtins__']:  # Python 3.6+
    #        print (lib + ' - ', getattr(__import__('__main__'), lib))
    #     for key, value in globals().items() :
    #         print ("{!s:<45}{!r:<75}".format(key ,value ))
    #    import pkgutil as pu
    #    for importer, modname, ispkg in sorted(pu.iter_imports("__main__")):
    #        print ('modname', modname )
    #        try:
    #            module= __import__(modname,__main__)
    #                print ('module', type(module), dir(module))
    dict_libraries = list_imported_libraries()
    return dict_libraries

@app.route('/libraries_counter')
def get_imported_libraries_counter():
    dict_libraries = {}
    dict_libraries = list_imported_libraries()
    return {"counter": dict_libraries["total_libraries"]}


def list_imported_user_defined_libraries():
    sys_modules = sys.modules.copy()
    dict_libraries = {}
    dict_libraries["libraries"] = []
    dict_libraries["total_libraries"] = 0
    for module_name, module in sys_modules.items():
        if hasattr(module, '__file__'):
            # print(f"Library: {module_name}, File: {module.__file__}")
            if not module.__file__.startswith("/usr/local/lib/python3.7/"):
                dict_libraries["libraries"].append({"Library": f"{module_name}", "File": f"{module.__file__}"})
                dict_libraries["total_libraries"] += 1
    dict_libraries["libraries"] = sorted(dict_libraries["libraries"], key=lambda x: x["Library"])
    return dict_libraries

@app.route('/libraries_user')
def get_imported_user_defined_libraries():
    dict_libraries = {}
    dict_libraries = list_imported_user_defined_libraries()
    return dict_libraries

@app.route('/sys_path')
def get_sys_path():
    dict_sys_path = {"list_paths": sys.path}
    return dict_sys_path

@app.route('/add_numpy')
def add_numpy():
    import numpy
    sys_modules = sys.modules.copy()
    loaded_libraries = [(module_name, module.__file__) for module_name, module in sys_modules.items() if hasattr(module, '__file__')]
    loaded_libraries = sorted(loaded_libraries, key=lambda x: x[0])
    total = len(loaded_libraries)
    return render_template('libraries.html', loaded_libraries=loaded_libraries, total = total)


@app.route('/current_imports')
def current_imports():
    loaded_libraries = []
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            if hasattr(val, '__file__'):
                loaded_libraries.append((name, val.__file__))
                # yield val.__name__
    loaded_libraries = sorted(loaded_libraries, key=lambda x: x[0])
    total = len(loaded_libraries)
    return render_template('libraries.html', loaded_libraries=loaded_libraries, total = total)



app.run(debug=True, host='localhost', port=5000)