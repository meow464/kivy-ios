kfrom kivy_ios.toolchain import CythonRecipe


class PyobjusRecipe(CythonRecipe):
    version = "uikit"
    url = "https://github.com/meow464/pyobjus/archive/{version}.zip"
    library = "libpyobjus.a"
    depends = ["python"]
    pre_build_ext = True


recipe = PyobjusRecipe()
