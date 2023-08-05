import os

import litgen
from srcmlcpp.scrml_warning_settings import WarningType
from generate_hello_imgui import autogenerate_hello_imgui
from generate_im_file_dialog import autogenerate_im_file_dialog
from generate_imgui import autogenerate_imgui, autogenerate_imgui_internal
from generate_imgui_color_text_edit import autogenerate_imgui_color_text_edit
from generate_imgui_knobs import autogenerate_imgui_knobs
from generate_imgui_node_editor import autogenerate_imgui_node_editor
from generate_implot import autogenerate_implot
from generate_immvision import autogenerate_immvision
from generate_imguizmo import autogenerate_imguizmo
from generate_imgui_tex_inspect import autogenerate_imgui_tex_inspect
from generate_immapp import autogenerate_immapp
from generate_imgui_toggle import autogenerate_imgui_toggle
from generate_imspinner import autogenerate_imspinner
from generate_imgui_md import autogenerate_imgui_md
from generate_portable_file_dialogs import autogenerate_portable_file_dialogs

_THIS_DIR = os.path.dirname(__file__)
BUNDLE_DIR = os.path.realpath(_THIS_DIR + "/..")
CPP_HEADERS_DIR = BUNDLE_DIR + "/src/imgui_bundle"
CPP_GENERATED_PYBIND_DIR = BUNDLE_DIR + "/bindings"
assert os.path.isdir(CPP_HEADERS_DIR)
assert os.path.isdir(CPP_GENERATED_PYBIND_DIR)


def autogenerate_imgui_bundle():
    print("autogenerate_imgui_bundle")
    input_cpp_header = CPP_HEADERS_DIR + "/imgui_bundle.h"
    output_cpp_pydef_file = CPP_GENERATED_PYBIND_DIR + "/pybind_imgui_bundle.cpp"
    output_stub_pyi_file = CPP_GENERATED_PYBIND_DIR + "/imgui_bundle/imgui_bundle.pyi"

    # Configure options
    options = litgen.LitgenOptions()
    options.srcmlcpp_options.ignored_warnings = [WarningType.LitgenIgnoreElement]
    options.namespace_root__regex = "ImGuiBundle"
    options.fn_params_output_modifiable_immutable_to_return__regex = r".*"
    options.python_run_black_formatter = True

    litgen.write_generated_code_for_file(
        options,
        input_cpp_header_file=input_cpp_header,
        output_cpp_pydef_file=output_cpp_pydef_file,
        output_stub_pyi_file=output_stub_pyi_file,
        omit_boxed_types=True,
    )


def main():
    autogenerate_imgui()
    autogenerate_imgui_internal()
    autogenerate_implot()
    autogenerate_immvision()
    autogenerate_imgui_node_editor()
    autogenerate_hello_imgui()
    autogenerate_imgui_bundle()
    autogenerate_im_file_dialog()
    autogenerate_imgui_color_text_edit()
    autogenerate_imgui_knobs()
    autogenerate_imguizmo()
    autogenerate_imgui_tex_inspect()
    autogenerate_immapp()
    autogenerate_imgui_toggle()
    autogenerate_imspinner()
    autogenerate_imgui_md()
    autogenerate_portable_file_dialogs()


if __name__ == "__main__":
    main()
